from patient_class import Patient
import pandas as pd
import datetime

def get_risk_level_details(risk_level):
    if risk_level == "green":
        percentage = "<10%"
    elif risk_level == "yellow":
        percentage = "10% to <20%"
    elif risk_level == "orange":
        percentage = "20% to <30%"
    elif risk_level == "red":
        percentage = "30% to <40%"
    elif risk_level == "brown":
        percentage = ">=40%"
    else:
        raise ValueError(f"Invalid risk_level! {risk_level} is not in the system.")
    return risk_level, percentage


def on_gender(gender):
    if gender=="Male":
        return True
    elif gender=="Female":
        return False
    else: raise ValueError("Invalid input for gender variable!")

def on_smoking_status(smoking_status):
    if smoking_status=="Smoker": 
        return True
    elif smoking_status=="Non-Smoker":
        return False
    else: raise ValueError("Invalid input for smoking_status variable!")

def on_diabetic_status(diabetic_status):
    if diabetic_status=="Diabetes": 
        return True
    elif diabetic_status=="Non-Diabetes":
        return False
    else: raise ValueError("Invalid input for diabetic_status variable!")

def predict_risk(name, age, is_Male, diabetes_status, smoking_status, blood_pressure, cholesterol):
    patient = Patient(name=name, age=age, is_Male=is_Male, diabetes_status=diabetes_status, smoking_status=smoking_status, blood_pressure=blood_pressure, cholesterol=cholesterol)
    return patient.risk_level()

def save_details(name, age, is_Male, diabetes_status, smoking_status, blood_pressure, cholesterol, risk_level_color, risk_level_percentage):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    details_df = pd.DataFrame({
        'Timestamp': [timestamp],
        'Name': [name],
        'Age': [age],
        'Gender': ['Male' if is_Male else 'Female'],
        'Diabetes Status': [diabetes_status],
        'Smoking Status': [smoking_status],
        'Blood Pressure': [blood_pressure],
        'Cholesterol': [cholesterol],
        'Risk Level': [risk_level_color],
        'Risk Percentage': [risk_level_percentage]
    })

    try:
        existing_df = pd.read_excel('Data/patient_details.xlsx')
        combined_df = pd.concat([existing_df, details_df], ignore_index=True)
    except FileNotFoundError:
        combined_df = details_df

    # Save the combined DataFrame to Excel
    combined_df.to_excel('Data/patient_details.xlsx', index=False)