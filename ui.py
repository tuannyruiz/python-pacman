# @ -> our hero
# G -> ghosts
#P -> pills
# . -> empty spaces
# | and - -> walls

def ui_print(map):
    for row in map:
        for column in row:
            print(column, end='')
        print('')

def ui_key():
    return input()

def ui_msg(msg):
    print(msg)