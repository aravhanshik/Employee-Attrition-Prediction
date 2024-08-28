from fastapi import FastAPI, Request
import joblib
import pandas as pd

app = FastAPI()

# Load the trained model and label encoders
model, label_encoders = joblib.load('employee_attrition_model.pkl')

@app.get("/")
async def root():
    return {"message": "Employee Attrition Prediction API"}

@app.post("/predict")
async def predict(data: dict):
    # Convert the input data into a DataFrame
    df = pd.DataFrame([data])

    # Apply label encoding to categorical columns
    for column, le in label_encoders.items():
        df[column] = le.transform(df[column])

    # Predict
    prediction = model.predict(df)
    return {"prediction": int(prediction[0])}