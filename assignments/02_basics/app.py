import streamlit as st
from datetime import datetime
# Make a small calculator in that the current date is in the backend, when user selects dob, print the years, months, and days, it is also called as age calculator

st.title("Age Calculator")

# Get the current date
current_date = datetime.now()

# User input for date of birth
dob = st.date_input("Select your date of birth")

if dob:
    # Calculate perfect years, months, and days
    dob_dt = datetime(dob.year, dob.month, dob.day)
    delta = current_date - dob_dt
    years = current_date.year - dob.year
    months = current_date.month - dob.month
    days = current_date.day - dob.day

    if days < 0:
        months -= 1
        prev_month = (current_date.month - 1) if current_date.month > 1 else 12
        prev_month_year = current_date.year if current_date.month > 1 else current_date.year - 1
        days_in_prev_month = (datetime(prev_month_year, prev_month % 12 + 1, 1) - datetime(prev_month_year, prev_month, 1)).days
        days += days_in_prev_month
    if months < 0:
        years -= 1
        months += 12

    if years < 0 or months < 0 or days < 0:
        st.error("Invalid Date of Birth")
    else:
        st.success(f"You are {years} years, {months} months, and {days} days old.")

st.info("Thank you for sharing your Date of Birth!\nFeel free to explore more about it and happy coding!🚀\n- ***Prath-Digital*** 🧑🏻‍💻")
