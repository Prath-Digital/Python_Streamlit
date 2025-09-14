import streamlit as st
import pandas as pd

st.title("Coffee Sales Data Explorer")
st.info(f"Requirements: coffee_sales.csv file and `pandas` library   \nThe data should contain this columns:\n- Date\n- City\n- Coffee Type\n- Price\n- Cups Sold\n- Revenue")
f = st.file_uploader("Upload your coffee sales CSV file", type=["csv"])

if f:
    df = pd.read_csv(f)

    st.subheader("Data Preview")
    st.dataframe(df)

if f:
    numeric_cols = df.select_dtypes(include=['number']).columns.tolist()
    st.subheader("Descriptive Statistics")
    st.write(df[numeric_cols].describe())

if f:
    st.subheader("Filter Options")
    st.markdown("> Note: This filters real data, not save as a other DataFrame")
    city_filter = st.selectbox("Select City", options=["All"] + df["City"].unique().tolist())
    coffee_filter = st.selectbox("Select Coffee Type", options=["All"] + df["Coffee Type"].unique().tolist())

    if city_filter != "All":
        df = df[df["City"] == city_filter]
    if coffee_filter != "All":
        df = df[df["Coffee Type"] == coffee_filter]

    st.dataframe(df)
