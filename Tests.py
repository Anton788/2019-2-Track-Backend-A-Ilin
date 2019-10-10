import unittest
import game


class TestGame(unittest.TestCase):
    '''Testing of game'''
    def test_win1(self):
        '''Testing on win'''
        our_game = game.Game()
        our_game.field = ["X", " ", "X", "O", "X", "X", "O", "X", "X"]
        self.assertTrue(our_game.is_win("X"))
        self.assertFalse(our_game.is_win("O"))

    def test_win2(self):
        '''Testing on win'''
        our_game = game.Game()
        our_game.field = ["X", " ", "O", "O", "O", "X", "O", "X", "X"]
        self.assertTrue(our_game.is_win("O"))
        self.assertFalse(our_game.is_win("X"))

    def test_wrong(self):
        '''Testing on loose'''
        our_game = game.Game()
        our_game.field = ["X", "O", "X", "O", "X", "X", "O", "X", "O"]
        self.assertFalse(our_game.is_win("O"))
        self.assertFalse(our_game.is_win("X"))


if __name__ == '__main__':
    unittest.main()
