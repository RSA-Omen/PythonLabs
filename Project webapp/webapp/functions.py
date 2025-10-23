import os

def get_todos(filepath="todos.txt"):
    """ Read a text file and return the list of to-do items."""
    try:
        with open(filepath, "r") as file:
            todos = file.readlines()
        # Strip newlines and filter out empty lines
        todos = [todo.strip() for todo in todos if todo.strip()]
        return todos
    except FileNotFoundError:
        print("The todo file does not exist. Please add an item first.")
        return []    

def write_todos(todos_arg, filepath="todos.txt"):
    """ Write the to-do items list in the text file."""
    with open(filepath, "w") as file:
        for todo in todos_arg:
            file.write(todo + "\n")