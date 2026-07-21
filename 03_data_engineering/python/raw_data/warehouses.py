import pandas as pd
import random
from faker import Faker

# ---------------------------------------
# Configuration
# ---------------------------------------

fake = Faker("en_IN")
random.seed(42)
Faker.seed(42)

NUM_WAREHOUSES = 100

# ---------------------------------------
# Warehouse Names
# ---------------------------------------

warehouse_prefix = [
    "Central", "North", "South", "East", "West",
    "Regional", "Prime", "National", "Smart",
    "Express", "Metro", "Global", "Infinity"
]

warehouse_suffix = [
    "Warehouse",
    "Distribution Center",
    "Fulfillment Center",
    "Storage Hub",
    "Logistics Center"
]

# ---------------------------------------
# Locations
# ---------------------------------------

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
    "Bhopal": "Madhya Pradesh",
    "Kolkata": "West Bengal",
    "Patna": "Bihar",
    "Chandigarh": "Chandigarh",
    "Kochi": "Kerala"
}

# ---------------------------------------
# Generate Data
# ---------------------------------------

records = []
used_names = set()

for warehouse_id in range(1, NUM_WAREHOUSES + 1):

    city = random.choice(list(cities.keys()))

    while True:
        warehouse_name = (
            f"{random.choice(warehouse_prefix)} "
            f"{city} "
            f"{random.choice(warehouse_suffix)}"
        )

        if warehouse_name not in used_names:
            used_names.add(warehouse_name)
            break

    records.append({
        "WarehouseID": warehouse_id,
        "WarehouseName": warehouse_name,
        "City": city,
        "State": cities[city],
        "Country": "India",
        "Capacity": random.randint(5000, 50000),
        "ManagerName": fake.name(),
        "OpeningDate": fake.date_between(
            start_date="-15y",
            end_date="-1y"
        )
    })

# ---------------------------------------
# DataFrame
# ---------------------------------------

df = pd.DataFrame(records)

# ---------------------------------------
# Save CSV
# ---------------------------------------

OUTPUT_FILE = "warehouses.csv"

df.to_csv(OUTPUT_FILE, index=False)

print(df.head())

print("\nWarehouses Generated Successfully!")
print(f"Total Warehouses : {len(df)}")
print(f"Saved As : {OUTPUT_FILE}")