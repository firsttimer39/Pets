import random
import time


class DiceGame:
    def __init__(self, name, player, system, ground):
        self.name = name
        self.player = player
        self.system = system
        self.ground = ground

    def first_round(self):
        print("Round 1")

    def players_roll(self):
        num1 = random.randint(1, 6)
        print(f"First number is {num1}")
        time.sleep(2)
        num2 = random.randint(1, 6)
        print(f"Second number is {num2}")
        time.sleep(2)
        sum_player = num1 + num2
        print(f"You have {sum_player} points")
        time.sleep(2)
        return sum_player

    def systems_roll(self):
        num3 = random.randint(1, 6)
        print(f"First number is {num3}")
        time.sleep(2)
        num4 = random.randint(1, 6)
        print(f"Second number is {num4}")
        time.sleep(2)
        sum_system = num3 + num4
        print(f"System has {sum_system} points")
        time.sleep(2)
        return sum_system

    def check_winner(self, players_result, systems_result):
        if players_result > systems_result:
            print(f"{self.name} wins {players_result}:{systems_result}")
            self.player += 1
        elif players_result == systems_result:
            print(f"Tied game {players_result}:{systems_result}")
        else:
            print(f"System wins {players_result}:{systems_result}")
            self.system += 1

    def reset(self):
        while True:
            reset = input("Do you want to play again Yes/No:")
            if reset == "Yes":
                self.ground += 1
                print(f"Round {self.ground}")
                print(f"Current score is {self.player}:{self.system}")
                players_result = game.players_roll()
                systems_result = game.systems_roll()
                game.check_winner(players_result, systems_result)
            else:
                print(f"Game over! Score is {self.player}:{self.system}")
                print(f"Goodbye {self.name}")


game = DiceGame(input("Enter your name "), 0, 0, 1)
game.first_round()
players_result = game.players_roll()
systems_result = game.systems_roll()
game.check_winner(players_result, systems_result)
game.reset()

