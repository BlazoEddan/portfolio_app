import streamlit as st
import os

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

st.title("🧑‍💻 About Me")

img_path = "dan.jpg"

col1, col2, col3 = st.columns([1,2,1])

with col2:
    if os.path.exists(img_path):
        st.image(img_path, width=200)
    else:
        st.warning("Image not found.")

st.markdown("""
    ## 👋 Hello, I'm Eddan G. Blazo
    🎓 3rd Year Computer Science Student  
    🏫 DEBESMSCAT  
    💻 Aspiring Developer | 🎨 UI/UX Designer | 🤖 Tech Enthusiast  
    """)


st.write("""
I am a third-year Computer Science student passionate about learning
 and exploring tech. I enjoy anime, movies, and traveling 
 and I’ve almost visited every municipality of Masbate.""")

st.subheader("📙Education")
st.write("🏫Jose Zurbito Sr. Elementary School")
st.write("🏫Masbate National Comprehensive High Schoo")
st.write("🏫 Dr. Emilio B. Espinosa, Sr. Memorial State College of Agriculture and technology (DEBESMSCAT)")
st.write("🧑‍💻 BS Computer Science")
st.write("🧑‍🏫 Trainings in Web Development & Design")
st.subheader(" 🎯 Goals 🎯")
st.write("👌 Become a Full Stack Developer")
st.write("👌 Build impactful tech solutions")