import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="☕ Coffee Sales Dashboard", layout="wide")

# Inject Cascadia Code font
st.markdown(
    """
    <style>
    @import url('https://fonts.cdnfonts.com/css/cascadia-code'); 
    html, body, [class*="css"] {
        font-family: 'Cascadia Code', monospace !important;
    }
    .stMetric label, .stMetric span {
        font-family: 'Cascadia Code', monospace !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


# Load data with caching
@st.cache_data
def load_data():
    return pd.read_csv("Data/coffee_sales.csv")


data = load_data()

# Sidebar filters
st.sidebar.header("🔍 Filters")
city = st.sidebar.multiselect(
    "Select City",
    options=sorted(data["City"].unique()),
    default=sorted(data["City"].unique()),
)
coffee_type = st.sidebar.multiselect(
    "Select Coffee Type",
    options=sorted(data["Coffee Type"].unique()),
    default=sorted(data["Coffee Type"].unique()),
)
date_range = st.sidebar.date_input(
    "Select Date Range",
    value=[pd.to_datetime(data["Date"]).min(), pd.to_datetime(data["Date"]).max()],
)

filtered_data = data[
    (data["City"].isin(city))
    & (data["Coffee Type"].isin(coffee_type))
    & (pd.to_datetime(data["Date"]) >= pd.to_datetime(date_range[0]))
    & (pd.to_datetime(data["Date"]) <= pd.to_datetime(date_range[-1]))
]

# ======================
# F-Dashboard Layout
# ======================

# Row 1: KPIs
st.markdown("## 📊 Key Metrics")
col1, col2, col3, col4, col5 = st.columns(5)
col1.metric("💰 Total Revenue", f"${filtered_data['Revenue'].sum():,.2f}")
col2.metric("🥤 Cups Sold", f"{filtered_data['Cups Sold'].sum():,}")
col3.metric("📈 Avg. Price/Cup", f"${filtered_data['Price'].mean():.2f}")
col4.metric("🏆 Top City", filtered_data.groupby("City")["Revenue"].sum().idxmax())

st.markdown("---")

# Row 2: Main Left (Bar) + Right (Line + Donut)
row1_col1, row1_col2 = st.columns([2, 3])

with row1_col1:
    st.markdown("### 🏙️ Revenue by City")
    city_rev = filtered_data.groupby("City")["Revenue"].sum().sort_values()
    fig1 = px.bar(
        city_rev,
        x=city_rev.values,
        y=city_rev.index,
        orientation="h",
        labels={"x": "Revenue", "y": "City"},
        color=city_rev.values,
        color_continuous_scale="Blues",
    )
    st.plotly_chart(fig1, use_container_width=True)

with row1_col2:
    st.markdown("### 📅 Revenue Trend Over Time")
    time_rev = filtered_data.groupby("Date")["Revenue"].sum().reset_index()
    fig2 = px.line(time_rev, x="Date", y="Revenue", markers=True)
    st.plotly_chart(fig2, use_container_width=True)

    st.markdown("### 🏷️ Revenue Share by Coffee Type")
    coffee_rev = filtered_data.groupby("Coffee Type")["Revenue"].sum().reset_index()
    fig3 = px.pie(
        coffee_rev,
        values="Revenue",
        names="Coffee Type",
        hole=0.5,
        color_discrete_sequence=px.colors.qualitative.Pastel,
    )
    st.plotly_chart(fig3, use_container_width=True)

st.markdown("---")

# Row 3: Heatmap (City vs Coffee Type)
st.markdown("### 🔥 Revenue Heatmap (City vs Coffee Type)")
heatmap_data = filtered_data.pivot_table(
    index="City", columns="Coffee Type", values="Revenue", aggfunc="sum", fill_value=0
)
fig4 = px.imshow(
    heatmap_data,
    aspect="auto",
    color_continuous_scale="YlOrBr",
    labels=dict(x="Coffee Type", y="City", color="Revenue"),
)
st.plotly_chart(fig4, use_container_width=True)

st.markdown("---")

# Row 4: Data + Insights
col_data, col_insights = st.columns([3, 2])

with col_data:
    st.markdown("### 📑 Data Preview")
    st.dataframe(filtered_data)
    st.download_button(
        "📥 Download Filtered Data",
        data=filtered_data.to_csv(index=False),
        file_name="filtered_coffee_sales.csv",
        mime="text/csv",
    )

with col_insights:
    st.markdown("### 📝 Quick Insights")
    top_city = filtered_data.groupby("City")["Revenue"].sum().idxmax()
    top_city_val = filtered_data.groupby("City")["Revenue"].sum().max()
    top_coffee = filtered_data.groupby("Coffee Type")["Revenue"].sum().idxmax()
    st.write(f"- 🏆 **{top_city}** leads with **${top_city_val:,.2f}** revenue.")
    st.write(f"- ☕ Best seller: **{top_coffee}** coffee.")
    st.write(
        f"- 📅 Period covers **{filtered_data['Date'].min()} → {filtered_data['Date'].max()}**."
    )
