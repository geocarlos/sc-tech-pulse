import streamlit as st
import duckdb
import pandas as pd  # Not explicitly used in the code, but required for duckdb .df() method to work

st.set_page_config(layout="wide")
st.title("Santa Catarina Tech Pulse")
st.subheader("Regional Entrepreneurship Insights")

con = duckdb.connect("../data/sc_business_data.duckdb")

df = con.execute("SELECT * FROM main_main.fct_startup_density").df()

total_startups = df["total_startups"].sum()
st.sidebar.metric("Total Startups in SC", f"{total_startups:,}")

st.write("### Top Tech Hubs by Startup Count")
st.bar_chart(data=df, x="city_name", y="total_startups")

st.write("### Detailed Regional Metrics")
st.dataframe(
    df.style.highlight_max(axis=0, subset=["total_employees"]),
    use_container_width=True,
    column_config={
        "total_employees": st.column_config.NumberColumn(
            "Total Employees",
            format="%d",  # This forces it to display as a signed integer
        ),
        "total_startups": st.column_config.NumberColumn(
            "Total Startups",
            format="%d",
        ),
        "avg_team_size": st.column_config.NumberColumn(
            "Avg Team Size",
            format="%.1f" 
        )
    },
)

con.close()
