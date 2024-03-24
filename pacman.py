from ui import ui_print
# @ -> our hero
# G -> ghosts
#P -> pills
# . -> empty spaces
# | and - -> walls

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


ui_print(map)