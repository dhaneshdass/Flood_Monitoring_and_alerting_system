from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle

app = Flask(__name__)
CORS(app)

# Load trained models
rain_model = pickle.load(open("rain_model.pkl", "rb"))
risk_model = pickle.load(open("risk_model.pkl", "rb"))

@app.route("/predict", methods=["POST"])
def predict():

    data = request.json

    temp = data['temp']
    humidity = data['humidity']
    wind = data['wind']

    # Predict rainfall (mm)
    rainfall = rain_model.predict([[temp, humidity, wind]])[0]

    # Predict flood risk
    risk = risk_model.predict([[temp, humidity, wind]])[0]

    return jsonify({
        "rainfall": round(rainfall, 2),
        "risk": risk
    })

# Run server
app.run(debug=True)