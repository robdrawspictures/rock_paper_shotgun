import random
from models.player import Player

class Game:
    def __init__(self, player1, player2):
        self.p1 = player1
        self.p2 = player2

    def play_game(self):
        if self.p1.choice == "rock" and self.p2.choice == "scissors":
            return f"{self.p1.name} wins!"
        elif self.p1.choice == "scissors" and self.p2.choice == "paper":
            return f"{self.p1.name} wins!"
        elif self.p1.choice == "paper" and self.p2.choice == "rock":
            return f"{self.p1.name} wins!"
        elif self.p1.choice == self.p2.choice:
            return f"{self.p1.name} and {self.p2.name} made the same choice. It's a draw!"
        else:
            return f"{self.p2.name} wins!"


    # def vs_computer(self):
    #     choices = ["rock", "paper", "scissors"]
    #     if self.p2.name == "computer":
    #         self.p2 = Player("Computer", random.choice(choices))
        
    #     if self.p1.choice == "rock" and self.p2.choice == "scissors":
    #         return f"{self.p1.name} wins!"
    #     elif self.p1.choice == "scissors" and self.p2.choice == "paper":
    #         return f"{self.p1.name} wins!"
    #     elif self.p1.choice == "paper" and self.p2.choice == "rock":
    #         return f"{self.p1.name} wins!"
    #     elif self.p1.choice == self.p2.choice:
    #         return f"{self.p1.name} and {self.p2.name} made the same choice. It's a draw!"
    #     else:
    #         return f"{self.p2.name} wins!"

        