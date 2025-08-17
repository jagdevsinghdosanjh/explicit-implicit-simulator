import streamlit as st
import pandas as pd
from utils.finance_models import forward_euler_forecast

def render_financial_tab():
    st.markdown("## 📈 Financial Forecasting")
    st.write("Apply numerical methods to forecast multi-company stock trends.")

    uploaded_file = st.file_uploader("Upload stock data CSV", type="csv")
    if uploaded_file:
        df = pd.read_csv(uploaded_file)
        st.dataframe(df.head())

        company = st.selectbox("Select Company", df['Company'].unique())
        days = st.slider("Forecast Days", 1, 30, 7)
        method = st.radio("Choose Method", ["Forward Euler", "Crank-Nicolson"])

        forecast = forward_euler_forecast(df[df['Company'] == company], days)
        st.line_chart(forecast)
