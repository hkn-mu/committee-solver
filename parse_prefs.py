#!/usr/bin/env python3
"""Convert Google Form to a format that can be read by the scheduling solver."""

import argparse

import pandas as pd


def main() -> None:
    """Drive preference parser."""
    parser = argparse.ArgumentParser(
        description="Parses committee forms into a format that the committee solver can ingest."
    )
    parser.add_argument("input", type=str, help="Input CSV.")
    parser.add_argument("output", type=str, help="Output CSV.")
    args = parser.parse_args()

    totals = ("", 10, 7, 7, 7, 10, 7, 7, 7, 11)

    col_1 = pd.Series(
        [
            "Counts",
            "Act",
            "Bridge",
            "Compserv",
            "Decal",
            "Indrel",
            "Prodev",
            "Serv",
            "Studrel",
            "Tutoring",
        ],
        name="Assignment",
    )

    col_2 = pd.Series(totals, name="Counts")

    responses = pd.read_csv(args.input)
    responses_clean = (
        responses.iloc[:, 2:-2]
        .transpose()
        .reset_index(drop=True)
        .replace(
            {"Very much preferred": 1, "Preferred": 2, "Neutral": 3, "Do not prefer": 4}
        )
    )
    responses_clean.columns = responses_clean.iloc[0]
    responses_clean = responses_clean[1:]
    responses_clean = pd.concat(
        [
            pd.DataFrame(
                [[1] * len(responses_clean.columns)], columns=responses_clean.columns
            ),
            responses_clean,
        ]
    )

    prefs = pd.concat([col_1, col_2, responses_clean], axis=1)
    prefs.to_csv(args.output, index=False)


if __name__ == "__main__":
    main()
