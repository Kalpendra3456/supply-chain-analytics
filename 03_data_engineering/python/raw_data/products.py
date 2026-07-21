import pandas as pd
import random
from faker import Faker

# ----------------------------
# Configuration
# ----------------------------
fake = Faker()
random.seed(42)
Faker.seed(42)

NUM_PRODUCTS = 10000

# ----------------------------
# Categories & Products
# ----------------------------

products = {
    "Electronics": {
        "Mobile": [
            "Smartphone", "Feature Phone", "Wireless Charger",
            "Power Bank", "Phone Case"
        ],
        "Laptop": [
            "Gaming Laptop", "Business Laptop",
            "Ultrabook", "Chromebook"
        ],
        "Accessories": [
            "Bluetooth Speaker", "Smart Watch",
            "Earbuds", "Keyboard", "Mouse"
        ]
    },

    "Home Appliances": {
        "Kitchen": [
            "Mixer Grinder", "Microwave",
            "Air Fryer", "Rice Cooker"
        ],
        "Cleaning": [
            "Vacuum Cleaner",
            "Steam Mop"
        ],
        "Cooling": [
            "Ceiling Fan",
            "Air Cooler"
        ]
    },

    "Fashion": {
        "Men": [
            "T-Shirt", "Jeans",
            "Shirt", "Jacket"
        ],
        "Women": [
            "Kurti", "Dress",
            "Handbag", "Top"
        ],
        "Footwear": [
            "Sneakers",
            "Running Shoes",
            "Sandals"
        ]
    },

    "Groceries": {
        "Food": [
            "Rice", "Wheat Flour",
            "Sugar", "Cooking Oil"
        ],
        "Beverages": [
            "Tea",
            "Coffee",
            "Fruit Juice"
        ],
        "Snacks": [
            "Biscuits",
            "Chips",
            "Namkeen"
        ]
    },

    "Furniture": {
        "Living Room": [
            "Sofa",
            "Coffee Table",
            "TV Unit"
        ],
        "Bedroom": [
            "Bed",
            "Wardrobe",
            "Mattress"
        ],
        "Office": [
            "Office Chair",
            "Study Table"
        ]
    }
}

brands = [
    "Samsung","Apple","Sony","LG","Dell","HP","Lenovo",
    "Nike","Adidas","Puma","Woodland",
    "Philips","Bajaj","Prestige","Havells",
    "Godrej","Parle","Tata","Nestle","Amul",
    "IKEA","Boat","Noise","Mi","Realme"
]

units = [
    "Piece",
    "Kg",
    "Liter",
    "Pack",
    "Box"
]

records = []

for pid in range(1, NUM_PRODUCTS + 1):

    category = random.choice(list(products.keys()))

    subcategory = random.choice(
        list(products[category].keys())
    )

    product = random.choice(
        products[category][subcategory]
    )

    brand = random.choice(brands)

    cost_price = round(random.uniform(50, 50000), 2)

    margin = random.uniform(0.15, 0.50)

    unit_price = round(cost_price * (1 + margin), 2)

    weight = round(random.uniform(0.2, 25), 2)

    supplier = random.randint(1, 500)

    sku = f"SKU-{category[:3].upper()}-{pid:06}"

    launch_date = fake.date_between(
        start_date="-8y",
        end_date="today"
    )

    active = random.choices(
        [True, False],
        weights=[95,5]
    )[0]

    records.append({
        "ProductID": pid,
        "SKU": sku,
        "ProductName": f"{brand} {product}",
        "Category": category,
        "SubCategory": subcategory,
        "Brand": brand,
        "UnitPrice": unit_price,
        "CostPrice": cost_price,
        "Weight": weight,
        "UnitOfMeasure": random.choice(units),
        "SupplierID": supplier,
        "LaunchDate": launch_date,
        "IsActive": active
    })

# ----------------------------
# Create DataFrame
# ----------------------------

df = pd.DataFrame(records)

# ----------------------------
# Save CSV
# ----------------------------

OUTPUT_FILE = "products.csv"

df.to_csv(OUTPUT_FILE, index=False)

print(df.head())

print(f"\nCSV created successfully!")
print(f"Total Products : {len(df)}")
print(f"Saved as : {OUTPUT_FILE}")