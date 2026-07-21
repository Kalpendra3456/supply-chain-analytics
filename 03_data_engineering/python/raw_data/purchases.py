import pandas as pd
import random
from faker import Faker
from datetime import timedelta

# ----------------------------------------------------
# Configuration
# ----------------------------------------------------

fake = Faker("en_IN")
random.seed(42)
Faker.seed(42)

NUM_PURCHASES = 50000

status_options = [
    "Delivered",
    "In Transit",
    "Delayed",
    "Cancelled"
]

records = []

# ----------------------------------------------------
# Generate Purchase Records
# ----------------------------------------------------

for purchase_id in range(1, NUM_PURCHASES + 1):

    purchase_date = fake.date_between(
        start_date="-3y",
        end_date="today"
    )

    quantity = random.randint(10, 500)

    unit_cost = round(
        random.uniform(50, 5000),
        2
    )

    subtotal = quantity * unit_cost

    freight_cost = round(
        subtotal * random.uniform(0.01, 0.05),
        2
    )

    tax_amount = round(
        (subtotal + freight_cost) * 0.18,
        2
    )

    total_cost = round(
        subtotal + freight_cost + tax_amount,
        2
    )

    expected_delivery = purchase_date + timedelta(
        days=random.randint(3, 15)
    )

    status = random.choices(
        status_options,
        weights=[80, 10, 7, 3]
    )[0]

    if status == "Delivered":
        actual_delivery = expected_delivery + timedelta(
            days=random.randint(-2, 2)
        )

    elif status == "Delayed":
        actual_delivery = expected_delivery + timedelta(
            days=random.randint(3, 10)
        )

    else:
        actual_delivery = ""

    records.append({

        "PurchaseID": purchase_id,

        "PurchaseDate": purchase_date,

        "Quantity": quantity,

        "UnitCost": unit_cost,

        "FreightCost": freight_cost,

        "TaxAmount": tax_amount,

        "TotalCost": total_cost,

        "ExpectedDelivery": expected_delivery,

        "ActualDelivery": actual_delivery,

        "Status": status
    })

# ----------------------------------------------------
# Create DataFrame
# ----------------------------------------------------

df = pd.DataFrame(records)

# ----------------------------------------------------
# Save CSV
# ----------------------------------------------------

OUTPUT_FILE = "purchases.csv"

df.to_csv(OUTPUT_FILE, index=False)

print(df.head())

print(f"\nPurchase Records Generated : {len(df):,}")
print(f"Saved As : {OUTPUT_FILE}")