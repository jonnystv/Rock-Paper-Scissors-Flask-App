import unittest

from classes.player import Player

class TestPlayer(unittest.TestCase):

    def setUp(self):
        self.player_1 = Player("Turing", "rock")


    def test_player_has_name(self):
        self.assertEqual("Turing", self.player_1.name)


    def test_player_has_game_choice(self):
        self.assertEqual("rock", self.player_1.game_choice)