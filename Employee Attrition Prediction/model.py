import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.model_selection import train_test_split
import joblib

# Load and preprocess data
emp_data = pd.read_csv("Employee_Attrition.csv")
emp_data1 = emp_data.drop_duplicates()
emp_data1['salary'] = LabelEncoder().fit_transform(emp_data1['salary'])
emp_data1['Department'] = LabelEncoder().fit_transform(emp_data1['Department'])

x = emp_data1.drop(['left'], axis=1)
y = emp_data1['left']

# Split data into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# Initialize and fit the scaler
std_scaler = StandardScaler()
x_train_scaled = std_scaler.fit_transform(x_train)
x_test_scaled = std_scaler.transform(x_test)

# Initialize and train the model
Random_Forest_model = RandomForestClassifier()
Random_Forest_model.fit(x_train_scaled, y_train)

# Save the model and scaler
joblib.dump(Random_Forest_model, 'random_forest_model.pkl')
joblib.dump(std_scaler, 'standard_scaler.pkl')

print("Model and scaler saved successfully.")
