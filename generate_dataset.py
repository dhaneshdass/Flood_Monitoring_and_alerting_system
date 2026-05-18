import pandas as pd
import random

data = []

for i in range(500):

    temp = random.randint(18, 35)
    humidity = random.randint(50, 100)
    wind = random.randint(1, 10)

    # Rainfall (mm)
    if humidity > 85:
        rainfall = random.randint(20, 60)
    elif humidity > 70:
        rainfall = random.randint(5, 20)
    else:
        rainfall = random.randint(0, 5)

    # Flood risk
    if rainfall > 40:
        risk = "High"
    elif rainfall > 15:
        risk = "Medium"
    else:
        risk = "Low"

    data.append([temp, humidity, wind, rainfall, risk])

df = pd.DataFrame(data, columns=[
    "temp", "humidity", "wind", "rainfall", "risk"
])

df.to_csv("weather_big.csv", index=False)

print("✅ Dataset created!")