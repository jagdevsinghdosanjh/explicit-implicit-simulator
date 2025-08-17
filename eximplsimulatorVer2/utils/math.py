import streamlit as st

def render_math_tab():
    st.markdown("## 📐 Mathematical Foundations")

    st.markdown("### 🔥 Explicit Method (Forward Euler)")
    st.latex(r"y_{n+1} = y_n + \Delta t \cdot f(y_n, t_n)")
    st.write("""
    - First-order accurate.
    - Simple and fast.
    - Conditionally stable (small Δt required).
    """)

    st.markdown("### 🌊 Implicit Method (Backward Euler)")
    st.latex(r"y_{n+1} = y_n + \Delta t \cdot f(y_{n+1}, t_{n+1})")
    st.write("""
    - Requires solving for future value.
    - Unconditionally stable for linear systems.
    - Suitable for stiff equations.
    """)

    st.markdown("### 🌗 Crank-Nicolson Method")
    st.latex(r"y_{n+1} = y_n + \frac{\Delta t}{2} \left[ f(y_n, t_n) + f(y_{n+1}, t_{n+1}) \right]")
    st.write("""
    - Second-order accurate.
    - Combines explicit and implicit evaluations.
    - May oscillate for stiff problems.
    """)

    st.markdown("### ⚡ IMEX Method (Implicit–Explicit)")
    st.latex(r"y_{n+1} = y_n + \Delta t \cdot \left[ f_{\text{explicit}}(y_n) + f_{\text{implicit}}(y_{n+1}) \right]")
    st.write("""
    - Splits dynamics into fast (implicit) and slow (explicit) parts.
    - Ideal for multi-scale systems.
    - Balances stability and efficiency.
    """)

    st.markdown("### 📊 Stability Summary")
    st.write("""
    - **Explicit**: Fast but unstable for stiff problems.
    - **Implicit**: Stable but computationally heavier.
    - **Crank-Nicolson**: Balanced but may oscillate.
    - **IMEX**: Flexible hybrid for complex systems.
    """)

# import streamlit as st

# def render_math_tab():
#     st.markdown("## 📐 Mathematical Foundations")

#     st.markdown("### 🔥 Explicit Method (Forward Euler)")
#     st.latex(r"y_{n+1} = y_n + \Delta t \cdot f(y_n, t_n)")
#     st.write("""
#     - Uses current value to estimate the next.
#     - First-order accurate.
#     - Simple but conditionally stable.
#     """)

#     st.markdown("### 🌊 Implicit Method (Backward Euler)")
#     st.latex(r"y_{n+1} = y_n + \Delta t \cdot f(y_{n+1}, t_{n+1})")
#     st.write("""
#     - Solves for future value using itself.
#     - Requires root-finding or matrix inversion.
#     - Unconditionally stable for linear problems.
#     """)

#     st.markdown("### 🌗 Crank-Nicolson Method")
#     st.latex(r"y_{n+1} = y_n + \frac{\Delta t}{2} \left[ f(y_n, t_n) + f(y_{n+1}, t_{n+1}) \right]")
#     st.write("""
#     - Averages explicit and implicit evaluations.
#     - Second-order accurate.
#     - Good balance of stability and accuracy.
#     """)

#     st.markdown("### ⚡ IMEX Method (Implicit–Explicit)")
#     st.latex(r"y_{n+1} = y_n + \Delta t \cdot \left[ f_{\text{explicit}}(y_n) + f_{\text{implicit}}(y_{n+1}) \right]")
#     st.write("""
#     - Splits the equation into fast and slow components.
#     - Treats stiff terms implicitly, others explicitly.
#     - Ideal for multi-scale systems.
#     """)

#     st.markdown("### 📊 Stability Insight")
#     st.write("""
#     - Explicit methods require small time steps for stability.
#     - Implicit methods allow larger steps but are computationally heavier.
#     - Crank-Nicolson is stable but may oscillate for stiff problems.
#     - IMEX offers flexibility by combining both worlds.
#     """)
