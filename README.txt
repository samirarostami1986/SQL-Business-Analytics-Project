# SQL Business Analytics Project – Company Database

This project demonstrates practical SQL skills using a synthetic company database.  
The focus is on data analysis, aggregation, joins, subqueries, and window functions commonly used in Business Intelligence and Data Analyst roles.

The database is generated using a Python script and analyzed using SQL queries.

## Project Overview

- Creation of a synthetic company database including employees, departments, projects, salaries, and employee-project assignments.
- SQL-based analysis without visualization.
- Focus on clean, readable queries and realistic business questions.
- Suitable for entry-level and junior data analytics practice.

## Technologies Used

- Python (for data generation)
- SQLite
- SQL (JOINs, GROUP BY, subqueries, CTEs, window functions)
- DB Browser for SQLite
- Git and GitHub

## Database Structure

The database contains the following tables:

- employees
- departments
- projects
- employee_projects
- salaries

All data is randomly generated for learning and practice purposes.

## Python Script

The database is created using the Python script:

generate_company_database.py

Run the script to generate or refresh the SQLite database (company.db).

## How to Run

1. Open a terminal or command prompt.
2. Navigate to the project folder.
3. Run the Python script:

python generate_company_database.py

After running the script, the SQLite database file (company.db) will be created automatically.

## Notes

- Data is randomly generated each time the script runs.
- Each employee is assigned to one to three random projects.
- Each employee has exactly one salary record.
- The database is ready for SQL practice and testing queries.

## SQL Queries

All practice SQL queries are included in the DB Browser project file:

company_queries.sqbpro

This file contains all SQL queries used for analysis, including joins, aggregations, ranking, and window functions.

## Sample Queries and Outputs

For demonstration purposes, only the first two queries have their results included as CSV files:

1️⃣ Employees with salary, highest first  
- File: employees_salary.csv  
- Lists all employees with their salary in descending order.

2️⃣ Rank employees by salary across the company  
- File: ranked_salary.csv  
- Assigns a rank to each employee based on salary across the company.

Both CSV files are ready to view on GitHub and can be used as sample results.

All other queries are available in company_queries.sqbpro for practice and execution.

## Project Files

| File | Description |
|------|-------------|
| generate_company_database.py | Python script to generate the SQLite database |
| company.db | The SQLite database containing all tables and data |
| company_queries.sqbpro | DB Browser project file with all SQL queries |
| employees_salary.csv | Sample output for Query 1 |
| ranked_salary.csv | Sample output for Query 2 |

## License

This project is free to use for learning and practice purposes.
