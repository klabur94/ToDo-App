import streamlit as st
import functions

# Holt die To-Do-Liste aus den Funktionen
todos = functions.get_todos()

# Funktion zum Hinzufügen eines neuen To-Dos
def add_todo():
    todo = st.session_state["new_todo"] + "\n"  # Holt das neue To-Do aus dem Eingabefeld und fügt einen Zeilenumbruch hinzu
    todos.append(todo)  # Fügt das neue To-Do zur Liste hinzu
    functions.write_todos(todos)  # Schreibt die aktualisierte To-Do-Liste in die Datei
    st.session_state["new_todo"] = ""  # Leert das Eingabefeld

# Setzt den Titel und die Unterüberschrift der App
st.title("My TODO App")
st.subheader("This is my todo APP")
st.write("This app increases your productivity")

# Erstellt Checkboxen für jedes To-Do mit einem eindeutigen Schlüssel
for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=f"todo_{index}")  # Erstellt eine Checkbox für jedes To-Do
    if checkbox:  # Überprüft, ob die Checkbox aktiviert wurde
        todos.pop(index)  # Entfernt das abgeschlossene To-Do aus der Liste
        functions.write_todos(todos)  # Schreibt die aktualisierte To-Do-Liste in die Datei
        st.experimental_rerun()  # Lädt die App neu, um die Änderungen anzuzeigen

# Eingabefeld für ein neues To-Do
st.text_input(label="", placeholder="Enter a todo",
              on_change=add_todo, key='new_todo')  # Erstellt ein Eingabefeld mit einem Placeholder und einem Schlüssel

