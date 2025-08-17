import matplotlib.pyplot as plt
import streamlit as st

def plot_stochastic(df):
    """
    Plots multiple stochastic simulation paths from a DataFrame.
    Assumes each column is a simulation and rows are time steps.
    """
    fig, ax = plt.subplots(figsize=(10, 5))
    for column in df.columns:
        if column != "Date":
            ax.plot(df["Date"], df[column], alpha=0.4)

    ax.set_title("Stochastic Forecast Simulations")
    ax.set_xlabel("Date")
    ax.set_ylabel("Simulated Price")
    st.pyplot(fig)

def plot_gbm(df):
    fig, ax = plt.subplots()
    for col in df.columns:
        ax.plot(df.index, df[col], alpha=0.3)
    ax.set_title("GBM Forecast Paths")
    st.pyplot(fig)

def plot_deterministic(df_euler, df_cn, title="Deterministic Forecast Comparison"):
    """
    Plots Euler vs Crank-Nicolson forecasts side-by-side.
    """
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(df_euler['Time'], df_euler['Forecast'], label='Euler Method', color='blue', linestyle='--')
    ax.plot(df_cn['Time'], df_cn['Forecast'], label='Crank-Nicolson Method', color='green', linestyle='-')
    
    ax.set_title(title)
    ax.set_xlabel("Time")
    ax.set_ylabel("Forecast Value")
    ax.legend()
    ax.grid(True)

    st.pyplot(fig)
