import streamlit as st
import pandas as pd

st.set_page_config(page_title="EHR Data Quality Auditor", layout="wide")

st.title("🩺 EHR Data Quality Auditor")

uploaded_file = st.file_uploader("Upload your EHR CSV file", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write("### Uploaded Data", df.head())

    completeness = df.notnull().mean() * 100
    st.write("### Completeness Score (%)", completeness)

    st.write("### Missing Data Matrix")
    st.dataframe(df.isnull())

    invalid_gender = df[~df["Gender"].isin(['M', 'F', 'O'])]
    if not invalid_gender.empty:
        st.warning("⚠️ Found records with invalid gender codes:")
        st.dataframe(invalid_gender)
