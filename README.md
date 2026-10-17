# Demographic Data Analyzer

A Python data analysis project that explores demographic data extracted from the **1994 U.S. Census database** using Pandas.

Built as part of the [freeCodeCamp Data Analysis with Python Certification](https://www.freecodecamp.org/learn/data-analysis-with-python/data-analysis-with-python-projects/demographic-data-analyzer).

## Overview

This project analyzes census data to uncover demographic patterns related to age, education, income, working hours, occupation, and country of origin.

Using Pandas, the project answers key questions about the population and identifies trends among people earning more than $50,000 annually.

## Key Features

- Calculate the number of people represented from each race.
- Find the average age of men.
- Calculate the percentage of people with a Bachelor's degree.
- Compare income levels across education groups.
- Identify the minimum number of working hours per week.
- Analyze income among people working the minimum number of hours.
- Identify the country with the highest percentage of people earning over $50,000.
- Find the most common occupation among high earners in India.

## Tech Stack

- **Language:** Python
- **Data Analysis:** Pandas
- **Testing:** Python `unittest`

## Project Structure

```text
demographic-data-analyzer/
├── adult.data.csv
├── demographic_data_analyzer.py
├── main.py
├── test_module.py
├── requirements.txt
└── README.md
```

## Installation

Clone the repository:

```bash
git clone https://github.com/Sharvesh-k/demographic-data-analyzer.git
cd demographic-data-analyzer
```

Install the dependencies:

```bash
python -m pip install -r requirements.txt
```

## Run the Project

```bash
python main.py
```

The program prints the demographic analysis results to the terminal.

## Run Tests

```bash
python -m unittest test_module.py
```

## Learning Outcomes

- Loading and exploring CSV datasets with Pandas.
- Filtering and grouping data using DataFrames.
- Calculating percentages, averages, and frequency distributions.
- Applying conditional logic to demographic data.
- Using data analysis to answer real-world questions.
- Testing Python functions with unit tests.

## Dataset

The project uses the 1994 Census Income dataset from the UCI Machine Learning Repository.

**Source:** [UCI Machine Learning Repository](https://archive.ics.uci.edu/)

## Acknowledgements

Project challenge provided by [freeCodeCamp](https://www.freecodecamp.org/).

---

**Author:** [Sharvesh-k](https://github.com/Sharvesh-k)
