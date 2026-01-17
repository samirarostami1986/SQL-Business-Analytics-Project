# -------------------------------
# Python Script: generate_company_database
# Purpose: Generate a test database with employees, departments, salaries, projects, and assignments
# -------------------------------

import sqlite3
from faker import Faker
import random

fake = Faker()  # Library to generate fake but realistic data

# ---------- Connect to the database ----------
conn = sqlite3.connect("company.db")  # SQLite database
cursor = conn.cursor()

# ---------- Drop previous tables (optional) ----------
cursor.executescript("""
DROP TABLE IF EXISTS employee_projects;
DROP TABLE IF EXISTS salaries;
DROP TABLE IF EXISTS employees;
DROP TABLE IF EXISTS projects;
DROP TABLE IF EXISTS departments;
""")  # Start from scratch

# ---------- Create tables ----------
cursor.executescript("""
CREATE TABLE departments (
    dept_id INTEGER PRIMARY KEY,
    dept_name TEXT
);

CREATE TABLE employees (
    emp_id INTEGER PRIMARY KEY,
    name TEXT,
    dept_id INTEGER,
    hire_date DATE,
    FOREIGN KEY (dept_id) REFERENCES departments(dept_id)
);

CREATE TABLE salaries (
    salary_id INTEGER PRIMARY KEY,
    emp_id INTEGER,
    salary INTEGER,
    from_date DATE,
    to_date DATE,
    FOREIGN KEY (emp_id) REFERENCES employees(emp_id)
);

CREATE TABLE projects (
    project_id INTEGER PRIMARY KEY,
    project_name TEXT,
    budget INTEGER
);

CREATE TABLE employee_projects (
    emp_id INTEGER,
    project_id INTEGER,
    role TEXT,
    PRIMARY KEY (emp_id, project_id)
);
""")

# ---------- Insert departments ----------
departments = [
    "IT", "HR", "Finance", "Marketing", "Sales",
    "Support", "Security", "Data", "Product", "Legal"
]

for i, dept in enumerate(departments, start=1):
    cursor.execute("INSERT INTO departments VALUES (?, ?)", (i, dept))

# ---------- Insert employees ----------
num_employees = 200
for emp_id in range(1, num_employees + 1):
    cursor.execute(
        "INSERT INTO employees VALUES (?, ?, ?, ?)",
        (
            emp_id,                       # Unique employee ID
            fake.name(),                  # Random employee name
            random.randint(1, len(departments)),  # Random department
            fake.date_between(start_date="-10y", end_date="today")  # Hire date
        )
    )

# ---------- Insert salaries ----------
salary_id = 1
for emp_id in range(1, num_employees + 1):
    salary_amount = random.randint(3000, 8000)  # Random salary
    from_date = fake.date_between(
        start_date="-5y", end_date="today")  # Salary start date
    to_date = None  # Only one record per employee

    cursor.execute(
        "INSERT INTO salaries VALUES (?, ?, ?, ?, ?)",
        (salary_id, emp_id, salary_amount, from_date, to_date)
    )
    salary_id += 1

# ---------- Insert projects ----------
num_projects = 10
for pid in range(1, num_projects + 1):
    cursor.execute(
        "INSERT INTO projects VALUES (?, ?, ?)",
        (
            pid,
            fake.bs().title(),           # Random project name
            random.randint(10000, 100000)  # Project budget
        )
    )

# ---------- Insert employee-project assignments ----------
roles = ["Developer", "Manager", "Analyst", "Lead", "Consultant"]

for emp_id in range(1, num_employees + 1):
    # Each employee assigned to 1–3 random projects
    for project_id in random.sample(range(1, num_projects + 1), random.randint(1, 3)):
        cursor.execute(
            "INSERT OR IGNORE INTO employee_projects VALUES (?, ?, ?)",
            (
                emp_id,
                project_id,
                random.choice(roles)  # Random role
            )
        )

# ---------- Save and close ----------
conn.commit()   # Save all changes
conn.close()    # Close connection

print("Database generated successfully ")
