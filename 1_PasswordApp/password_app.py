
from modules.functions import get_todos, write_todos
from datetime import datetime

print(f"It´s the {datetime.now().strftime("date: %Y-%m-%d, time: %H:%M:%S")}") # shows the current date

# If Statements
while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()  # Leerzeichen bereinigen
    # --------------------------------------------------------------------------------
    if user_action.startswith("add"): # Fall 1
        todo = user_action[4:]

        todos = get_todos()

        todos.append(todo + '\n')

        write_todos(todos)
    # ----------------------------------------------------------------------------
    elif user_action.startswith('show'):

        todos = get_todos()

        new_todos = [item.strip('\n') for item in todos]  # list comprehansion

        for index, item in enumerate(new_todos):
            print(f"{index + 1}-{item}")
    # ----------------------------------------------------------------------------
    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            number = number - 1

            todos = get_todos()

            new = input("Enter new todo: ")  # neuer Input
            todos[number] = new + '\n'

            write_todos(todos)

        except ValueError:
            print("Your command is not valid")
            # user_action = input("Type add, show, edit, complete or exit: ")
            continue # runs the loop (input-Query) again
    # ----------------------------------------------------------------------------
    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])

            todos = get_todos()

            index = number - 1
            todo_to_remove = todos[index]
            todos.pop(index)  # entfernt den Inhalt am Index "number"

            write_todos(todos)

            message = f"Todo {todo_to_remove.strip()} was removed from the list"
            print(message)

        except IndexError:
            print("There is no item with that number")
            continue
    # ----------------------------------------------------------------------------
    elif user_action.startswith('exit'):
        break  # stoppt die While Schleife
    # ----------------------------------------------------------------------------
    else:
        print("Hey, unknown command!")
    # ----------------------------------------------------------------------------
print("bye")
