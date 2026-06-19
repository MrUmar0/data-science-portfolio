# Clean Titanic Data

A simple data cleaning script that loads the classic Titanic dataset (via `seaborn`) and prepares it for analysis using `pandas`.

## What it does

- Loads the Titanic dataset from `seaborn`
- Inspects the data (`info()`, `head()`, `tail()`, shape, columns, null counts)
- Fills missing `age` values with the mean (rounded to nearest integer)
- Fills missing `embarked` and `embark_town` values with the most frequent value (mode)
- Drops the `deck` column (mostly missing values)
- Exports the cleaned dataset to `clean_titanic_data_panda.csv`

## Requirements

```bash
pip install pandas seaborn
```

## Usage

```bash
python titan.py
```

This will print dataset info to the console and generate `clean_titanic_data_panda.csv` in the same directory.

## Output

A cleaned CSV file with:
- No missing values in `age`, `embarked`, or `embark_town`
- The `deck` column removed
- `age` converted to integer type