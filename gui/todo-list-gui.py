from functions import update_file, index_from_todo, get_time
import PySimpleGUI as ps

label = ps.Text('Type in a To-do:')
input_box = ps.InputText(tooltip='Enter a todo')
add_button = ps.Button('Add')

window = ps.Window('Todo List App', layout=[[label], [input_box, add_button]])
window.read()
window.close()
