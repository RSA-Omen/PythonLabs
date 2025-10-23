"""
# My first app
"""

import streamlit as st
import functions

todos = functions.get_todos()

st.title("My Todo App")
st.subheader("This is my todo app.")
st.write("This app is to help you track your todos.")

for todo in todos:
    st.checkbox(todo)

st.text_input(label="Enter a todo", placeholder="Add a new todo...")

