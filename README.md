# Employee Attrition Prediction Web Application

This web application predicts whether an employee is likely to leave the company based on various features such as satisfaction level, number of projects, and more. The application is built using FastAPI for the backend and Streamlit for the frontend.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Model](#model)
- [Contributing](#contributing)

## Overview
The application is designed to predict employee attrition using a machine learning model trained on a dataset containing various employee attributes. The user can input the details of an employee, and the application will return a prediction on whether the employee is likely to leave the company.

## Features
- **Prediction API**: FastAPI is used to create an API that takes employee details as input and returns a prediction.
- **User Interface**: Streamlit provides a simple and intuitive web interface for users to input data and view predictions.
- **High Accuracy**: The model achieves an accuracy of 98.83% on the test set.

## Installation

### Prerequisites
- Python 3.7+
- pip

### Install Dependencies
```bash 
pip install -r requirements.txt
```

### Usage
Start the FastAPI Application: Start the FastAPI application using Uvicorn:
```bash 
uvicorn main:app --reload
```
Run the Streamlit Application: Run the Streamlit application to open the web interface:
```bash
streamlit run streamlit_app.py
```
Input the Necessary Employee Details: Use the web interface to input the required employee details such as satisfaction level, number of projects, time spent at the company, etc.

Click on the "Predict" Button: After inputting the details, click on the "Predict" button to get the prediction on whether the employee is likely to leave the company.

### Project Structure
```bash
employee-attrition-prediction/
├── main.py                 # FastAPI backend
├── streamlit_app.py        # Streamlit frontend
├── employee_attrition_model.pkl  # Trained machine learning model
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
```

### Model
The machine learning model is trained using a RandomForestClassifier on a dataset with features such as satisfaction_level, number_project, time_spend_company, and more. The target variable is left, indicating whether an employee left the company.

### Contributing
Contributions are welcome! Please feel free to submit a Pull Request or open an Issue if you have any suggestions or improvements.


### Clone the Repository
```bash
git clone https://github.com/aravhanshik/employee-attrition-prediction.git
cd employee-attrition-prediction
```
