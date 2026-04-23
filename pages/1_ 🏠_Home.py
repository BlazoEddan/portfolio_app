import streamlit as st
import os

import streamlit as st

st.markdown(
    """
    <style>
    .stApp {
        background-color: #7DAACB;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("🏠 Home")

img_path = "eddan.jpg" 


col1, col2, col3 = st.columns([1,2,1])

with col2:
    if os.path.exists(img_path):
        st.image(img_path, width=300)
    else:
        st.warning("Image not found.")

st.header("🙋Hi, I'm Eddan G. Blazo")
st.write("💻Aspiring Developer | 🧑‍💻Designer | 👓Tech Enthusiast | 🎨 UI/UX ")

st.info("Welcome to my portfolio! Explore my work and skills.")