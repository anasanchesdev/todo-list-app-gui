import functions as f
import PySimpleGUI as ps

label = ps.Text('Type in a To-do:')
input_box = ps.InputText(tooltip='Enter a todo', key='add')
add_button = ps.Button('Add')

window = ps.Window('Todo List App', font=('Helvetica', 13), layout=[
    [label],
    [input_box, add_button]
])

todo_list = f.get_todos()

while True:
    events, values = window.read()

    if events == 'Add':
        new_todo = values['add'] + '\n'
        todo_list.append(new_todo)
        f.update_file(todo_list)

    elif ps.WIN_CLOSED:
        break

window.close()
