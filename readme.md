# Data analysis demo with only numpy

## Description
This simple demo is intended to perform basic data analysis using only numpy in following steps:

### Data and table generation:
- Read Georgian name, surname data from 'data.json' file
- Generate random student full names using this data
- Generate random matrix of student scores using numpy
- Add student names list to scores matrix as a first column
- Add topic names as a first row to simulate a table in numpy

### Data analysis in 3 steps:
- Calculating the average score for each student and finding the best
- Finding best and worst students in math
- Finding students with better-than-average English scores

### Note
Each of the above step builds a string which is then written to 'output.txt'

## Requirements
- Python 3.x
- numpy
- tabulate

To install required packages, run in terminal:
```bash
pip install -r requirements.txt
```
