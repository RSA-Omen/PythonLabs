def get_todos(filepath="/home/lauchlan/thelab/todos.txt"):
    """ Read a text file and return the list of to-do items."""
    try:
        with open(filepath, "r") as file:
            todos = file.readlines()
        return todos
    except FileNotFoundError:
        print("The todo file does not exist. Please add an item first.")
        return []    

def write_todos(todos_arg, filepath="/home/lauchlan/thelab/todos.txt"):
    """ Write the to-do items list in the text file."""
    with open(filepath, "w") as file:
        file.writelines(todos_arg)