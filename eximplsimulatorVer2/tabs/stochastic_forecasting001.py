import streamlit as st
from forecasting_engine.models.stochastic import gbm_forecast
from forecasting_engine.visual.plotter import plot_gbm

def render_stochastic_forecast_tab():
    st.markdown("## 🔮 Stochastic Forecasting")
    S0 = st.number_input("Initial Price", value=100.0)
    mu = st.slider("Drift (μ)", 0.0, 0.2, 0.05)
    sigma = st.slider("Volatility (σ)", 0.0, 0.5, 0.2)
    days = st.slider("Forecast Days", 1, 60, 30)
    paths = st.slider("Simulation Paths", 10, 500, 100)

    forecast_df = gbm_forecast(S0, mu, sigma, days, paths)
    plot_gbm(forecast_df)
