import functions as f
import PySimpleGUI as ps

ERROR_MSG = 'You must select an item before trying to edit/complete it.'
TITLE = 'Todo List App'
LOGO_FONT = ('Calibri Bold', 25)
DEFAULT_COLOR = '#384ff5'


ps.theme('TanBlue')
ps.theme_button_color(DEFAULT_COLOR)

logo_img = ps.Image(source='images/logo.png', size=(100, 100), pad=0)
logo_text = ps.Text('TODO LIST APP', font=LOGO_FONT, pad=0, text_color='#384ff5')

clock_label = ps.Text('', key='clock')
label = ps.Text('Type in a To-do:')
input_box = ps.InputText(tooltip='Enter a todo', key='add', size=37)

add_button = ps.Button('Add')
edit_button = ps.Button('Edit')
exit_button = ps.Button('Exit', tooltip='Exit the program')
complete_button = ps.Button('Complete')

todo_list = f.get_todos()
list_box = ps.Listbox(values=todo_list, key='todos_list', enable_events=True, size=(36, 10), tooltip='Select a TO-DO '
                                                                                                     'to complete or '
                                                                                                     'edit')

window = ps.Window(TITLE, font=('Helvetica', 13), layout=[
    [logo_img, logo_text],
    [clock_label],
    [label],
    [input_box, add_button],
    [list_box, edit_button, complete_button],
    [exit_button]
])


while True:
    events, values = window.read(timeout=200)
    window['clock'].update(value=f.get_time())

    if events == 'Add':
        new_todo = values['add']
        todo_list.append(new_todo + '\n')
        f.update_file(todo_list)
        window['todos_list'].update(values=todo_list)

    #  text box value changes according to the selected list item
    elif events == 'todos_list':

        try:
            window['add'].update(value=values['todos_list'][0].strip())
        except IndexError:
            continue

    elif events == 'Complete':

        try:
            completed_todo = values['todos_list'][0]
        except IndexError:
            ps.popup(ERROR_MSG, font='Arial', title=TITLE)
            continue

        todo_list.remove(completed_todo)
        f.update_file(todo_list)
        window['todos_list'].update(values=todo_list)
        window['add'].update(value='')

    elif events == 'Edit':

        try:
            completed_todo = values['todos_list'][0]
        except IndexError:
            ps.popup(ERROR_MSG, font='Arial', title=TITLE)
            continue

        to_edit = values['todos_list'][0]
        todo_index = todo_list.index(to_edit)
        new_todo = values['add']
        todo_list[todo_index] = new_todo + '\n'
        f.update_file(todo_list)
        window['todos_list'].update(values=todo_list)

    elif events == ps.WIN_CLOSED or events == 'Exit':
        break

window.close()
