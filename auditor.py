import pandas as pd
import re

df = pd.read_csv("ehr_sample.csv")
valid_genders = ['M', 'F', 'O']
bp_pattern = re.compile(r"^\d{2,3}/\d{2,3}$")
icd10_pattern = re.compile(r"^[A-Z]\d{2}(\.\d)?$")

issues = []

for index, row in df.iterrows():
    row_issues = []

    if pd.isnull(row["Age"]):
        row_issues.append("Missing Age")
    elif row["Age"] < 0 or row["Age"] > 120:
        row_issues.append("Unrealistic Age")

    if row["Gender"] not in valid_genders:
        row_issues.append("Invalid Gender")

    if not bp_pattern.match(str(row["BloodPressure"])):
        row_issues.append("Invalid Blood Pressure Format")

    try:
        hr = int(row["HeartRate"])
        if hr < 30 or hr > 180:
            row_issues.append("Heart Rate Outlier")
    except:
        row_issues.append("Invalid Heart Rate")

    if not icd10_pattern.match(str(row["DiagnosisCode"])):
        row_issues.append("Invalid Diagnosis Code")

    if row_issues:
        issues.append((row["PatientID"], row_issues))

for patient_id, errors in issues:
    print(f"Patient {patient_id} has issues: {', '.join(errors)}")
