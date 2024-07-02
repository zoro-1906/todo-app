#from functions import get_todos, write_todos
import functions
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is ", now)
while True:
    user_action = input("Type  add, show, edit, complete or exit : ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:] + '\n'

        todos = functions.get_todos()

        todos.append(todo)

        functions.write_todos(todos)

    elif user_action.startswith("show"):

        todos = functions.get_todos()

        # new_todos = [item.strip('\n') for item in todos] "This is an alternative to strip the \n in item"

        for index, items in enumerate(todos):
            items = items.strip('\n')
            index = index + 1
            row = f"{index}-{items}"
            print(row)
    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            number = number - 1

            todos = functions.get_todos()

            new_task = input("Enter a new task: ")
            todos[number] = new_task + '\n'
            print("Task replaced to: ", new_task)

            functions.write_todos(todos)
        except ValueError:
            print("You typed an invalid command")
            continue
    elif user_action.startswith("complete"):
        try:
            remove = int(user_action[9:])
            removed = remove - 1

            todos = functions.get_todos()
            todos.pop(removed)
            print(remove, "is removed form the todos list")

            functions.write_todos(todos)
        except IndexError:
            print("There is no item with that index in the list")
            continue
    elif user_action.startswith("exit"):
        break
    else:
        print("You typed an invalid command.")
print("Exited")