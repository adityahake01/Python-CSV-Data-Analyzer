# Python CSV Data Analyzer

## Project Overview

A beginner-friendly command-line application developed using Python to analyze product sales data stored in CSV files.

The program calculates sales statistics, identifies the highest-revenue product, and handles common data-entry errors.

## Features

- Reads sales records from CSV files
- Calculates revenue for each product
- Calculates total sales revenue
- Calculates total quantity sold
- Counts valid product records
- Calculates average revenue per product record
- Identifies the highest-revenue product
- Skips invalid rows and reports the number skipped
- Handles missing files without crashing
- Supports different CSV files using a filename parameter
- Validates CSV column headers before processing data

## Technologies Used

- Python 3
- Python's built-in `csv` module
- Visual Studio Code

No additional Python packages are required.

## Project Structure

```text
CSV_Data_Analyzer/
├── main.py
├── sales.csv
├── test_sales.csv
└── README.md
```

## CSV Input Format

The CSV file must contain the following columns in this order:

| Product | Quantity | Price |
|---|---|---|
| Keyboard | 5 | 800 |
| Mouse | 10 | 400 |
| Monitor | 2 | 8000 |

- `Product`: Product name
- `Quantity`: Number of items sold
- `Price`: Price per item

Quantity and price must be non-negative whole numbers.

## How to Run

1. Install Python 3.
2. Open the project folder in VS Code.
3. Ensure the CSV file is saved in the project folder.
4. Open `main.py`.
5. Set the filename in the function call:

```python
if __name__ == "__main__":
    analyze_sales("sales.csv")
```

6. Open the terminal and run:

```bash
python main.py
```

To analyze a different file, replace `"sales.csv"` with the required filename, such as `"test_sales.csv"`.


## Example Output

For the six-product sample dataset in `sales.csv`:

```text
========================================
         SALES ANALYSIS REPORT
========================================
Total Revenue         : Rs. 81,200
Total Quantity Sold   : 30
Valid Product Records : 6
Average Revenue       : Rs. 13,533.33
Top Revenue Product   : Laptop
Highest Revenue       : Rs. 50,000
Invalid Rows Skipped  : 0
========================================
```



## Functions Used

### calculate_revenue(quantity, price)

Calculates and returns the revenue for one product by multiplying its quantity by its price.

### analyze_sales(filename)

Opens the specified CSV file, validates individual records, calculates sales statistics, and displays the results in the terminal.

## Error Handling

The program handles several common problems:

- Invalid numeric values
- Missing columns in a row
- Empty product names
- Negative quantities or prices
- Missing CSV files
- Detects incorrect or missing CSV headers

Invalid data rows are skipped so that remaining valid records can still be analyzed. If the CSV header is incorrect or the file is missing, the analysis stops and an error message is displayed.

## Testing

The program was tested with:

- A valid six-product sales dataset
- Invalid price values
- Missing CSV columns
- Negative quantities
- A missing CSV file
- A second CSV dataset
- An incorrect CSV header (wrong column name)
- An incorrect CSV header (wrong column order)
- A dataset containing only zero-revenue products

## Current Limitations

- The program supports whole-number quantities and prices only.
- It expects columns in the order `Product,Quantity,Price`.
- It displays results in the terminal rather than exporting a report.
- When multiple products have the same highest revenue, it reports the first one encountered.
- Average revenue is calculated per valid product record, not per individual item sold.

## Author

Aditya Sitaram Hake

Developed as a Python learning project to practice file handling, loops, conditional statements, functions, data analysis, and exception handling.
