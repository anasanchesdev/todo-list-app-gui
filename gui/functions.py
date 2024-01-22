from time import strftime

FILEPATH = 'todos.txt'


def update_file(todos):
    """
    Updates todos.txt file with new values of todo_list.
    :param todos: list of to-dos
    """
    with open(FILEPATH, 'w') as todos_file_f:
        todos_file_f.writelines(todos)


def index_from_todo(index_input):
    """
    Picks the index of the to-do to be edited/completed by the user.
    :param index_input: index given from the user
    :returns: the given index minus 1
    """
    todo_index = int(index_input)
    todo_index -= 1
    return todo_index


def get_time():
    """
    Gets time and formats into string.
    """
    n = strftime('= %A, %b %d, %Y =')
    return n


if __name__ == '__main__':
    pass
