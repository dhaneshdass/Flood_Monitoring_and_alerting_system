import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import pickle

data = pd.read_csv("weather_big.csv")

X = data[['temp', 'humidity', 'wind']]
y = data['risk']

model = DecisionTreeClassifier()
model.fit(X, y)

pickle.dump(model, open("risk_model.pkl", "wb"))

print("✅ Risk model trained")