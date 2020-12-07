import unittest

from classes.rps_game import RpsGame, winning_game_choice
from classes.player import Player


class TestRpsGame(unittest.TestCase):

    def setUp(self):
        self.player_1 = Player("Turing", "rock")
        self.player_2 = Player("Boole", "paper")
        self.player_3 = Player("Babbage", "scissors")


    def test_rock_beats_paper(self, player_1, player_2, player_3):
        game_result = winning_game_choice(self.player_1.game_choice, self.player_2.game_choice)
        self.assertEqual(self.player_1.game_choice, game_result)