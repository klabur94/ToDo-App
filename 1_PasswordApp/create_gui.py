from modules import functions
import FreeSimpleGUI as sg  # Library for GUI

# Überschrift
label = sg.Text("Type in a to do")

# User Input Box
input_box = sg.InputText(tooltip="Enter Todo", key='todo')  # Füge den Schlüssel 'todo' hinzu

# Button
add_button = sg.Button("Add")
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")

# List Box mit den Todos
list_box = sg.Listbox(values=functions.get_todos(),
                      key='todos',
                      enable_events=True,
                      size=(45, 10))

# Anzeigefläche
layout = [
    [label],
    [input_box, add_button],
    [list_box, edit_button, complete_button],
    [exit_button]
]

window = sg.Window('My to-do App', layout=layout, font=('Helvetica', 20))

# Loop
while True:
    # Ausgabe Fenster
    event, values = window.read()

    if event == sg.WINDOW_CLOSED:
        print("Program closed")
        break

    print(event)
    print(values)

    if event == 'Add':
        todos = functions.get_todos()
        new_todo = values['todo'] + "\n"
        todos.append(new_todo)
        functions.write_todos(todos)
        window['todos'].update(values=todos)

    elif event == 'Edit':
        if values['todos']:
            todo_to_edit = values['todos'][0]
            new_todo = values['todo']

            todos = functions.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo + "\n"
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        else:
            sg.popup("Please select a todo to edit")

    elif event == "Complete":
        todo_to_complete = values['todos'][0]
        todos = functions.get_todos()
        todos.remove(todo_to_complete)
        functions.write_todos(todos)
        window['todos'].update(values=todos)
        window['todo'].update(value='')


    elif event == "Exit":
        print("Program closed")
        break

    elif event == 'todos':
        if values['todos']:
            window['todo'].update(value=values['todos'][0])


window.close()
