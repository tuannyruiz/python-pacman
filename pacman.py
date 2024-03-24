from ui import ui_print

map = [
    '|--------|',
    '|G..|..G.|',
    '|...PP...|',
    '|G...@.|.|',
    '|........|',
    '|--------|'
]

def find_pacman(map):
    pacman_x = -1
    pacman_y = -1

    for x in range(len(map)):
        for y in range(len(map[x])):
            if map[x][y] == '@':
                pacman_x = x
                pacman_y = y

    return pacman_x, pacman_y


def move_pacman(map, next_pacman_x, next_pacman_y):
    pacman_x, pacman_y = find_pacman(map)

    new_row = map[pacman_x][0:pacman_y] + '.' + map[pacman_x][pacman_y + 1:]
    map[pacman_x] = new_row

    new_row_2 = map[next_pacman_x][0:next_pacman_y] + '@' + map[next_pacman_x][next_pacman_y + 1:]
    map[next_pacman_x] = new_row_2


def play(map, key): 
    # a -> left
    # d -> right
    # s -> down
    # w -> up
    next_x, next_y = next_position(map, key)
    move_pacman(map, next_x, next_y)


def next_position(map, key):
    x, y = find_pacman(map)
    next_x = -1
    next_y = -1

    if key == 'a':
        next_x = x
        next_y = y - 1
    elif key == 'd':
        next_x = x
        next_y = y + 1
    elif key == 'w':
        next_y = y
        next_x = x - 1
    elif key == 's':
        next_y = y
        next_x = x + 1
    
    return next_x, next_y

    