import pandas as pd
import random
from faker import Faker

# -------------------------------------
# Configuration
# -------------------------------------
fake = Faker("en_IN")
random.seed(42)
Faker.seed(42)

NUM_SUPPLIERS = 500

# -------------------------------------
# Supplier Company Prefixes
# -------------------------------------
company_prefixes = [
    "Global", "Prime", "National", "Elite", "Star",
    "Reliable", "United", "Modern", "Smart", "Sunrise",
    "Shree", "Sai", "Om", "Royal", "Green",
    "Future", "Apex", "Vertex", "Infinity", "Supreme"
]

company_suffixes = [
    "Traders", "Industries", "Supplies", "Distributors",
    "Corporation", "Solutions", "Enterprises",
    "Manufacturing", "Retail", "Wholesale"
]

cities = [
    "Delhi", "Mumbai", "Bengaluru", "Hyderabad",
    "Chennai", "Pune", "Ahmedabad", "Kolkata",
    "Jaipur", "Lucknow", "Noida", "Ghaziabad",
    "Indore", "Nagpur", "Surat", "Kanpur"
]

states = {
    "Delhi": "Delhi",
    "Mumbai": "Maharashtra",
    "Bengaluru": "Karnataka",
    "Hyderabad": "Telangana",
    "Chennai": "Tamil Nadu",
    "Pune": "Maharashtra",
    "Ahmedabad": "Gujarat",
    "Kolkata": "West Bengal",
    "Jaipur": "Rajasthan",
    "Lucknow": "Uttar Pradesh",
    "Noida": "Uttar Pradesh",
    "Ghaziabad": "Uttar Pradesh",
    "Indore": "Madhya Pradesh",
    "Nagpur": "Maharashtra",
    "Surat": "Gujarat",
    "Kanpur": "Uttar Pradesh"
}

payment_terms = [
    "Advance",
    "Net 15",
    "Net 30",
    "Net 45",
    "Net 60"
]

status_list = [
    "Active",
    "Inactive",
    "Suspended"
]

records = []

used_names = set()

for supplier_id in range(1, NUM_SUPPLIERS + 1):

    while True:
        supplier_name = (
            f"{random.choice(company_prefixes)} "
            f"{fake.last_name()} "
            f"{random.choice(company_suffixes)}"
        )

        if supplier_name not in used_names:
            used_names.add(supplier_name)
            break

    city = random.choice(cities)

    records.append({
        "SupplierID": supplier_id,
        "SupplierName": supplier_name,
        "ContactPerson": fake.name(),
        "Email": fake.company_email(),
        "Phone": fake.msisdn()[:10],
        "City": city,
        "State": states[city],
        "Country": "India",
        "LeadTimeDays": random.randint(2, 30),
        "PaymentTerms": random.choice(payment_terms),
        "Rating": round(random.uniform(3.0, 5.0), 1),
        "Status": random.choices(
            status_list,
            weights=[85, 10, 5]
        )[0]
    })

# -------------------------------------
# Create DataFrame
# -------------------------------------

df = pd.DataFrame(records)

# -------------------------------------
# Save CSV
# -------------------------------------

OUTPUT_FILE = "suppliers.csv"

df.to_csv(OUTPUT_FILE, index=False)

print(df.head())
print(f"\nCSV created successfully!")
print(f"Total Suppliers: {len(df)}")
print(f"Saved as: {OUTPUT_FILE}")