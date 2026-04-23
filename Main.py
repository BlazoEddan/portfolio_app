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

st.set_page_config(page_title="My Portfolio", page_icon="💻")
st.title(" Welcome to My Portfolio")
st.write("""Navigate through my portfolio using the sidebar
Sections included:
- Home
- About Me
- Skills
- Projects
- Contact
""")
st.success("Simple Portfolio Multipage App using Streamlit ")