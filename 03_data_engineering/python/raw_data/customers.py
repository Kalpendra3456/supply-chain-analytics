import pandas as pd
import random
from faker import Faker

# ----------------------------------------
# Configuration
# ----------------------------------------

fake = Faker("en_IN")
random.seed(42)
Faker.seed(42)

NUM_CUSTOMERS = 10000

# ----------------------------------------
# Locations
# ----------------------------------------

cities = {
    "Delhi": "Delhi",
    "Mumbai": "Maharashtra",
    "Pune": "Maharashtra",
    "Nagpur": "Maharashtra",
    "Bengaluru": "Karnataka",
    "Hyderabad": "Telangana",
    "Chennai": "Tamil Nadu",
    "Ahmedabad": "Gujarat",
    "Surat": "Gujarat",
    "Jaipur": "Rajasthan",
    "Lucknow": "Uttar Pradesh",
    "Noida": "Uttar Pradesh",
    "Ghaziabad": "Uttar Pradesh",
    "Kanpur": "Uttar Pradesh",
    "Indore": "Madhya Pradesh",
    "Kolkata": "West Bengal",
    "Patna": "Bihar",
    "Bhopal": "Madhya Pradesh",
    "Chandigarh": "Chandigarh",
    "Kochi": "Kerala"
}

segments = [
    "Retail",
    "Wholesale",
    "Corporate",
    "Online"
]

# ----------------------------------------
# Generate Data
# ----------------------------------------

customers = []

used_emails = set()

for customer_id in range(1, NUM_CUSTOMERS + 1):

    gender = random.choice(["Male", "Female"])

    if gender == "Male":
        name = fake.name_male()
    else:
        name = fake.name_female()

    city = random.choice(list(cities.keys()))
    state = cities[city]

    first = name.split()[0].lower()

    email = f"{first}{customer_id}@gmail.com"

    while email in used_emails:
        email = f"{first}{customer_id}{random.randint(1,99)}@gmail.com"

    used_emails.add(email)

    customers.append({
        "CustomerID": customer_id,
        "CustomerName": name,
        "Gender": gender,
        "Age": random.randint(18, 70),
        "Segment": random.choices(
            segments,
            weights=[55,15,20,10]
        )[0],
        "City": city,
        "State": state,
        "Country": "India",
        "JoinDate": fake.date_between(
            start_date="-8y",
            end_date="today"
        ),
        "Email": email,
        "Phone": fake.msisdn()[:10]
    })

# ----------------------------------------
# DataFrame
# ----------------------------------------

df = pd.DataFrame(customers)

# ----------------------------------------
# Save CSV
# ----------------------------------------

OUTPUT_FILE = "customers.csv"

df.to_csv(OUTPUT_FILE, index=False)

print(df.head())

print("\nCustomers Generated Successfully!")
print(f"Total Customers : {len(df)}")
print(f"Saved As : {OUTPUT_FILE}")