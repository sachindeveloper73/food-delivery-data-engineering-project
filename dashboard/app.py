import pandas as pd
import streamlit as st

# Page config
st.set_page_config(page_title="Food Analytics", layout="wide")

# Title
st.markdown("## 🚀 Food Delivery Analytics Dashboard")

# Load data
df = pd.read_parquet("gold/sales_by_city")

# -----------------------
# KPIs
# -----------------------
total_revenue = df["sum(amount)"].sum()
avg_revenue = df["sum(amount)"].mean()
top_city = df.sort_values("sum(amount)", ascending=False).iloc[0]["city"]

col1, col2, col3 = st.columns(3)

col1.metric("💰 Total Revenue", f"₹{total_revenue:,.0f}")
col2.metric("📊 Avg Revenue/City", f"₹{avg_revenue:,.0f}")
col3.metric("🏆 Top City", top_city)

st.markdown("---")

# -----------------------
# Sidebar Filters
# -----------------------
st.sidebar.header("🔍 Filters")

cities = df["city"].unique()
selected_cities = st.sidebar.multiselect("Select Cities", cities, default=cities)

filtered_df = df[df["city"].isin(selected_cities)]

# -----------------------
# Charts
# -----------------------

col1, col2 = st.columns(2)

with col1:
    st.subheader("📊 Revenue by City")
    st.bar_chart(filtered_df.set_index("city"))

with col2:
    st.subheader("📈 Revenue Distribution")
    st.line_chart(filtered_df.set_index("city"))

# -----------------------
# Top Cities Table
# -----------------------

st.subheader("🏆 Top 5 Cities")

top5 = filtered_df.sort_values("sum(amount)", ascending=False).head(5)
st.dataframe(top5)

# -----------------------
# Raw Data Toggle
# -----------------------

if st.checkbox("Show Raw Data"):
    st.dataframe(filtered_df)

# Footer
st.markdown("---")
st.caption("Built using PySpark + Airflow + Streamlit 🚀")
