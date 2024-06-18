# Erstelle eine GUI für deine TO-DO APP

from modules import functions
import FreeSimpleGUI as sg

# Überschrift
label = sg.Text("Type in a to do")

# User Input Box
input_box = sg.InputText(tooltip="Enter Todo", key='todo')  # Füge den Schlüssel 'to do' hinzu

# Button
add_button = sg.Button("Add")

# Anzeigefläche
window = sg.Window('My to-do App',
                   layout=[[label], [input_box, add_button]],
                   font=('Helvetica', 20))
# Loop
while True:
    # Ausgabe Fenster
    event, values = window.read()

    if event == sg.WINDOW_CLOSED:
        print("Program closed")
        break

    print(event)
    print(values)

    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)

window.close()
