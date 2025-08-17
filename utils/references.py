import streamlit as st
from streamlit.components.v1 import html 

def render_reference_tab():
    st.markdown("## 📚 Reference Library")
    st.write("Explore foundational texts and papers that deepen your understanding of numerical methods and symbolic mathematics.")

    references = {
        "Numerical Methods for Partial Differential Equations": "https://ocw.mit.edu/courses/18-336-numerical-methods-for-partial-differential-equations-spring-2009/",
        "Finite Difference Methods for ODEs and PDEs – LeVeque": "https://faculty.washington.edu/rjl/fdmbook/",
        "Numerical Methods for Engineers – Chapra & Canale": "https://drive.google.com/file/d/1h0TOgQN1b5EcnHyENeZiWUgfq4cSiOtM/view",
        "Stability Theory – Trefethen Lecture Notes": "https://www.maths.ox.ac.uk/events/public-lectures-events",
        "Symbolic Computation and Geometry – Springer": "https://link.springer.com/book/10.1007/978-3-030-20206-2",
        "Ancient Geometry and Philosophy – Euclid’s Elements": "https://mathcs.clarku.edu/~djoyce/elements/Euclid.html"
    }

    for title, link in references.items():
        st.markdown(f"- [{title}]({link})")

    # ✅ Move this inside the function
    st.markdown("### 🔗 Share This App")
    html("""
    <div style="display: flex; gap: 10px; margin-top: 10px;">
      <a href="https://twitter.com/intent/tweet?text=Explore+numerical+methods+with+this+Explicit-Implicit+Simulator!&url=https://explicit-implicit-simulator-byjsd.streamlit.app/" target="_blank">
        <img src="https://img.icons8.com/color/48/000000/twitter--v1.png" alt="Twitter"/>
      </a>
      <a href="https://www.facebook.com/sharer/sharer.php?u=https://explicit-implicit-simulator-byjsd.streamlit.app/" target="_blank">
        <img src="https://img.icons8.com/color/48/000000/facebook-new.png" alt="Facebook"/>
      </a>
      <a href="https://www.linkedin.com/sharing/share-offsite/?url=https://explicit-implicit-simulator-byjsd.streamlit.app/" target="_blank">
        <img src="https://img.icons8.com/color/48/000000/linkedin.png" alt="LinkedIn"/>
      </a>
    </div>
    """, height=60)
