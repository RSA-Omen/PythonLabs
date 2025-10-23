import streamlit as st

st.title("My Todo App")

# Initialize session state for todos
if 'todos' not in st.session_state:
    st.session_state.todos = []



