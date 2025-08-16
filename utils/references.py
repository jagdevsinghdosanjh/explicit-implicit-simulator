import streamlit as st

def render_reference_tab():
    st.markdown("## 📚 Reference Library")
    st.write("Explore foundational texts and papers that deepen your understanding of numerical methods and symbolic mathematics.")

    references = {
        #"Numerical Analysis by Burden & Faires:"https://mathcs.clarku.edu/~djoyce/numerical-analysis/",
        "Numerical Methods for Partial Differential Equations": "https://ocw.mit.edu/courses/18-336-numerical-methods-for-partial-differential-equations-spring-2009/",
        "Finite Difference Methods for ODEs and PDEs – LeVeque": "https://faculty.washington.edu/rjl/fdmbook/",
        "Numerical Methods for Engineers – Chapra & Canale": "https://www.academia.edu/42140879/Numerical_Methods_for_Engineers_7th_Edition",
        "Stability Theory – Trefethen Lecture Notes": "https://people.maths.ox.ac.uk/trefethen/lectures.html",
        "Symbolic Computation and Geometry – Springer": "https://link.springer.com/book/10.1007/978-3-030-20206-2",
        "Ancient Geometry and Philosophy – Euclid’s Elements": "https://mathcs.clarku.edu/~djoyce/elements/Euclid.html"
    }

    for title, link in references.items():
        st.markdown(f"- [{title}]({link})")
