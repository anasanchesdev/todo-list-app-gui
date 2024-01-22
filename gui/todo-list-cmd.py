from functions import update_file, index_from_todo, get_time

ERROR_MSG = "You must type a valid index or there isn't to-dos to be edited/completed. Please, try again."
ERRORS = (ValueError, TypeError, IndexError)

with open('todos.txt', 'r') as todos_file:  # creates todo_list based on previous todos
    todo_list = todos_file.readlines()

print('🗹 TO-DO APP 🗹')
print(get_time())

while True:

    user_input = input('\nType add, show, edit, complete or exit:\n > ').lower().strip()

    if user_input.startswith('add'):

        todo_added = user_input[4:]
        if any(todo_added):
            todo_added = todo_added.capitalize() + '\n'
        else:
            print(f'"add" cant be empty.')
            continue

        todo_list.append(todo_added)
        update_file(todo_list)
        print(f'\nTo-do "{todo_added.strip()}" added!')

    elif user_input.startswith('show'):

        print('')
        if any(todo_list):
            for index, todo in enumerate(todo_list):
                print(f'{index + 1}.', todo.strip())
        else:
            print('Nothing here!')

    elif user_input.startswith('edit'):

        try:
            edited_todo_index = index_from_todo(user_input[5:])
            edited_todo = todo_list[edited_todo_index]
            new_edit_todo = input('Enter the new todo:\n > ').capitalize() + '\n'
            todo_list[edited_todo_index] = new_edit_todo
            update_file(todo_list)
            print(f'\n"{edited_todo.strip()}" changed to "{new_edit_todo.strip()}" successfully!"')

        except ERRORS:
            print(ERROR_MSG)
            continue

    elif user_input.startswith('complete'):

        try:
            completed_todo_index = index_from_todo(user_input[9:])
            completed_todo = todo_list[completed_todo_index]
            todo_list.pop(completed_todo_index)
            update_file(todo_list)
            print(f'You completed "{completed_todo.strip()}"! Yay!!')

        except ERRORS:
            print(ERROR_MSG)
            continue

    elif user_input == 'exit':
        break

    else:
        print(f'\nThe given command is unknown. Please, try again.')
