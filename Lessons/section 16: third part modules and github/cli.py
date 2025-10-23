import FreeSimpleGUI as sg
from zipcreator import make_archive

label = sg.Text("Select files to compress:")
input1 = sg.Input()
choose_button = sg.FilesBrowse("Choose", key="files")
label2 = sg.Text("Select destination folder:")
input2 = sg.Input()
choose_button2 = sg.FolderBrowse("Choose", key="folder")
compress_button = sg.Button("Compress")

window = sg.Window('files compressor', layout=[[label, input1, choose_button], [label2, input2, choose_button2], [compress_button]])

while True:
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED:
        break
    match event:
        case "Compress":
            files = values["files"].split(";") if values["files"] else []
            folder = values["folder"]
            if not files or not folder:
                sg.popup("Please choose files and a destination folder.")
                continue
            make_archive(files, folder)
            sg.popup("Archive created!", title="Done")
        case _:
            pass

window.close()  

    