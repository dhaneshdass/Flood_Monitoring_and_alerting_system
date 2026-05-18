import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle

data = pd.read_csv("weather_big.csv")

X = data[['temp', 'humidity', 'wind']]
y = data['rainfall']

model = LinearRegression()
model.fit(X, y)

pickle.dump(model, open("rain_model.pkl", "wb"))

print("✅ Rain model trained")