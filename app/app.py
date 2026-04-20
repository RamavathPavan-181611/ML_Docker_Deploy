from flask import Flask, request, jsonify, render_template
import joblib
import numpy as np

app = Flask(__name__)
model = joblib.load("model.pkl")

CLASSES = ["setosa", "versicolor", "virginica"]


@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok", "model": "iris-classifier"})


@app.route("/", methods=["GET", "POST"])
def home():
    prediction = None
    probabilities = None
    error = None

    values = {
        "sepal_length": "",
        "sepal_width": "",
        "petal_length": "",
        "petal_width": ""
    }

    if request.method == "POST":
        try:
            values["sepal_length"] = request.form.get("sepal_length", "").strip()
            values["sepal_width"] = request.form.get("sepal_width", "").strip()
            values["petal_length"] = request.form.get("petal_length", "").strip()
            values["petal_width"] = request.form.get("petal_width", "").strip()

            features = np.array([
                float(values["sepal_length"]),
                float(values["sepal_width"]),
                float(values["petal_length"]),
                float(values["petal_width"])
            ]).reshape(1, -1)

            pred_idx = int(model.predict(features)[0])
            probs = model.predict_proba(features)[0]

            prediction = CLASSES[pred_idx]
            probabilities = {
                CLASSES[i]: round(float(p), 4)
                for i, p in enumerate(probs)
            }

        except ValueError:
            error = "Please enter valid numeric values in all fields."
        except Exception as e:
            error = f"Unexpected error: {str(e)}"

    return render_template(
        "index.html",
        prediction=prediction,
        probabilities=probabilities,
        error=error,
        values=values
    )


@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    if not data or "features" not in data:
        return jsonify({"error": "Send JSON with 'features' key"}), 400

    features = np.array(data["features"]).reshape(1, -1)
    prediction = int(model.predict(features)[0])
    probability = model.predict_proba(features)[0].tolist()

    return jsonify({
        "prediction": CLASSES[prediction],
        "class_index": prediction,
        "probabilities": {
            CLASSES[i]: round(p, 4) for i, p in enumerate(probability)
        }
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
