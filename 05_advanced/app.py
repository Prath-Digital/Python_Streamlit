import streamlit as st
import requests as req
from bs4 import BeautifulSoup as bs

st.title("💱 Live Currency Converter")
st.markdown("""
Welcome to the Live Currency Converter!

**Instructions:**
- Use the sidebar to select currencies and enter the amount you want to convert.
- Click the **Convert** button to see the result in the sidebar.

This app uses real-time exchange rates from ExchangeRate-API.
""")

currency_options = ["USD", "EUR", "GBP", "INR"]
st.sidebar.header("Currency Converter Settings")
from_currency = st.sidebar.selectbox("From Currency", currency_options)
to_currency = st.sidebar.selectbox("To Currency", currency_options)
amount = st.sidebar.number_input("Amount", min_value=1)

if st.sidebar.button("Convert"):
    api_key = "57e22eb51281ac0ecd859416"
    url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/{from_currency}"
    response = req.get(url)
    data = response.json()
    if data.get("result") == "success":
        rate = data["conversion_rates"].get(to_currency)
        if rate:
            converted_amount = amount * rate
            st.sidebar.success(f"{amount} {from_currency} = {converted_amount} {to_currency}")
        else:
            st.sidebar.error("Conversion rate not found.")
    else:
        st.sidebar.error("Error fetching exchange rates.")