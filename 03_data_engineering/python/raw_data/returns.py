import pandas as pd
import random
from faker import Faker

# -------------------------------------------------
# Configuration
# -------------------------------------------------

fake = Faker("en_IN")
random.seed(42)
Faker.seed(42)

NUM_RETURNS = 10000
NUM_EMPLOYEES = 500

return_reasons = [
    "Damaged Product",
    "Wrong Item",
    "Defective Product",
    "Quality Issue",
    "Late Delivery",
    "Customer Changed Mind",
    "Incorrect Size",
    "Missing Parts"
]

return_types = [
    "Refund",
    "Replacement",
    "Exchange"
]

status_options = [
    "Pending",
    "Approved",
    "Rejected",
    "Completed"
]

records = []

# -------------------------------------------------
# Generate Return Records
# -------------------------------------------------

for return_id in range(1, NUM_RETURNS + 1):

    quantity = random.randint(1, 5)

    refund_amount = round(
        random.uniform(200, 25000),
        2
    )

    records.append({

        "ReturnID": return_id,

        "ReturnDate": fake.date_between(
            start_date="-3y",
            end_date="today"
        ),

        "Quantity": quantity,

        "ReturnReason": random.choices(
            return_reasons,
            weights=[20, 12, 18, 15, 10, 15, 5, 5]
        )[0],

        "RefundAmount": refund_amount,

        "ReturnType": random.choices(
            return_types,
            weights=[60, 25, 15]
        )[0],

        "ProcessedBy": random.randint(
            1,
            NUM_EMPLOYEES
        ),

        "Status": random.choices(
            status_options,
            weights=[10, 25, 5, 60]
        )[0]

    })

# -------------------------------------------------
# Create DataFrame
# -------------------------------------------------

df = pd.DataFrame(records)

# -------------------------------------------------
# Save CSV
# -------------------------------------------------

OUTPUT_FILE = "returns.csv"

df.to_csv(OUTPUT_FILE, index=False)

print(df.head())

print(f"\nReturn Records Generated : {len(df):,}")
print(f"Saved As : {OUTPUT_FILE}")