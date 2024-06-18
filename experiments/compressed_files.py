
# Compress files to zip files with a GUI

import FreeSimpleGUI as sg

# 1. File
label1 = sg.Text("Select files to compress:")
# Input Button
input1 = sg.Input()
# Button to select files
choose_button1 = sg.FilesBrowse("Choose", key="files")

# 2. Destination ZIP
label2 = sg.Text("Select destination folder:")
# Input Button
input2 = sg.Input()
# Button to select files
choose_button2 = sg.FolderBrowse("Choose", key="folder")

# 3. Compressed Button
compress_button = sg.Button("Compress")

# Aufbau Window
window = sg.Window("File Compressor",
                   layout=[[label1, input1, choose_button1],
                           [label2, input2, choose_button2],
                           [compress_button]])

# Loop
while True:
    event, values = window.read() # zeigt das Window an
    print(event, values)
    filepaths = values["Choose"].split(";")
    folder = values["Choose0"]

window.close()
