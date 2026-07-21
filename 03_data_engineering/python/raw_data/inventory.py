import pandas as pd
import random
from faker import Faker

# ----------------------------------------------------
# Configuration
# ----------------------------------------------------

fake = Faker("en_IN")
random.seed(42)
Faker.seed(42)

NUM_RECORDS = 50000

records = []

# ----------------------------------------------------
# Generate Inventory Records
# ----------------------------------------------------

for _ in range(NUM_RECORDS):

    # Current Stock
    stock_qty = random.randint(50, 5000)

    # Reserved Stock (0% - 30%)
    reserved_qty = random.randint(
        0,
        int(stock_qty * 0.30)
    )

    # Available Stock
    available_qty = stock_qty - reserved_qty

    # Reorder Level (10% - 25%)
    reorder_level = random.randint(
        int(stock_qty * 0.10),
        int(stock_qty * 0.25)
    )

    # Safety Stock (5% - 15%)
    safety_stock = random.randint(
        int(stock_qty * 0.05),
        int(stock_qty * 0.15)
    )

    # Inventory Value
    unit_cost = round(random.uniform(50, 5000), 2)

    inventory_value = round(
        stock_qty * unit_cost,
        2
    )

    records.append({

        "StockQty": stock_qty,

        "ReservedQty": reserved_qty,

        "AvailableQty": available_qty,

        "ReorderLevel": reorder_level,

        "SafetyStock": safety_stock,

        "InventoryValue": inventory_value,

        "LastUpdated": fake.date_between(
            start_date="-30d",
            end_date="today"
        )

    })

# ----------------------------------------------------
# Create DataFrame
# ----------------------------------------------------

df = pd.DataFrame(records)

# ----------------------------------------------------
# Save CSV
# ----------------------------------------------------

OUTPUT_FILE = "inventory.csv"

df.to_csv(OUTPUT_FILE, index=False)

print(df.head())

print(f"\nInventory Records Generated : {len(df):,}")
print(f"Saved As : {OUTPUT_FILE}")