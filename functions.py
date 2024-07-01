def get_todos():
    with open('txtfiles/todos.txt', 'r') as file:
        todos_local = file.readlines()
        return todos_local


def write_todos(todos_arg):
    with open('txtfiles/todos.txt', 'w') as file:
        todos = file.writelines(todos_arg)
