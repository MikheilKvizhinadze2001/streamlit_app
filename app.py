import streamlit as st
from menu import menu


st.title("Welcome to the main app page!", anchor="top")
# Initialize st.session_state.role to None
if "role" not in st.session_state:
    st.session_state.role = None

# Retrieve the role from Session State to initialize the widget
st.session_state._role = st.session_state.role

def set_role():
    # Assign the value of `_role` to the `role` attribute in the `session_state` object
    st.session_state.role = st.session_state._role


# Render the dynamic menu
def menu():
    if st.session_state.role:
        st.write(f"Welcome, {st.session_state.role}!")
    else:
        st.write("Please select your role.")


# Selectbox to choose role
st.selectbox(
    "Select your role:",
    [None, "user", "admin", "super-admin"],
    key="_role",
    on_change=set_role,
)

# Add a link to fragments.py
container = st.container(border=True)
container.write("""
                 This container has the link to the fragments page. 
                 Click the link to navigate to the fragments page, which contains 
                 demo to show the use of fragments in Streamlit.
                 """)
container.page_link("pages/fragments.py", label="Go to fragments")
menu()
