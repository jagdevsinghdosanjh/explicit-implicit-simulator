import streamlit as st
import numpy as np
from methods import explicit, implicit, crank_nicolson, imex
from utils.plotter import plot_solutions
from utils.lore_cards import LORE

st.set_page_config(page_title="Explicit–Implicit Simulator", layout="wide")
st.title("🌗 Explicit–Implicit Simulator")

method = st.selectbox("Choose a method", ["Explicit", "Implicit", "Crank-Nicolson", "IMEX"])
dt = st.slider("Time step Δt", 0.01, 0.5, 0.1)
y0 = st.number_input("Initial value y₀", value=1.0)
steps = st.slider("Number of steps", 10, 100, 50)

# Solver dispatch
solver_map = {
    "Explicit": explicit.forward_euler_step,
    "Implicit": implicit.backward_euler_step,
    "Crank-Nicolson": crank_nicolson.crank_nicolson_step,
    "IMEX": imex.imex_step
}

y_values = [y0]
for _ in range(steps):
    y_next = solver_map[method](y_values[-1], dt)
    y_values.append(y_next)

plot_solutions(y_values, dt, method)
st.markdown(f"### Lore Card: {method}")
st.info(LORE[method.lower()])

# Replace list with numpy array for better performance and future ops
y_values = np.zeros(steps + 1)
y_values[0] = y0

for i in range(steps):
    y_values[i + 1] = solver_map[method](y_values[i], dt)

plot_solutions(y_values.tolist(), dt, method)