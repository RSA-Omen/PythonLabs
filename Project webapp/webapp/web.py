"""
# My first app
"""

import streamlit as st
import functions

todos = functions.get_todos()

st.title("My Todo App")
st.subheader("This is my todo app.")
st.write("This app is to help you track your todos.")

# Display existing todos
if todos:
    st.write("**Your current todos:**")
    for todo in todos:
        st.checkbox(todo)
else:
    st.write("No todos yet!")

# Add new todo
st.subheader("Add New Todo")
new_todo = st.text_input(label="Enter a todo", placeholder="Add a new todo...")
if st.button("Add Todo") and new_todo:
    todos.append(new_todo)
    functions.write_todos(todos)
    st.rerun()

