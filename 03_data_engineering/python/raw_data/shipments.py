import pandas as pd
import random
from faker import Faker
from datetime import timedelta

# -------------------------------------------------
# Configuration
# -------------------------------------------------

fake = Faker("en_IN")
random.seed(42)
Faker.seed(42)

NUM_SHIPMENTS = 80000

carriers = [
    "Blue Dart",
    "Delhivery",
    "DTDC",
    "Ecom Express",
    "India Post",
    "XpressBees",
    "FedEx",
    "DHL"
]

shipping_modes = [
    "Standard",
    "Express",
    "Same Day"
]

delivery_status = [
    "Delivered",
    "In Transit",
    "Delayed",
    "Cancelled"
]

delay_reasons = [
    "",
    "Weather Conditions",
    "Traffic Delay",
    "Vehicle Breakdown",
    "Customer Unavailable",
    "Address Issue"
]

records = []

# -------------------------------------------------
# Generate Shipments
# -------------------------------------------------

for shipment_id in range(1, NUM_SHIPMENTS + 1):

    ship_date = fake.date_between(
        start_date="-3y",
        end_date="today"
    )

    mode = random.choices(
        shipping_modes,
        weights=[60,30,10]
    )[0]

    if mode == "Same Day":
        expected = ship_date
    elif mode == "Express":
        expected = ship_date + timedelta(days=random.randint(1,3))
    else:
        expected = ship_date + timedelta(days=random.randint(4,8))

    status = random.choices(
        delivery_status,
        weights=[82,10,6,2]
    )[0]

    if status == "Delivered":
        delivery_date = expected + timedelta(days=random.randint(-1,1))
        reason = ""

    elif status == "Delayed":
        delivery_date = expected + timedelta(days=random.randint(2,7))
        reason = random.choice(delay_reasons[1:])

    else:
        delivery_date = ""
        reason = ""

    records.append({

        "ShipmentID": shipment_id,

        "SaleID": random.randint(1,100000),

        "Carrier": random.choice(carriers),

        "ShippingMode": mode,

        "ShipDate": ship_date,

        "ExpectedDelivery": expected,

        "DeliveryDate": delivery_date,

        "ShippingCost": round(random.uniform(50,1500),2),

        "TrackingNumber":
            f"TRK{random.randint(1000000000,9999999999)}",

        "DeliveryStatus": status,

        "DelayReason": reason,

        "DistanceKM": random.randint(5,2500)

    })

# -------------------------------------------------
# Create DataFrame
# -------------------------------------------------

df = pd.DataFrame(records)

# -------------------------------------------------
# Save CSV
# -------------------------------------------------

OUTPUT_FILE = "shipments.csv"

df.to_csv(OUTPUT_FILE,index=False)

print(df.head())

print(f"\nShipment Records : {len(df):,}")
print(f"Saved As : {OUTPUT_FILE}")