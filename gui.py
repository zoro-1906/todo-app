import functions
import FreeSimpleGUI as sg
import time

sg.theme("DarkPurple4")
# Search FreeSimpleGUI themes in google to change the theme
clock = sg.Text("", key="clock")
label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter a todo", key="todo")
button = sg.Button("Add")
list_box = sg.LBox(values=functions.get_todos(), key='todos', enable_events=True,
                   size=[40, 10])
edit_button= sg.Button("Edit")
complete_button= sg.Button("Complete")
exit_button = sg.Button("Exit")

window = sg.Window('My To-Do App',
                       layout=[[clock],
                               [label],
                               [input_box, button],
                               [list_box, edit_button, complete_button],
                               [exit_button]],
                       font=('Helvetica', 14))
while True:
    event, values= window.read(timeout=200)
    window["clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    print(1,event)
    print(2, values)
    print(3, values['todos'])
    match event:
        case "Add":
            todos = functions.get_todos()
            if values['todo'] == "":
                sg.popup("Please type a todo before clicking Add.",
                         font=("Helvetica", 10))
                window['todo'].update(value='')
            else:
                new_todo = values['todo'] + "\n"
                todos.append(new_todo)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
        case "Edit":
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo']

                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                sg.popup("Please select an item to be Edited", font=('Helvetica', 14))
        case "Complete":
            try:
                todo_to_complete = values['todos'][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value="")
            except IndexError:
                sg.popup("Please select an item to be Completed", font=('Helvetica', 14))
        case "Exit":
            break
        case 'todos':
            window['todo'].update(value=values['todos'][0])
        case sg.WINDOW_CLOSED:
            break
window.close()