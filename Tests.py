import unittest
import Game


class TestGame(unittest.TestCase):
    def test_win1(self):
        game = Game.Game()
        game.field = ["X", " ", "X", "O", "X", "X", "O", "X", "X"]
        self.assertEqual(True, game.is_win("X"))
        self.assertEqual(False, game.is_win("O"))

    def test_win2(self):
        game = Game.Game()
        game.field = ["X", " ", "O", "O", "O", "X", "O", "X", "X"]
        self.assertEqual(True, game.is_win("O"))
        self.assertEqual(False, game.is_win("X"))

    def test_wrong(self):
        game = Game.Game()
        game.field = ["X", "O", "X", "O", "X", "X", "O", "X", "O"]
        self.assertEqual(False, game.is_win("O"))
        self.assertEqual(False, game.is_win("X"))


if __name__ == '__main__':
    unittest.main()
