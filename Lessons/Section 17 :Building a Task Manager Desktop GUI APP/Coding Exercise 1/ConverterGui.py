from tkinter.constants import W
import FreeSimpleGUI as sg

label = sg.Text("Enter feet:")
input_box = sg.InputText(tooltip="Enter feet", key="feet")
btn_convert = sg.Button("Convert")
label2 = sg.Text("Enter inches:")
input_box2 = sg.InputText(tooltip="Enter inches", key="inches")
result_label = sg.Text("", key="result", size=(20, 1))

window = sg.Window('Converter', layout=[[label, input_box],
 [label2, input_box2],[sg.Text("Result:"), result_label, btn_convert]])


while True:
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED:
        break
    match event:
        case "Convert":
            try:
                feet = float(values["feet"])
                inches = float(values["inches"])
                feet_to_meters = feet * 0.3048
                inches_to_meters = inches * 0.0254  
                result = feet_to_meters + inches_to_meters
                window["result"].update(f"{result} m")
            except Exception as e:
                window["result"].update(f"Error: {e}")
        case _:
            pass

window.close()