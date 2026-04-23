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

st.title("📞 Contact Me")


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

st.markdown("""
### 💬 Let's Connect
If you have any questions, project ideas, or collaboration offers,
feel free to reach out.
""")


st.markdown(
    """
    <style>
    .card {
        padding: 20px;
        border-radius: 15px;
        background-color: #0e1117;
        border: 1px solid #262730;
    }
    </style>
    """,
    unsafe_allow_html=True
)

col1, col2 = st.columns(2)


with col1:
    st.markdown("## 💬 Send a Message")

    with st.form("contact_form"):
        name = st.text_input("Your Name")
        email = st.text_input("Your Email")
        message = st.text_area("Your Message")

        submit = st.form_submit_button("🤳 Send Message")

        if submit:
            if name and email and message:
                st.success("✅ Message sent successfully!")
                st.balloons()
            else:
                st.error("⚠ Please complete all fields.")

# ================= CONTACT INFO =================
with col2:
    st.markdown("## ☎️ Contact Info")

    st.info("""
📍 Location: Philippines  
📧 Email: blazoeddan@gmail.com  
📱 Phone: +639302849866
""")

    st.markdown("###  Social Links")

    st.link_button("🤖 GitHub", "https://github.com/BlazoEddan")
    st.link_button("💻 Facebook", "https://www.facebook.com/eddan.blazo.5")
    st.link_button("💬 Email Me", "blazoeddan@gmail.com")

st.markdown("---")


st.markdown(
    """
    <div style="text-align:center; color:gray;">
        ⚙️ Built with Streamlit | © 2026 Eddan Blazo Portfolio
    </div>
    """,
    unsafe_allow_html=True
)