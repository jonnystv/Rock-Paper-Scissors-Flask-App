from app.models.player import Player

class RpsGame:

    def __init__(self, player_1, player_2):
            self.player_1 = player_1
            self.player_2 = player_2

    player_1 = Player("Turing", "rock")
    player_2 = Player("Boole", "paper")
    player_3 = Player("Babbage", "scissors")


    def winning_game_choice(self, player_1, player_2):
        if player_1.game_choice == "rock" and player_2.game_choice == "scissors":
            return player_1

        if player_1.game_choice == "scissors" and player_2.game_choice == "paper":
            return player_1

        if player_1.game_choice == "paper" and player_2.game_choice == "rock":
            return player_1

        if player_1.game_choice == player_2.game_choice:
            return None

        return player_2