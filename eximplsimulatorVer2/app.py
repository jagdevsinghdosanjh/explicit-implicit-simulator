import streamlit as st
import os
import sys

from tabs.financial_forecasting import render_financial_tab
from tabs.stochastic_forecasting import render_stochastic_forecast_tab

# Add explimpmsimulatorVer2 to sys.path
base_dir = os.path.dirname(__file__)
sys.path.append(os.path.join(base_dir, "eximplsimulatorVer2"))


# Ensure local imports work
sys.path.append(os.path.dirname(__file__))

# Import tab renderers

# Optional: import other tabs if modularized
# from tabs.simulator import render_simulator_tab
# from tabs.philosophy import render_philosophy_tab
# from tabs.math_foundations import render_math_tab
# from tabs.reference_library import render_reference_tab

# Load custom CSS if available
css_path = os.path.join("assets", "overlays", "philosophy.css")
if os.path.exists(css_path):
    with open(css_path) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# App title and header
st.set_page_config(page_title="Explicit–Implicit Simulator", layout="wide")
st.title("🌗 Explicit–Implicit Simulator")

# Define tabs
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "🔬 Simulator", 
    "🧠 Philosophy", 
    "📐 Mathematical Foundations", 
    "📚 Reference Library",
    "📈 Financial Forecasting",
    "📊 Stochastic Forecasting"
])

# Render each tab
with tab1:
    st.subheader("🔬 Simulator")
    st.info("Run explicit and implicit simulations using your selected numerical method.")
    # render_simulator_tab()  # Uncomment if modularized

with tab2:
    st.subheader("🧠 Philosophy")
    st.markdown("Explore the philosophical foundations of numerical modeling and symbolic computation.")
    # render_philosophy_tab()  # Uncomment if modularized

with tab3:
    st.subheader("📐 Mathematical Foundations")
    st.markdown("Dive into the math behind stability, convergence, and error analysis.")
    # render_math_tab()  # Uncomment if modularized

with tab4:
    st.subheader("📚 Reference Library")
    st.markdown("Explore foundational texts and papers that deepen your understanding of numerical methods and symbolic mathematics.")
    st.markdown("- Numerical Methods for PDEs – LeVeque")
    st.markdown("- Stability Theory – Trefethen")
    st.markdown("- Euclid’s Elements – [Clark University](https://mathcs.clarku.edu/~djoyce/elements/)")

with tab5:
    render_financial_tab()

with tab6:
    render_stochastic_forecast_tab()
