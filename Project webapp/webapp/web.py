import streamlit as st

st.title("My Todo App")

# Initialize session state for todos
if 'todos' not in st.session_state:
    st.session_state.todos = []

# Add new todo
st.subheader("Add New Todo")
new_todo = st.text_input("Enter a new todo:")
if st.button("Add Todo") and new_todo:
    st.session_state.todos.append(new_todo)
    st.rerun()

# Display todos
st.subheader("Your Todos")
if st.session_state.todos:
    for i, todo in enumerate(st.session_state.todos):
        col1, col2 = st.columns([4, 1])
        with col1:
            st.write(f"• {todo}")
        with col2:
            if st.button("Delete", key=f"delete_{i}"):
                st.session_state.todos.pop(i)
                st.rerun()
else:
    st.write("No todos yet. Add one above!")

# Clear all todos
if st.button("Clear All Todos"):
    st.session_state.todos = []
    st.rerun()

