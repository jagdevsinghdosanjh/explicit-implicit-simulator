import streamlit as st
import pandas as pd
from forecasting_engine.models.deterministic import euler_forecast, crank_nicolson_forecast
from forecasting_engine.visual.plotter import plot_deterministic


def render_financial_tab():
    st.markdown("## 📈 Financial Forecasting")
    st.write("Apply numerical methods to forecast multi-company stock trends.")

    uploaded_file = st.file_uploader("Upload stock data CSV", type="csv")
    if uploaded_file:
        df = pd.read_csv(uploaded_file)
        st.dataframe(df.head())

        # Check for 'Company' column
        if 'Company' not in df.columns:
            st.error("❌ The uploaded file must contain a 'Company' column.")
            st.write("Columns found:", df.columns.tolist())
            return

        company = st.selectbox("Select Company", df['Company'].unique())
        days = st.slider("Forecast Days", 1, 30, 7)
        method = st.radio("Choose Method", ["Forward Euler", "Crank-Nicolson"])

        subset = df[df['Company'] == company]
        if subset.empty or 'Close' not in subset.columns:
            st.error("❌ No valid 'Close' prices found for selected company.")
            return

        S0 = subset['Close'].values[-1]
        r = 0.05  # Fixed rate; can be made dynamic
        T = days / 252  # Convert days to years
        dt = 1 / 252

        if method == "Forward Euler":
            forecast_df = euler_forecast(S0, r, T, dt)
        else:
            forecast_df = crank_nicolson_forecast(S0, r, T, dt)

        forecast_df.columns = ["Time", "Forecast"]
        st.line_chart(forecast_df["Forecast"])

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
