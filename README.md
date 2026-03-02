# Advanced Cricket Match Performance Analysis Using Pandas & NumPy (Python)

## Project Description

The Advanced Cricket Match Performance Analysis project is a Python application that uses Pandas and NumPy to analyze multi-match cricket performance data. The program processes player statistics across different matches and teams, performs data cleaning, calculates strike rates, classifies player performance, evaluates team aggression, and identifies top performers.

This project demonstrates advanced group-based aggregation, conditional classification, cross-tabulation, and match-level analysis using structured DataFrame operations.

The application executes once and displays all computed results in the terminal.

---

## Features

* Store multi-match cricket data using a Pandas DataFrame
* Detect and handle missing run values
* Calculate strike rate for each player
* Classify player performance (Excellent, Good, Low)
* Compute total runs per team
* Calculate average team strike rate
* Compare team aggression levels
* Identify top scorers by player and by team
* Count Excellent performances per team
* Calculate total runs per match
* Identify best player per match
* Detect match with highest total runs
* Identify consistent players (Runs ≥ 40)

---

## Concepts Used

### Python Fundamentals

* Variables
* Conditional statements (if-else)
* Logical operations
* Output formatting

### Pandas Concepts

* DataFrame creation
* Missing value detection using isna()
* Data cleaning using fillna()
* Grouping using groupby()
* Aggregation using sum() and mean()
* Index selection using idxmax()
* Cross-tabulation using crosstab()
* Boolean filtering

### NumPy Concepts

* Handling missing values using np.nan
* Conditional classification using np.select()
* Numerical performance calculations

### Programming Concepts

* Multi-match sports data analysis
* Team performance comparison
* Strike rate computation
* Performance grading system
* Match-level statistical analysis
* Consistency evaluation

---

## Project Structure

```
advanced-cricket-analysis/
│
├── match_analysis.py
└── README.md
```

---

## How to Run the Program

### Requirements

* Python 3.x installed on the system
* Pandas library installed
* NumPy library installed

### Steps

1. Open terminal or command prompt
2. Navigate to the project directory
3. Run the following command:

```
python match_analysis.py
```

---

## Operations Performed

```
Phase 1 – Data Cleaning
1. Detect missing values
2. Replace missing Runs with 0
3. Calculate Strike Rate

Phase 2 – Performance Classification
4. Classify players as Excellent (≥80), Good (40–79), Low (<40)

Phase 3 – Team Analysis
5. Calculate total runs per team
6. Calculate average team strike rate
7. Calculate total balls faced per team
8. Compare team aggression using strike rate

Phase 4 – Player & Team Insights
9. Identify top scorer by player
10. Identify top scorer per team
11. Identify highest strike rate player
12. Count Excellent performances per team

Phase 5 – Match-Level Analysis
13. Calculate total runs per match
14. Identify best player in each match
15. Determine match with highest total runs
16. Identify consistent players (Runs ≥ 40)
```

---

## Sample Output

```
Indian team is more aggressive

Match with the Highest Total Runs: Match ID 3 with 220 runs.

Count of Excellent Performances per Team:
India        2
Australia    1
```

---

## Edge Cases Handled

* Missing run values safely replaced before calculations
* Accurate strike rate computation after cleaning
* Proper team comparison using aggregated averages
* Reliable identification of top performers using idxmax()
* Cross-tabulation ensures correct performance counts
* Match-wise grouping prevents data overlap

---

## Author

Meet Tailor

Python Programming Learner

---

## License

This project is created for learning and educational purposes only.

---

## Project Status

Completed

Last Updated: 2026
