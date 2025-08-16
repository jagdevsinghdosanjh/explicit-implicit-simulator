import streamlit as st
import os

def render_philosophy_tab():
    # Load custom CSS if available
    css_path = 'assets/overlays/philosophy.css'
    if os.path.exists(css_path):
        with open(css_path, 'r') as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

    st.markdown("## 🧠 The Philosophy Behind This App")
    st.write("""
This simulator is more than math—it’s a symbolic mirror. It helps us understand how change unfolds, how we predict the future, and how we reflect on uncertainty.
""")

    st.markdown("### 🌞 Explicit vs 🌑 Implicit")

    col1, col2 = st.columns([1, 5])
    with col1:
        st.image("https://upload.wikimedia.org/wikipedia/commons/3/3f/Sun_symbol.svg", width=40)
    with col2:
        st.markdown("**Explicit**: Fast, intuitive—like guessing tomorrow’s weather from today’s sunshine.")

    col1, col2 = st.columns([1, 5])
    with col1:
        st.image("https://upload.wikimedia.org/wikipedia/commons/3/3c/Moon_symbol.svg", width=40)
    with col2:
        st.markdown("**Implicit**: Stable, reflective—like moonlight revealing hidden truths.")

    col1, col2 = st.columns([1, 5])
    with col1:
        st.image("https://upload.wikimedia.org/wikipedia/commons/4/4f/Yin_yang.svg", width=40)
    with col2:
        st.markdown("**Crank-Nicolson**: A breath between inhale and exhale.")

    col1, col2 = st.columns([1, 5])
    with col1:
        st.image("https://upload.wikimedia.org/wikipedia/commons/6/6f/Lightning_bolt.svg", width=40)
    with col2:
        st.markdown("**IMEX**: Lightning that splits time—handling fast and slow parts separately.")

    st.markdown("### 🌀 Why Symbolism Matters")
    st.write("""
Each method is wrapped in a lore card—a poetic overlay that turns equations into metaphors. This helps learners connect emotionally and intuitively with the math.
""")

    st.markdown("### 🎨 How It Works")
    st.write("""
You choose a method, simulate its behavior, and explore its symbolic meaning. Behind the scenes, Python and Streamlit do the math—but the front end tells a story.
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

# def render_philosophy_tab():
#     css_path = 'assets/overlays/philosophy.css'
#     if os.path.exists(css_path):
#         with open(css_path, 'r') as f:
#             st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
#     else:
#         st.warning("Philosophy CSS file not found. Rendering without custom styles.")

#     st.markdown("""
#     <div class="philosophy-card">
#         <h2>🧠 The Philosophy Behind This App</h2>
#         <p>This simulator is more than math—it’s a symbolic mirror. It helps us understand how change unfolds, how we predict the future, and how we reflect on uncertainty.</p>

#         <h3>🌞 Explicit vs 🌑 Implicit</h3>
#         <ul>
#             <li><img src="https://upload.wikimedia.org/wikipedia/commons/3/3f/Sun_symbol.svg" alt="Sun" class="svg-icon"> <b>Explicit</b>: Fast, intuitive, like guessing tomorrow’s weather from today’s sunshine.</li>
#             <li><img src="https://upload.wikimedia.org/wikipedia/commons/3/3c/Moon_symbol.svg" alt="Moon" class="svg-icon"> <b>Implicit</b>: Stable, reflective, like moonlight revealing hidden truths.</li>
#             <li><img src="https://upload.wikimedia.org/wikipedia/commons/4/4f/Yin_yang.svg" alt="Yin Yang" class="svg-icon"> <b>Crank-Nicolson</b>: A breath between inhale and exhale.</li>
#             <li><img src="https://upload.wikimedia.org/wikipedia/commons/6/6f/Lightning_bolt.svg" alt="Lightning" class="svg-icon"> <b>IMEX</b>: Lightning that splits time—handling fast and slow parts separately.</li>
#         </ul>

#         <h3>🌀 Why Symbolism Matters</h3>
#         <p>Each method is wrapped in a lore card—a poetic overlay that turns equations into metaphors. This helps learners connect emotionally and intuitively with the math.</p>

#         <h3>🎨 How It Works</h3>
#         <p>You choose a method, simulate its behavior, and explore its symbolic meaning. Behind the scenes, Python and Streamlit do the math—but the front end tells a story.</p>

#         <h3>🧬 Who Is This For?</h3>
#         <ul>
#             <li>Curious learners</li>
#             <li>Educators</li>
#             <li>Philosophers</li>
#             <li>Anyone who wonders how we model change</li>
#         </ul>

#         <h3>🌌 Final Thought</h3>
#         <p>This app is a bridge—between intuition and rigor, sunlight and moonlight, breath and computation. Welcome to a universe where math becomes myth.</p>
#     </div>
#     """, unsafe_allow_html=True)

# import streamlit as st

# def render_philosophy_tab():
#     st.markdown('<style>' + open('assets/overlays/philosophy.css').read() + '</style>', unsafe_allow_html=True)

#     st.markdown("""
#     <div class="philosophy-card">
#         <h2>🧠 The Philosophy Behind This App</h2>
#         <p>This simulator is more than math—it’s a symbolic mirror. It helps us understand how change unfolds, how we predict the future, and how we reflect on uncertainty.</p>

#         <h3>🌞 Explicit vs 🌑 Implicit</h3>
#         <ul>
#             <li><img src="https://upload.wikimedia.org/wikipedia/commons/3/3f/Sun_symbol.svg" class="svg-icon"> <b>Explicit</b>: Fast, intuitive, like guessing tomorrow’s weather from today’s sunshine.</li>
#             <li><img src="https://upload.wikimedia.org/wikipedia/commons/3/3c/Moon_symbol.svg" class="svg-icon"> <b>Implicit</b>: Stable, reflective, like moonlight revealing hidden truths.</li>
#             <li><img src="https://upload.wikimedia.org/wikipedia/commons/4/4f/Yin_yang.svg" class="svg-icon"> <b>Crank-Nicolson</b>: A breath between inhale and exhale.</li>
#             <li><img src="https://upload.wikimedia.org/wikipedia/commons/6/6f/Lightning_bolt.svg" class="svg-icon"> <b>IMEX</b>: Lightning that splits time—handling fast and slow parts separately.</li>
#         </ul>

#         <h3>🌀 Why Symbolism Matters</h3>
#         <p>Each method is wrapped in a lore card—a poetic overlay that turns equations into metaphors. This helps learners connect emotionally and intuitively with the math.</p>

#         <h3>🎨 How It Works</h3>
#         <p>You choose a method, simulate its behavior, and explore its symbolic meaning. Behind the scenes, Python and Streamlit do the math—but the front end tells a story.</p>

#         <h3>🧬 Who Is This For?</h3>
#         <ul>
#             <li>Curious learners</li>
#             <li>Educators</li>
#             <li>Philosophers</li>
#             <li>Anyone who wonders how we model change</li>
#         </ul>

#         <h3>🌌 Final Thought</h3>
#         <p>This app is a bridge—between intuition and rigor, sunlight and moonlight, breath and computation. Welcome to a universe where math becomes myth.</p>
#     </div>
#     """, unsafe_allow_html=True)
