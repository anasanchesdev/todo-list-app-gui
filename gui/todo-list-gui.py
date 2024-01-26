import functions as f
import PySimpleGUI as ps

todo_list = f.get_todos()
label = ps.Text('Type in a To-do:')
input_box = ps.InputText(tooltip='Enter a todo', key='add')
add_button = ps.Button('Add')
edit_button = ps.Button('Edit')
exit_button = ps.Button('Exit', tooltip='Exit the program')
complete_button = ps.Button('Complete')
list_box = ps.Listbox(values=todo_list, key='todos_list', enable_events=True, size=(40, 10), tooltip='Select a TO-DO '
                                                                                                     'to complete or '
                                                                                                     'edit')

window = ps.Window('Todo List App', font=('Helvetica', 13), layout=[
    [label],
    [input_box, add_button],
    [list_box, edit_button, complete_button],
    [exit_button]
])


while True:
    events, values = window.read()

    print(f'EVENT: {events}\nVALUES: {values}')

    if events == 'Add':
        new_todo = values['add']
        todo_list.append(new_todo + '\n')
        f.update_file(todo_list)
        window['todos_list'].update(values=todo_list)

    #  text box value changes according to the selected list item
    elif events == 'todos_list':
        print(values['todos_list'])
        window['add'].update(value=values['todos_list'][0].strip())

    elif events == 'Complete':
        completed_todo = values['todos_list'][0]
        todo_list.remove(completed_todo)
        f.update_file(todo_list)
        window['todos_list'].update(values=todo_list)
        window['add'].update(value='')

    elif events == 'Edit':
        to_edit = values['todos_list'][0]
        todo_index = todo_list.index(to_edit)
        new_todo = values['add']
        todo_list[todo_index] = new_todo + '\n'
        f.update_file(todo_list)
        window['todos_list'].update(values=todo_list)

    elif events == ps.WIN_CLOSED or events == 'Exit':
        break

window.close()
