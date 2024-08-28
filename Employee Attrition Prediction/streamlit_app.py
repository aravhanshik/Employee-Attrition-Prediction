import streamlit as st
import requests

st.title('Employee Attrition Prediction')

# Input fields
satisfaction_level = st.slider('Satisfaction Level', 0.0, 1.0, 0.5)
last_evaluation = st.slider('Last Evaluation', 0.0, 1.0, 0.5)
number_project = st.number_input('Number of Projects', min_value=1, max_value=10, value=3)
average_montly_hours = st.number_input('Average Monthly Hours', min_value=100, max_value=300, value=200)
time_spend_company = st.number_input('Years Spent at Company', min_value=1, max_value=10, value=3)
work_accident = st.selectbox('Work Accident', [0, 1])
promotion_last_5years = st.selectbox('Promotion in Last 5 Years', [0, 1])
department = st.selectbox('Department', ['sales', 'technical', 'support', 'management', 'IT', 'product_mng', 'marketing', 'RandD', 'accounting', 'hr'])
salary = st.selectbox('Salary Level', ['low', 'medium', 'high'])

if st.button('Predict'):
    data = {
        "satisfaction_level": satisfaction_level,
        "last_evaluation": last_evaluation,
        "number_project": number_project,
        "average_montly_hours": average_montly_hours,
        "time_spend_company": time_spend_company,
        "Work_accident": work_accident,
        "promotion_last_5years": promotion_last_5years,
        "Department": department,
        "salary": salary
    }
    
    response = requests.post('http://127.0.0.1:8000/predict', json=data)
    result = response.json()

    st.write(f"Prediction: {'Left' if result['prediction'] == 1 else 'Stayed'}")