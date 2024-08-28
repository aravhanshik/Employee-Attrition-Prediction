import pandas as pd

# Load the dataset to explore its structure
data_path = 'Employee_Attrition.csv'
df = pd.read_csv(data_path)

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score
import joblib

# Preprocessing
# Encode categorical features
label_encoders = {}
for column in ['Department', 'salary']:
    le = LabelEncoder()
    df[column] = le.fit_transform(df[column])
    label_encoders[column] = le

# Define features and target
X = df.drop(columns=['left'])
y = df['left']

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a RandomForestClassifier
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# Evaluate the model
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

# Save the model
model_path = 'employee_attrition_model.pkl'
joblib.dump((model, label_encoders), model_path)