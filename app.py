from flask import Flask, render_template, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

model = joblib.load("model.pkl")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()

        area = float(data["area"])
        bedrooms = int(data["bedrooms"])
        bathrooms = float(data["bathrooms"])
        floors = float(data["floors"])
        waterfront = int(data["waterfront"])
        grade = int(data["grade"])

        # validation
        if area <= 0:
            return jsonify({"price": "Invalid input"})

        features = np.array([[area, bedrooms, bathrooms, floors, waterfront, grade]])

        prediction = model.predict(features)[0]

        # prevent negative
        prediction = max(0, prediction)

        # convert to lakhs
        prediction = prediction / 100000

        return jsonify({"price": round(prediction, 2)})

    except Exception as e:
        print("ERROR:", e)
        return jsonify({"price": "Error"})

if __name__ == "__main__":
    app.run(debug=True)