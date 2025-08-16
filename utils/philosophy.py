import streamlit as st
import os

def render_philosophy_tab():
    # 🔹 Load custom CSS if available
    css_path = "assets/overlays/philosophy.css"
    if os.path.exists(css_path):
        with open(css_path, "r") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

    # 🔹 Header
    st.markdown("## 🧠 The Philosophy Behind This App")
    st.write("""
    This simulator is more than math—it’s a symbolic mirror.  
    It helps us understand how change unfolds, how we predict the future, and how we reflect on uncertainty.
    """)

    st.markdown("### 🌞 Explicit vs 🌑 Implicit")

    # 🔹 Helper function for method cards
    def method_card(icon_url, label, description):
        col1, col2 = st.columns([1, 5])
        with col1:
            if icon_url:
                st.image(icon_url, width=40)
        with col2:
            st.markdown(f"**{label}**: {description}")

    # 🔹 Method overlays
    method_card("assets/icons/explicit.png", "Explicit", "Fast, intuitive—like guessing tomorrow’s weather from today’s sunshine.")
    method_card("assets/icons/implicit.png", "Implicit", "Stable, reflective—like moonlight revealing hidden truths.")
    method_card("assets/icons/crank_nicolson.png", "Crank-Nicolson", "A breath between inhale and exhale—balancing prediction and reflection.")
    method_card("assets/icons/imex.png", "IMEX", "Lightning that splits time—handling fast and slow parts separately.")

    # 🔹 Symbolic context
    st.markdown("### 🌀 Why Symbolism Matters")
    st.write("""
    Each method is wrapped in a lore card—a poetic overlay that turns equations into metaphors.  
    This helps learners connect emotionally and intuitively with the math.
    """)

    st.markdown("### 🎨 How It Works")
    st.write("""
    You choose a method, simulate its behavior, and explore its symbolic meaning.  
    Behind the scenes, Python and Streamlit do the math—but the front end tells a story.
    """)

    st.markdown("### 🧬 Who Is This For?")
    st.write("""
    - Curious learners  
    - Educators  
    - Philosophers  
    - Anyone who wonders how we model change
    """)

    st.markdown("### 🌌 Final Thought")
    st.write("""
    This app is a bridge—between intuition and rigor, sunlight and moonlight, breath and computation.  
    Welcome to a universe where math becomes myth.
    """)
