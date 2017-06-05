import unittest

from app import game


class GameTest(unittest.TestCase):
    def test_record_roll__with_new_game_and_cero_num_pins_knocked__game_get_score_return_cero(self):
        # Assert
        bowling_game = game.Game()
        # Act
        bowling_game.record_roll(num_pins_knocked=0)
        result = bowling_game.get_score()
        # Assert
        self.assertEqual(first=0, second=result)

    def test_record_roll__with_new_game_and_5_pins_knocked__game_get_score_return_cero(self):
        # Assert
        bowling_game = game.Game()
        # Act
        bowling_game.record_roll(num_pins_knocked=5)
        result = bowling_game.get_score()
        # Assert
        self.assertEqual(first=0, second=result)

    def test_record_roll__5_pins_knocked_after_0_pins_knocked__game_get_score_return_5(self):
        # Assert
        bowling_game = game.Game()
        bowling_game.record_roll(num_pins_knocked=0)
        # Act
        bowling_game.record_roll(num_pins_knocked=5)
        result = bowling_game.get_score()
        # Assert
        self.assertEqual(first=5, second=result)

    def test_record_roll__5_pins_knocked_after_3_completed_sets_with_4_4_6_1_0_5__game_get_score_return_20(self):
        # Assert
        bowling_game = game.Game()
        bowling_game.record_roll(num_pins_knocked=4)
        bowling_game.record_roll(num_pins_knocked=4)
        bowling_game.record_roll(num_pins_knocked=6)
        bowling_game.record_roll(num_pins_knocked=1)
        bowling_game.record_roll(num_pins_knocked=0)
        bowling_game.record_roll(num_pins_knocked=5)
        # Act
        bowling_game.record_roll(num_pins_knocked=5)
        result = bowling_game.get_score()
        # Assert
        self.assertEqual(first=20, second=result)
