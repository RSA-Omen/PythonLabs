import FreeSimpleGUI as sg


label = sg.Text("Type in a todo:")
input_box = sg.InputText(tooltip="Enter todo")
add_button = sg.Button("Add")


window = sg.Window('Task Manager',
                   layout=[[label, input_box, add_button]],font=("Helvetica", 20))
window.read()
window.close()  

    