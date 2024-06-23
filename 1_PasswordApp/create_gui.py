# TO DO APP

from modules import functions  # Importiert benutzerdefinierte Funktionen aus dem Modul 'functions'
import PySimpleGUI as sg  # Importiert die PySimpleGUI-Bibliothek für die GUI
import os  # Importiert das OS-Modul für Betriebssystemoperationen

# Überprüft, ob die Datei 'todos.txt' existiert, und erstellt sie, falls nicht
if not os.path.exists("todos.txt"):
    with open("todos.txt", "w") as file:
        pass  # Erstellt eine leere Datei

# Setzt das Thema der GUI auf Schwarz
sg.theme("Black")

# Erstellt ein Text-Label
label = sg.Text("Type in a to do")

# Erstellt ein Eingabefeld für To-Dos mit einem Tooltip und einem Schlüssel "to do"
input_box = sg.InputText(tooltip="Enter Todo", key='todo')

# Erstellt Buttons für verschiedene Aktionen
add_button = sg.Button("Add")
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")

# Erstellt eine Listbox zur Anzeige der To-Dos
list_box = sg.Listbox(values=functions.get_todos(),  # Holt die aktuellen To-Dos
                      key='todos',  # Setzt den Schlüssel 'todos' für die Listbox
                      enable_events=True,  # Aktiviert Ereignisse bei Auswahländerungen
                      size=(45, 10))  # Setzt die Größe der Listbox

# Layout der GUI
layout = [
    [label],  # Zeile 1: Text-Label
    [input_box, add_button],  # Zeile 2: Eingabefeld und Hinzufügen-Button
    [list_box, edit_button, complete_button],  # Zeile 3: Listbox, Bearbeiten- und Abschluss-Button
    [exit_button]  # Zeile 4: Beenden-Button
]

# Erstellt das Fenster mit dem Titel 'My to-do App' und dem definierten Layout
window = sg.Window('My to-do App', layout=layout, font=('Helvetica', 20))

# Haupt-Ereignisschleife
while True:
    event, values = window.read()  # Liest Ereignisse und Werte aus dem Fenster

    if event == sg.WINDOW_CLOSED:  # Überprüft, ob das Fenster geschlossen wurde
        print("Program closed")  # Gibt eine Meldung auf der Konsole aus
        break  # Bricht die Schleife ab und schließt das Fenster

    print(event)  # Gibt das Ereignis auf der Konsole aus
    print(values)  # Gibt die aktuellen Werte der Eingabefelder auf der Konsole aus

    if event == 'Add':  # Überprüft, ob der Hinzufügen-Button gedrückt wurde
        todos = functions.get_todos()  # Holt die aktuellen To-Dos
        new_todo = values['todo'] + "\n"  # Holt das neue To-Do aus dem Eingabefeld und fügt einen Zeilenumbruch hinzu
        todos.append(new_todo)  # Fügt das neue To-Do zur Liste hinzu
        functions.write_todos(todos)  # Schreibt die aktualisierte To-Do-Liste in die Datei
        window['todos'].update(values=todos)  # Aktualisiert die Listbox mit den neuen To-Dos

    elif event == 'Edit':  # Überprüft, ob der Bearbeiten-Button gedrückt wurde
        if values['todos']:  # Überprüft, ob ein To-Do ausgewählt ist
            todo_to_edit = values['todos'][0]  # Holt das zu bearbeitende To-Do
            new_todo = values['todo']  # Holt das neue To-Do aus dem Eingabefeld
            todos = functions.get_todos()  # Holt die aktuellen To-Dos
            index = todos.index(todo_to_edit)  # Findet den Index des zu bearbeitenden To-Dos
            todos[index] = new_todo + "\n"  # Ersetzt das alte To-Do durch das neue
            functions.write_todos(todos)  # Schreibt die aktualisierte To-Do-Liste in die Datei
            window['todos'].update(values=todos)  # Aktualisiert die Listbox mit den neuen To-Dos
        else:
            sg.popup("Please select a todo to edit")  # Zeigt eine Popup-Meldung an, wenn kein To-Do ausgewählt ist

    elif event == "Complete":  # Überprüft, ob der Abschluss-Button gedrückt wurde
        if values['todos']:  # Überprüft, ob ein To-Do ausgewählt ist
            todo_to_complete = values['todos'][0]  # Holt das abzuschließende To-Do
            todos = functions.get_todos()  # Holt die aktuellen To-Dos
            todos.remove(todo_to_complete)  # Entfernt das abgeschlossene To-Do aus der Liste
            functions.write_todos(todos)  # Schreibt die aktualisierte To-Do-Liste in die Datei
            window['todos'].update(values=todos)  # Aktualisiert die Listbox mit den neuen To-Dos
            window['todo'].update(value='')  # Löscht das Eingabefeld
        else:
            sg.popup("Please select a todo to complete")  # Zeigt eine Popup-Meldung an, wenn kein To-Do ausgewählt ist

    elif event == "Exit":  # Überprüft, ob der Beenden-Button gedrückt wurde
        print("Program closed")  # Gibt eine Meldung auf der Konsole aus
        break  # Bricht die Schleife ab und schließt das Fenster

    elif event == 'todos':  # Überprüft, ob ein To-Do in der Listbox ausgewählt wurde
        if values['todos']:  # Überprüft, ob ein To-Do ausgewählt ist
            window['todo'].update(value=values['todos'][0])  # Aktualisiert das Eingabefeld mit dem ausgewählten To-Do

window.close()  # Schließt das Fenster, wenn die Schleife beendet wird