import streamlit as st

# Page config
st.set_page_config(page_title="Login Page", page_icon="🔐", layout="centered")

# Title
st.title("🔐 Login Page")

# Initialize session state
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# Dummy credentials (for demo)
USER_EMAIL = "admin@example.com"
USER_PASSWORD = "password123"

# Login form
if not st.session_state.logged_in:
    with st.form("login_form"):
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")
        submit = st.form_submit_button("Login")

        if submit:
            if not email or not password:
                st.error("Please fill in all fields")
            elif email == USER_EMAIL and password == USER_PASSWORD:
                st.session_state.logged_in = True
                st.success("Login successful!")
                st.rerun()
            else:
                st.error("Invalid email or password")

# After login
if st.session_state.logged_in:
    st.success("Welcome! You are logged in 🎉")

    if st.button("Logout"):
        st.session_state.logged_in = False
        st.rerun()
