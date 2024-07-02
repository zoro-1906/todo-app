import functions
import FreeSimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter a todo", key="todo")
button = sg.Button("Add")

window = sg.Window('My To-Do App',
                       layout=[[label],[input_box, button]],
                       font=('Helvetica', 16))
while True:
    event, values= window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)

        case sg.WINDOW_CLOSED:
            break
window.close()