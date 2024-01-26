import functions as f
import PySimpleGUI as ps

ERROR_MSG = 'You must select an item before trying to edit/complete it.'
TITLE = 'Todo List App'
DEFAULT_FONT = 'Calibri Bold'
BUTTON_SIZE = (28, 28)
BUTTON_COLOR_MOUSEOVER = 'dark blue'
LOGO_FONT = (DEFAULT_FONT, 25)
INPUT_FONT = ('Calibri', 12)
DEFAULT_COLOR = '#384ff5'

ps.theme('TanBlue')
ps.theme_button_color(DEFAULT_COLOR)

logo_img = ps.Image(source='images/logo.png', size=(100, 100), pad=0)
logo_text = ps.Text('TODO LIST APP', font=LOGO_FONT, pad=0, text_color='#384ff5')
dev_credits = ps.Text('by: anasanchesdev', font=(DEFAULT_FONT, 8), justification='right', pad=((50, 0), (0, 0)))

clock_label = ps.Text('', key='clock', font=(DEFAULT_FONT, 10))
label = ps.Text('Type in a To-do:', font=(DEFAULT_FONT, 15))
input_box = ps.InputText(tooltip='Enter a todo', key='add', size=37, font=INPUT_FONT)

add_button = ps.Button(image_source='images/add.png', key='Add', image_size=BUTTON_SIZE, pad=((18, 0), (0, 0)),
                       tooltip='Add a TO-DO', mouseover_colors=BUTTON_COLOR_MOUSEOVER)

edit_button = ps.Button(image_source='images/edit.png', key='Edit', image_size=BUTTON_SIZE, pad=5,
                        tooltip='Edit a TO-DO', mouseover_colors=BUTTON_COLOR_MOUSEOVER)

exit_button = ps.Button('EXIT', tooltip='Exit the program', font=(DEFAULT_FONT, 12),
                        mouseover_colors=BUTTON_COLOR_MOUSEOVER)

complete_button = ps.Button(image_source='images/complete.png', key='Complete', image_size=BUTTON_SIZE, pad=5,
                            tooltip='Complete a TO-DO', mouseover_colors=BUTTON_COLOR_MOUSEOVER)

todo_list = f.get_todos()

list_box = ps.Listbox(font=INPUT_FONT, values=todo_list, key='todos_list', enable_events=True, size=(35, 10),
                      tooltip='Select a TO-DO to complete or edit')

left_column = [[list_box]]
right_column = [[edit_button], [complete_button]]
left_column = ps.Column(left_column)
right_column = ps.Column(right_column)

window = ps.Window(TITLE, font=('Helvetica', 13), layout=[
    [logo_img, logo_text],
    [label],
    [input_box, add_button],
    [left_column, right_column],
    [exit_button, clock_label, dev_credits]
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

    elif events == ps.WIN_CLOSED or events == 'EXIT':
        break

window.close()
