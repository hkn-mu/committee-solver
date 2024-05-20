# Installation

## Poetry

1. Download [Poetry](https://python-poetry.org/docs/#installation).
2. Run the following commands in this folder:
    ```bash
    poetry update
    poetry shell
    ```

## `pip`

Run the following commands (appropriate for your shell):
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```
   
# Usage

1. Export the Google Form responses as a CSV to this folder.
2. Edit `parse_prefs.py` to have the correct number of candidates per committee in the `totals` variable, leaving the `""`.
   Make sure the sum is _exactly_ equal to the number of candidates, otherwise you will get cryptic errors that are hard to figure out.
3. Run
   ```bash
   python parse_prefs.py <input file> <output file>
   ```
   This script transforms the responses into a CSV of the form that the solver can use.
4. Run the solver:
   ```bash
   python scheduling_solution.py <output of last script> <output file>
   ```

<!--# ~~Anirban's~~ Bryan's Notes (Spring 2023 ~~VP~~ CSec)

I've deleted the `matching.py` script.
The new method to use this solver is:

1. Download [Poetry](https://python-poetry.org/docs/#installation).
2. Run the following commands in this folder:
    ```bash
    poetry update
    ```
3. Export the Google Form responses as a CSV to this folder.
4. Edit `parse_prefs.py` to have the correct number of candidates per committee in the `totals` variable, leaving the `""`.
5. Run
   ```bash
   poetry run python parse_prefs.py <input file> <output file>
   ```
   This script transforms the responses into a CSV of the form that the solver can use.
6. Run the solver:
   ```python
   poetry run python scheduling_solution.py <output of last script> <output file>
   ```

# Shalin's Notes (Spring 22, Fall 22 Vp)
You have to make sure you specify bounds otherwise the solver will not work. Also, you have to make sure your cvxpy version is < 1.2 and cvxopt version is > 1.0.

If you see the error:
'TypeError: must be real number, not NoneType'
Then it means you are using bounds that don't allow for a valid solution. Fix em' and it should be alright


# scheduling_solution
Scheduling solution for my needs to match persons optimally to assignments based on 4 levels of preferences. 

To get started, type `python scheduling_solution.py --help`. 
An example for the input CSV file is available on the repository tmp.csv.

A solution for scheduling hell! 

Create a CSV with the following properties:
* cell A1 = 'Assignment'
* cell A2 = 'Counts'
* cells A3-A[#] being the names of the entities that require assignments. 
For instance, "Section 1", "Section 2", etc. 
* cell B1 = 'Counts'
* leave cell B2 blank
* cells B3-B[#] being the number of assignments to be made 
to the corresponding entity in A3-A[#]. For instance, Section 2 
requires 3 persons assigned to it.
* cell C1 should contain the name of a person (who needs to be 
assigned an entity)
* cell C2 should contain the count of entities to be assigned to this person
* cells C3-C[#] should contain the preferences of the person to be assigned 
to the corresponding entity. The prefernce must be {1, 2, 3, 4}, where 1 is 
"most preferred" and 4 is "cannot make it at all."
* follow the same thing for more persons as column C. 

This script can then be run by providing the input csv name and an 
output csv name. 

More options:
* It is possible to skip column B and row 2 (the counts), and let 
the program assume that all counts are 1.

* It is possible to specify the minimum/maximum counts and let 
the program generate assignments that are allowed to be over/under 
the counts provided in the CSV. 
Common use case: There are 4 homework party slots, and 18 TAs. Each 
slot needs a minimum of 4 people, but the remaining 2 can be assigned 
freely to the best preferred slot. In this case, this script can be run 
with --bound lower, specifying that the counts in the CSV are a 
lower bound.

-->
