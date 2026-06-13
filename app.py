
from flask import Flask, render_template, request
import os

from utils.biomedclip_predict import predict_xray
from utils.disease_info import disease_info
from utils.condition_mapper import infer_conditions

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    # Get uploaded image
    file = request.files["image"]

    # Save image
    filepath = os.path.join(
        app.config["UPLOAD_FOLDER"],
        file.filename
    )

    file.save(filepath)

    # AI prediction
    result = predict_xray(filepath)

    # Disease reasoning engine
    conditions = infer_conditions(result)

    # Sort findings
    sorted_result = sorted(
        result.items(),
        key=lambda x: x[1],
        reverse=True
    )

    top5 = []

    for disease, score in sorted_result[:5]:

        if disease in disease_info:

            info = disease_info[disease]

            if score >= 0.8:
                confidence = "High"

            elif score >= 0.6:
                confidence = "Moderate"

            elif score >= 0.4:
                confidence = "Low"

            else:
                confidence = "Very Low"

            top5.append({

                "medical_name": disease,

                "display_name": info["display_name"],

                "description": info["description"],

                "icon": info["icon"],

                "score": round(float(score), 4),

                "confidence": confidence

            })

    return render_template(
        "index.html",
        predictions=top5,
        conditions=conditions
    )


if __name__ == "__main__":
    app.run(debug=True)
