import matplotlib.pyplot as plt
import streamlit as st

def plot_solutions(y_values, dt, method):
    t = [i * dt for i in range(len(y_values))]
    fig, ax = plt.subplots()
    ax.plot(t, y_values, label=method, color="purple")
    ax.set_xlabel("Time")
    ax.set_ylabel("y(t)")
    ax.set_title(f"{method} Method Simulation")
    ax.grid(True)
    ax.legend()
    st.pyplot(fig)
