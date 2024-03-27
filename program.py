from pacman import move_ghosts, play
from ui import ui_print, ui_key, ui_msg

map = [
    '|--------|',
    '|G..|..G.|',
    '|...PP...|',
    '|G...@.|.|',
    '|........|',
    '|--------|'
]

game_finished = False

while not game_finished:
    ui_print(map)
    key = ui_key();
    valid_key, pacman_alive, pacman_won = play(map, key)

    pacman_was_hit = move_ghosts(map)

    if not pacman_alive or pacman_was_hit:
        ui_msg("You died :(")
        game_finished = True
    elif pacman_won:
        ui_msg("You won the game!!!")
        game_finished = True

