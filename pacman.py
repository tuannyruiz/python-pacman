import random

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

def total_pills(map):
    total = 0
    for x in range(len(map)):
        for y in range(len(map[x])):
            if map[x][y] == 'P':
                total = total + 1
    return total

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

def is_within_borders(map, next_x, next_y):
    number_of_rows = len(map)
    number_of_columns = len(map[0])
    x_is_valid = 0 <= next_x < number_of_rows
    y_is_valid = 0 <= next_y < number_of_columns

    return x_is_valid and y_is_valid

def is_a_wall(map, next_x, next_y):
    return map[next_x][next_y] == '|' or map[next_x][next_y] == '-'

def is_a_ghost(map, next_x, next_y):
    return map[next_x][next_y] == 'G'

def is_a_pill(map, next_x, next_y):
    return map[next_x][next_y] == 'P'

def is_pacman(map, next_x, next_y):
    return map[next_x][next_y] == '@'

def find_ghosts(map):
    all_ghosts = []
    for x in range(len(map)):
        for y in range(len(map[x])):
            if map[x][y] == 'G':
                all_ghosts.append([x,y])
    return all_ghosts

def move_ghosts(map):
    all_ghosts = find_ghosts(map)
    for ghost in all_ghosts:
        ghost_x = ghost[0]
        ghost_y = ghost[1]

        possible_directions = [
            [ghost_x, ghost_y + 1],
            [ghost_x, ghost_y - 1],
            [ghost_x - 1, ghost_y],
            [ghost_x + 1, ghost_y]
        ]

        random_number = random.randint(0, 3)
        next_ghost_x = possible_directions[random_number][0]
        next_ghost_y = possible_directions[random_number][1]

        if (is_a_wall(map, next_ghost_x, next_ghost_y) 
            or is_a_ghost(map, next_ghost_x, next_ghost_y) 
            or is_a_pill(map, next_ghost_x, next_ghost_y)):
            continue

        if is_pacman(map, next_ghost_x, next_ghost_y):
            return True

        new_row = map[ghost_x][0:ghost_y] + '.' + map[ghost_x][ghost_y + 1:]
        map[ghost_x] = new_row

        new_row_2 = map[next_ghost_x][0:next_ghost_y] + 'G' + map[next_ghost_x][next_ghost_y + 1:]
        map[next_ghost_x] = new_row_2

        return False

# play() returns 3 booleans: 
    # isMovementLegal, isPacManAlive, hasPacManWon
def play(map, key): 
    # a -> left
    # d -> right
    # s -> down
    # w -> up
    next_x, next_y = next_position(map, key)

    is_an_invalid_key = next_x == -1 and next_y == -1
    if is_an_invalid_key:
        return False, True, False
    
    if not is_within_borders(map, next_x, next_y):
        return False, True, False
    
    if is_a_wall(map, next_x, next_y):
        return False, True, False
    
    if is_a_ghost(map, next_x, next_y):
        return True, False, False
    
    move_pacman(map, next_x, next_y)

    remaining_pills = total_pills(map)
    if remaining_pills == 0:
        return True, True, True
    else:
        return True, True, False
