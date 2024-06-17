# Functions
FILEPATH = "files/todos.txt"
def get_todos(filepath=FILEPATH):
    with open(filepath) as file:
        todos = file.readlines()
    return todos


def write_todos(todos_arg, filepath=FILEPATH):
    with open(filepath, 'w') as file:  # Open in write mode
        file.writelines(todos_arg)


#print(f"It is {datetime}")
