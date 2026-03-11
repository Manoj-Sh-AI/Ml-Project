from flask import Flask, request, render_template, redirect, url_for, session
import numpy as np
import pandas as pd

# Test comment
from sklearn.preprocessing import StandardScaler
from src.pipeline.predict_pipeline import CustomData, PredictPipeline

application = Flask(__name__)

app = application
app.secret_key = "your_super_secret_key"  # Necessary for session management


## Route for a home page
@app.route("/")
def index():
    # Pop data from session, providing None as a default if not found
    results = session.pop("results", None)
    form_data = session.pop("form_data", {})  # Default to empty dict
    return render_template("home.html", results=results, form_data=form_data)


@app.route("/predictdata", methods=["POST"])
def predict_datapoint():
    data = CustomData(
        gender=request.form.get("gender"),
        race_ethnicity=request.form.get("ethnicity"),
        parental_level_of_education=request.form.get("parental_level_of_education"),
        lunch=request.form.get("lunch"),
        test_preparation_course=request.form.get("test_preparation_course"),
        reading_score=float(request.form.get("reading_score")),
        writing_score=float(request.form.get("writing_score")),
    )
    pred_df = data.get_data_as_data_frame()

    predict_pipeline = PredictPipeline()
    results = predict_pipeline.predict(pred_df)

    # Store results and form data in the session
    session["results"] = round(results[0], 2)
    session["form_data"] = request.form

    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
