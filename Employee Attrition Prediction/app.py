from fastapi import FastAPI, Request
from pydantic import BaseModel
import joblib
import numpy as np
from sklearn.preprocessing import StandardScaler
from typing import Optional
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# Load the trained model and scaler
model = joblib.load('random_forest_model.pkl')
scaler = joblib.load('standard_scaler.pkl')

class EmployeeData(BaseModel):
    number_project: int
    average_montly_hours: float
    time_spend_company: int
    Work_accident: int
    promotion_last_5years: int
    satisfaction_level: float
    last_evaluation: float
    salary: int
    Department: int

@app.get("/", response_class=HTMLResponse)
async def read_index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/predict", response_class=HTMLResponse)
async def predict(request: Request):
    form_data = await request.json()
    data = EmployeeData(**form_data)
    
    # Convert data to a numpy array
    data_array = np.array([[
        data.number_project,
        data.average_montly_hours,
        data.time_spend_company,
        data.Work_accident,
        data.promotion_last_5years,
        data.satisfaction_level,
        data.last_evaluation,
        data.salary,
        data.Department
    ]])
    
    # Scale the data
    data_scaled = scaler.transform(data_array)
    
    # Make a prediction
    prediction = model.predict(data_scaled)[0]
    
    result = "Left" if prediction == 1 else "Stayed"
    return templates.TemplateResponse("result.html", {"request": request, "prediction": result})
