
#TODO: Erstelle eine GUI für deine TO-DO APP

from modules import functions
import FreeSimpleGUI as sg

label = sg.Text("Type in a to do")

input_box = sg.InputText(tooltip="Enter Todo")

add_button = sg.Button("Add")

window = sg.Window('My to-do App', layout=[[label], [input_box, add_button]])
window.read()
window.close()


