import pandas as pd
import random
from faker import Faker

# ----------------------------------------------------
# Configuration
# ----------------------------------------------------

fake = Faker("en_IN")
random.seed(42)
Faker.seed(42)

NUM_EMPLOYEES = 500

# ----------------------------------------------------
# Departments & Roles
# ----------------------------------------------------

department_roles = {
    "Sales": [
        "Sales Executive",
        "Sales Manager",
        "Sales Associate"
    ],

    "Marketing": [
        "Marketing Executive",
        "Digital Marketing Specialist",
        "Marketing Manager"
    ],

    "Finance": [
        "Accountant",
        "Finance Executive",
        "Finance Manager"
    ],

    "Human Resources": [
        "HR Executive",
        "HR Manager",
        "Recruiter"
    ],

    "Information Technology": [
        "Data Analyst",
        "Business Analyst",
        "Software Engineer",
        "System Administrator",
        "Database Administrator"
    ],

    "Operations": [
        "Operations Executive",
        "Operations Manager"
    ],

    "Procurement": [
        "Procurement Executive",
        "Procurement Manager",
        "Buyer"
    ],

    "Customer Support": [
        "Customer Support Executive",
        "Support Manager"
    ]
}

salary_range = {
    "Sales Executive": (30000, 50000),
    "Sales Associate": (25000, 40000),
    "Sales Manager": (70000, 120000),

    "Marketing Executive": (35000, 55000),
    "Digital Marketing Specialist": (45000, 70000),
    "Marketing Manager": (80000, 130000),

    "Accountant": (35000, 60000),
    "Finance Executive": (45000, 70000),
    "Finance Manager": (90000, 150000),

    "HR Executive": (35000, 60000),
    "Recruiter": (30000, 50000),
    "HR Manager": (80000, 130000),

    "Data Analyst": (50000, 90000),
    "Business Analyst": (60000, 100000),
    "Software Engineer": (60000, 120000),
    "System Administrator": (50000, 90000),
    "Database Administrator": (60000, 100000),

    "Operations Executive": (35000, 60000),
    "Operations Manager": (70000, 120000),

    "Procurement Executive": (35000, 60000),
    "Buyer": (40000, 70000),
    "Procurement Manager": (80000, 130000),

    "Customer Support Executive": (25000, 45000),
    "Support Manager": (60000, 100000)
}

status_options = [
    "Active",
    "On Leave",
    "Resigned"
]

records = []
used_emails = set()

# ----------------------------------------------------
# Generate Employees
# ----------------------------------------------------

for emp_id in range(1, NUM_EMPLOYEES + 1):

    department = random.choice(list(department_roles.keys()))
    role = random.choice(department_roles[department])

    name = fake.name()

    email = (
        name.lower()
        .replace(" ", ".")
        .replace(".", "") +
        str(emp_id) +
        "@company.com"
    )

    while email in used_emails:
        email = f"employee{emp_id}{random.randint(100,999)}@company.com"

    used_emails.add(email)

    min_salary, max_salary = salary_range[role]

    records.append({
        "EmployeeID": emp_id,
        "EmployeeName": name,
        "Department": department,
        "Role": role,
        "HireDate": fake.date_between(
            start_date="-10y",
            end_date="today"
        ),
        "Salary": random.randint(
            min_salary,
            max_salary
        ),
        "Email": email,
        "Phone": fake.msisdn()[:10],
        "Status": random.choices(
            status_options,
            weights=[88, 7, 5]
        )[0]
    })

# ----------------------------------------------------
# Create DataFrame
# ----------------------------------------------------

df = pd.DataFrame(records)

# ----------------------------------------------------
# Save CSV
# ----------------------------------------------------

OUTPUT_FILE = "employees.csv"

df.to_csv(OUTPUT_FILE, index=False)

print(df.head())

print("\nEmployees CSV Generated Successfully!")
print(f"Total Employees : {len(df)}")
print(f"Saved As : {OUTPUT_FILE}")