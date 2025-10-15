import FreeSimpleGUI as sg


label = sg.Text("Selecvt files to compress:")
input1 = sg.Input()
choose_button = sg.FilesBrowse("Choose", key="files")
label2 = sg.Text("Select destination folder:")
input2 = sg.Input()
choose_button2 = sg.FolderBrowse("Choose", key="folder")
compress_button = sg.Button("Compress")

window = sg.Window('files compressor', layout=[[label, input1, choose_button], [label2, input2, choose_button2], [compress_button]])
window.read()
window.close()  

    