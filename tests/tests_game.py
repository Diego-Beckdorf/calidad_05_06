import unittest

from app import game


class GameTest(unittest.TestCase):
    def test_record_roll__with_new_game_and_cero_num_pins_knocked__game_return_cero(self):
        # Assert
        bowling_game = game.Game()
        # Act
        bowling_game.record_roll(num_pins_knocked=0)
        result = bowling_game.get_score()
        # Assert
        self.assertEqual(first=0, second=result)