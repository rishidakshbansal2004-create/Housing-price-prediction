import pandas as pd
import random

data = []

for _ in range(300):

    area = random.randint(800, 4000)

    floors = random.randint(1, 3)

    bedrooms = random.randint(floors, 6)

    bathrooms = random.randint(1, min(5, bedrooms))

    age = random.randint(0, 30)

    price = (
        area * 1800
        + bedrooms * 500000
        + bathrooms * 100000
        + floors * 700000
        - age * 40000
        + random.randint(-150000, 150000)
    )

    data.append([
        area,
        bedrooms,
        bathrooms,
        age,
        floors,
        price
    ])

df = pd.DataFrame(
    data,
    columns=[
        "Area",
        "Bedrooms",
        "Bathrooms",
        "Age",
        "Floors",
        "Price"
    ]
)

df.to_csv("housing.csv", index=False)

print(df.head())
print("\nShape:", df.shape)