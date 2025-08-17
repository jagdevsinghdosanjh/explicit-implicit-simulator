import matplotlib.pyplot as plt
import streamlit as st

def plot_gbm(df):
    fig, ax = plt.subplots()
    for col in df.columns:
        ax.plot(df.index, df[col], alpha=0.3)
    ax.set_title("GBM Forecast Paths")
    st.pyplot(fig)
