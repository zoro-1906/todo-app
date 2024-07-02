import functions
import FreeSimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter a todo")
button = sg.Button("Add")

window = sg.Window('My To-Do App', layout=[[label],[input_box, button]])
window.read()
window.close()