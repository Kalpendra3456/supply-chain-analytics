import pandas as pd
import random
from faker import Faker

# ----------------------------------------------------
# Configuration
# ----------------------------------------------------

fake = Faker("en_IN")
random.seed(42)
Faker.seed(42)

NUM_SALES = 100000

payment_methods = [
    "Cash",
    "Credit Card",
    "Debit Card",
    "UPI",
    "Net Banking"
]

payment_status = [
    "Paid",
    "Pending",
    "Failed",
    "Refunded"
]

sales_channels = [
    "Online",
    "Retail Store",
    "Mobile App",
    "Distributor"
]

order_priority = [
    "Low",
    "Medium",
    "High",
    "Critical"
]

order_status = [
    "Completed",
    "Processing",
    "Shipped",
    "Cancelled",
    "Returned"
]

records = []

# ----------------------------------------------------
# Generate Sales Data
# ----------------------------------------------------

for sale_id in range(1, NUM_SALES + 1):

    quantity = random.randint(1, 20)

    unit_price = round(random.uniform(100, 5000), 2)

    subtotal = quantity * unit_price

    discount_percent = random.choice([0, 5, 10, 15, 20])

    discount_amount = round(
        subtotal * discount_percent / 100,
        2
    )

    taxable_amount = subtotal - discount_amount

    tax_amount = round(
        taxable_amount * 0.18,
        2
    )

    total_amount = round(
        taxable_amount + tax_amount,
        2
    )

    records.append({

        "SaleID": sale_id,

        "OrderNumber": f"ORD{202600000 + sale_id}",

        "SaleDate": fake.date_between(
            start_date="-3y",
            end_date="today"
        ),

        "Quantity": quantity,

        "UnitPrice": unit_price,

        "DiscountPercent": discount_percent,

        "DiscountAmount": discount_amount,

        "TaxAmount": tax_amount,

        "TotalAmount": total_amount,

        "PaymentMethod": random.choices(
            payment_methods,
            weights=[10, 20, 20, 40, 10]
        )[0],

        "PaymentStatus": random.choices(
            payment_status,
            weights=[90, 6, 2, 2]
        )[0],

        "SalesChannel": random.choices(
            sales_channels,
            weights=[45, 30, 15, 10]
        )[0],

        "OrderPriority": random.choices(
            order_priority,
            weights=[45, 35, 15, 5]
        )[0],

        "OrderStatus": random.choices(
            order_status,
            weights=[75, 10, 8, 4, 3]
        )[0]
    })

# ----------------------------------------------------
# Create DataFrame
# ----------------------------------------------------

df = pd.DataFrame(records)

# ----------------------------------------------------
# Save CSV
# ----------------------------------------------------

OUTPUT_FILE = "sales.csv"

df.to_csv(OUTPUT_FILE, index=False)

print(df.head())

print(f"\nSales Records Generated : {len(df):,}")
print(f"Saved As : {OUTPUT_FILE}")