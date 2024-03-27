import unittest

from pacman import find_pacman, move_pacman, next_position

map_with_pacman = [
    "|--------|",
    "|G..|..G.|",
    "|...PP...|",
    "|G...@.|.|",
    "|........|",
    "|--------|"
]

class PacmanTest (unittest.TestCase):

    def test_find_pacman(self):
        x, y = find_pacman(map_with_pacman)

        self.assertEqual(x, 3)
        self.assertEqual(y, 5)

    def test_find_pacman_when_pacman_doesnt_exist(self):
        map = [
            "|--------|",
            "|G..|..G.|",
            "|...PP...|",
            "|G.....|.|",
            "|........|",
            "|--------|"
        ]

        x, y = find_pacman(map)

        self.assertEqual(x, -1)
        self.assertEqual(y, -1)

    def test_move_pacman(self):
        moveMap = map_with_pacman
        move_pacman(moveMap, 4, 1)
        new_x, new_y = find_pacman(moveMap)

        self.assertEqual(new_x, 4)
        self.assertEqual(new_y, 1)

    def test_next_position(self):
        nextPosMap = map_with_pacman
        next_x, next_y = next_position(nextPosMap, 'd')

        self.assertEqual(next_x, 4)
        self.assertEqual(next_y, 2)