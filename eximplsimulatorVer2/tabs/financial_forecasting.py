import streamlit as st
import pandas as pd
import datetime
from forecasting_engine.models.deterministic import euler_forecast, crank_nicolson_forecast
from forecasting_engine.visual.plotter import plot_deterministic


def render_financial_tab():
    st.markdown("## 📈 Financial Forecasting")
    st.write("Apply numerical methods to forecast multi-company stock trends.")

    #uploaded_file = st.file_uploader("Upload stock data CSV", type="csv")
    uploaded_file = st.file_uploader("Upload stock data CSV", type="csv", key="financial_upload")

    if uploaded_file:
        df = pd.read_csv(uploaded_file)
        st.dataframe(df.head())

        if 'Company' not in df.columns or 'Close' not in df.columns or 'Date' not in df.columns:
            st.error("❌ CSV must contain 'Company', 'Close', and 'Date' columns.")
            st.write("Found columns:", df.columns.tolist())
            return

        company = st.selectbox("Select Company", df['Company'].unique())
        days = st.slider("Forecast Days", 1, 30, 7)
        method = st.radio("Choose Method", ["Forward Euler", "Crank-Nicolson"])

        subset = df[df['Company'] == company]
        if subset.empty:
            st.error("❌ No data found for selected company.")
            return

        S0 = subset['Close'].values[-1]
        last_date = pd.to_datetime(subset['Date'].values[-1])
        r = 0.05
        T = days / 252
        dt = 1 / 252

        forecast_df = (
            euler_forecast(S0, r, T, dt)
            if method == "Forward Euler"
            else crank_nicolson_forecast(S0, r, T, dt)
        )

        forecast_df.columns = ["Time", "Forecast"]
        forecast_df["Date"] = [
            last_date + datetime.timedelta(days=int(t * 252))
            for t in forecast_df["Time"]
        ]
        forecast_df = forecast_df[["Date", "Forecast"]]

        st.line_chart(forecast_df.set_index("Date")["Forecast"])

        st.download_button(
            label=f"Download {method} Forecast CSV",
            data=forecast_df.to_csv(index=False).encode("utf-8"),
            file_name=f"{method.lower().replace(' ', '_')}_forecast.csv",
            mime="text/csv"
        )


def render_financial_forecast_tab():
    st.header("Deterministic Forecasting")

    S0 = st.number_input("Initial Value (S₀)", value=100.0)
    r = st.slider("Interest Rate (r)", min_value=0.01, max_value=0.2, value=0.05)
    T = st.slider("Time Horizon (T in years)", min_value=1, max_value=10, value=1)
    dt = st.selectbox("Time Step (dt)", options=[0.01, 0.05, 0.1], index=0)

    df_euler = euler_forecast(S0, r, T, dt)
    df_cn = crank_nicolson_forecast(S0, r, T, dt)

    df_euler.columns = ["Time", "Forecast"]
    df_cn.columns = ["Time", "Forecast"]

    plot_deterministic(df_euler, df_cn)

    st.download_button(
        label="Download Euler Forecast CSV",
        data=df_euler.to_csv(index=False).encode("utf-8"),
        file_name="euler_forecast.csv",
        mime="text/csv"
    )

    st.download_button(
        label="Download Crank-Nicolson Forecast CSV",
        data=df_cn.to_csv(index=False).encode("utf-8"),
        file_name="crank_nicolson_forecast.csv",
        mime="text/csv"
    )
