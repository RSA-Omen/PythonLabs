from tkinter.constants import W
import FreeSimpleGUI as sg
from functions import get_todos, write_todos


#UI creation
label = sg.Text("Type in a todo:")
input_box = sg.InputText(tooltip="Enter todo", key="todo_input")
btn_add = sg.Button("Add")
btn_exit = sg.Button("Exit")
btn_edit = sg.Button("Edit")
list_box = sg.Listbox(values=[todo.strip('\n') for todo in get_todos()], key="todos", size=(45, 10),
                  enable_events=True)
delete_button = sg.Button("Delete")

window = sg.Window('Task Manager',
                   layout=[[label], [input_box, btn_add], [list_box, delete_button],[btn_edit,btn_exit]],
                   font=("Helvetica", 20))


#Event loop
while True:
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED:
        break
    match event:
        case "Add":
            try:
                item = values["todo_input"].strip()  # Get value from input box
                if item:  # Only add if something was entered
                    todos = get_todos()  # Get current todos
                    if not item.endswith('\n'):
                        item += '\n'
                    todos.append(item)  # Add new item to list
                    write_todos(todos)  # Write the entire list
                    window["todos"].update(values=[todo.strip('\n') for todo in todos])  # Update the listbox display
                    window["todo_input"].update("")  # Clear the input box
                    input_box.focus()
            except Exception as e:
                print(f"An error occurred while adding the item: {e}")
                continue
        case "Edit":
            try:
                todo_to_edit = values["todos"][0]
                new_todo = values["todo_input"].strip()
                if new_todo:  # Only edit if something was entered
                    todos = get_todos()
                    # Find the index by adding back the newline to match file format
                    index = todos.index(todo_to_edit + '\n')
                    # Replace with new todo (add newline)
                    todos[index] = new_todo + '\n'
                    write_todos(todos)
                    window["todos"].update(values=[todo.strip('\n') for todo in todos])  # Update the listbox display
                    window["todo_input"].update("")  # Clear the input box
            except Exception as e:
                print(f"An error occurred while editing the item: {e}")
                continue
        case sg.WIN_CLOSED|"Exit":
            window.close() 
            break
        case "Delete":
            try:
                todo_to_delete = values["todos"][0]
                todos = get_todos()
                # Need to add back the newline to match the file format
                todos.remove(todo_to_delete + '\n')
                write_todos(todos)
                window["todos"].update(values=[todo.strip('\n') for todo in todos])  # Update the listbox display
            except Exception as e:
                print(f"An error occurred while deleting the item: {e}")
                continue
        case "todos":
            window["todo_input"].update(values["todos"][0])
 
window.close()  

    