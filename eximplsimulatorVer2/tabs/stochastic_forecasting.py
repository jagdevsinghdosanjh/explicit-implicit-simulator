import streamlit as st
import pandas as pd
import numpy as np # noqa
import datetime
from forecasting_engine.models.stochastic import gbm_forecast
from forecasting_engine.visual.plotter import plot_stochastic


def render_stochastic_forecast_tab():
    st.markdown("## 📊 Stochastic Forecasting")
    st.write("Simulate stock prices using Geometric Brownian Motion.")

    #uploaded_file = st.file_uploader("Upload stock data CSV", type="csv")
    uploaded_file = st.file_uploader("Upload stock data CSV", type="csv", key="stochastic_upload")

    if uploaded_file:
        df = pd.read_csv(uploaded_file)
        st.dataframe(df.head())

        if 'Company' not in df.columns or 'Close' not in df.columns or 'Date' not in df.columns:
            st.error("❌ CSV must contain 'Company', 'Close', and 'Date' columns.")
            st.write("Found columns:", df.columns.tolist())
            return

        company = st.selectbox("Select Company", df['Company'].unique())
        days = st.slider("Forecast Days", 1, 30, 7)
        simulations = st.slider("Number of Simulations", 10, 1000, 100)

        subset = df[df['Company'] == company]
        if subset.empty:
            st.error("❌ No data found for selected company.")
            return

        S0 = subset['Close'].values[-1]
        last_date = pd.to_datetime(subset['Date'].values[-1])
        mu = 0.05
        sigma = 0.2
        dt = 1 / 252

        forecast_df = gbm_forecast(S0, mu, sigma, days, dt, simulations)
        forecast_df["Date"] = [
            last_date + datetime.timedelta(days=i) for i in range(len(forecast_df))
        ]

        plot_stochastic(forecast_df)

        st.download_button(
            label="Download Stochastic Forecast CSV",
            data=forecast_df.to_csv(index=False).encode("utf-8"),
            file_name="stochastic_forecast.csv",
            mime="text/csv"
        )
