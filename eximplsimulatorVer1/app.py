import streamlit as st
import numpy as np
from methods import explicit, implicit, crank_nicolson, imex
from utils.plotter import plot_solutions
from utils.lore_cards import LORE
from utils.philosophy import render_philosophy_tab
from utils.math import render_math_tab
from utils.references import render_reference_tab  # NEW

# Inject symbolic CSS overlays
st.markdown('<style>' + open('assets/overlays/philosophy.css').read() + '</style>', unsafe_allow_html=True)

# Page setup
st.set_page_config(page_title="Explicit–Implicit Simulator", layout="wide")
st.title("🌗 Explicit–Implicit Simulator")

# Tabs
tab1, tab2, tab3, tab4 = st.tabs([
    "🔬 Simulator", 
    "🧠 Philosophy", 
    "📐 Mathematical Foundations", 
    "📚 Reference Library"
])

# 🔬 Simulator Tab
with tab1:
    method = st.selectbox("Choose a method", ["Explicit", "Implicit", "Crank-Nicolson", "IMEX"])
    dt = st.slider("Time step Δt", 0.01, 0.5, 0.1)
    y0 = st.number_input("Initial value y₀", value=1.0)
    steps = st.slider("Number of steps", 10, 100, 50)

    solver_map = {
        "Explicit": explicit.forward_euler_step,
        "Implicit": implicit.backward_euler_step,
        "Crank-Nicolson": crank_nicolson.crank_nicolson_step,
        "IMEX": imex.imex_step
    }

    y_values = np.zeros(steps + 1)
    y_values[0] = y0
    for i in range(steps):
        y_values[i + 1] = solver_map[method](y_values[i], dt)

    plot_solutions(y_values.tolist(), dt, method)

    st.markdown(f"### Lore Card: {method}")
    st.info(LORE[method.lower()])

# 🧠 Philosophy Tab
with tab2:
    render_philosophy_tab()

# 📐 Mathematical Foundations Tab
with tab3:
    render_math_tab()

# 📚 Reference Library Tab
with tab4:
    render_reference_tab()
