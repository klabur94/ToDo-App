import streamlit as st
import functions

# Holt die To-Do-Liste aus den Funktionen
todos = functions.get_todos()

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)

# Setzt den Titel und die Unterüberschrift der App
st.title("My TODO App")
st.subheader("This is my todo APP")
st.write("This app increases your productivity")

# Erstellt Checkboxen für jedes To-Do mit einem eindeutigen Schlüssel
for index, todo in enumerate(todos):
    st.checkbox(todo, key=f"todo_{index}")

# Eingabefeld für ein neues To-Do
new_todo = st.text_input(label="",placeholder="Enter a todo",
                         on_change=add_todo, key='new_todo')
st.session_state

# Optional: Fügen Sie Code hinzu, um das neue To-Do zur Liste hinzuzufügen und die Liste zu aktualisieren
if new_todo:
    todos.append(new_todo + "\n")
    functions.write_todos(todos)  # Aktualisiert die To-Do-Liste in der Datei
