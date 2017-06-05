import unittest

from app import game


class GameTest(unittest.TestCase):
    def test_get_score__for_new_game_and_cero_num_pins_knocked__game_get_score_return_cero(self):
        # Arrange
        bowling_game = game.Game()
        # Act
        bowling_game.record_roll(num_pins_knocked=0)
        result = bowling_game.get_score()
        # Assert
        self.assertEqual(first=0, second=result)

    def test_get_score__for_new_game_and_5_pins_knocked__game_get_score_return_cero(self):
        # Arrange
        bowling_game = game.Game()
        # Act
        bowling_game.record_roll(num_pins_knocked=5)
        result = bowling_game.get_score()
        # Assert
        self.assertEqual(first=0, second=result)

    def test_get_score__after_5_pins_knocked_and_0_pins_knocked__game_get_score_return_5(self):
        # Arrange
        bowling_game = game.Game()
        bowling_game.record_roll(num_pins_knocked=0)
        # Act
        bowling_game.record_roll(num_pins_knocked=5)
        result = bowling_game.get_score()
        # Assert
        self.assertEqual(first=5, second=result)

    def test_get_score__after_5_pins_knocked_and_3_completed_sets_with_4_4_6_1_0_5__game_get_score_return_20(self):
        # Arrange
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

    def test_get_score__after_5_pins_knocked_and_spare__game_get_score_return_15(self):
        # Arrange
        bowling_game = game.Game()
        bowling_game.record_roll(num_pins_knocked=0)
        bowling_game.record_roll(num_pins_knocked=10)
        # Act
        bowling_game.record_roll(num_pins_knocked=5)
        result = bowling_game.get_score()
        # Assert
        self.assertEqual(first=15, second=result)

    def test_get_score__after_5_pins_knocked_and_two_consecutive_spares_0_10__game_get_score_return_25(self):
        # Arrange
        bowling_game = game.Game()
        bowling_game.record_roll(num_pins_knocked=0)
        bowling_game.record_roll(num_pins_knocked=10)
        bowling_game.record_roll(num_pins_knocked=0)
        bowling_game.record_roll(num_pins_knocked=10)
        # Act
        bowling_game.record_roll(num_pins_knocked=5)
        result = bowling_game.get_score()
        # Assert
        self.assertEqual(first=25, second=result)
