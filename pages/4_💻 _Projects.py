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

st.title("📂 Projects")

projects = [
    {"title": "E-Attendance Navigator", "desc": "Attendance system with reports."},
    {"title": "Hair studio", "desc": "A website for online booking for an haircut."},
    {"title": "Banking System", "desc": " Handles transactions and analytics."},
]

for i, project in enumerate(projects):
    with st.container():
        st.subheader(project["title"])
        st.write(project["desc"])

        col1, col2 = st.columns(2)

        with col1:
            if st.button("🔍 View Details", key=f"view{i}"):
                st.info("Details coming soon")

        with col2:
            if st.button("❤️ Like", key=f"like{i}"):
                st.success("Liked!")

        st.markdown("---")

st.subheader("➕ Add New Project")

with st.form("add_project_form"):
    name = st.text_input("Project Name")
    desc = st.text_area("Project Description")
    category = st.selectbox("Category", ["System", "Web", "Design"])
    status = st.selectbox("Status", ["Completed", "In Progress"])

    submit = st.form_submit_button("Add Project")

    if submit:
        if name and desc:
            st.success(f"✅ Project '{name}' added successfully!")
        else:
            st.error("⚠ Please complete all fields.")