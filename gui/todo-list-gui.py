import functions as f
import PySimpleGUI as ps

todo_list = f.get_todos()
label = ps.Text('Type in a To-do:')
input_box = ps.InputText(tooltip='Enter a todo', key='add')
add_button = ps.Button('Add')
edit_button = ps.Button('Edit')
list_box = ps.Listbox(values=todo_list, key='todos_list', enable_events=True, size=(40, 10))

window = ps.Window('Todo List App', font=('Helvetica', 13), layout=[
    [label],
    [input_box, add_button],
    [list_box, edit_button]
])


while True:
    events, values = window.read()
    print(f'EVENT: {events}\nVALUES: {values}')

    if events == 'Add':
        new_todo = values['add']
        todo_list.append(new_todo + '\n')
        f.update_file(todo_list)

        #  atualiza a lista inteira
        window['todos_list'].update(values=todo_list)

    elif events == 'todos_list':
        window['add'].update(value=values['todos_list'][0])

    elif events == 'Edit':
        to_edit = values['todos_list'][0]

        #  índice do to-do a ser editado na lista de todos
        todo_index = todo_list.index(to_edit)
        new_todo = values['add']
        todo_list[todo_index] = new_todo + '\n'
        f.update_file(todo_list)
        window['todos_list'].update(values=todo_list)

    elif events == ps.WIN_CLOSED:
        break

window.close()
