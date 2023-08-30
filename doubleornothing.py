import os
import random
import subprocess

def clear_terminal():
    # Function to clear the terminal screen
    subprocess.run(['clear' if os.name == 'posix' else 'cls'], shell=True)

def calculate_chance(current_multiplier, chances_dict):
    # Function to calculate the chance of moving to the next multiplier
    return chances_dict.get(current_multiplier, 0.05)

def roll_the_dice():
    # Function to prompt the player to roll the dice
    input("Press Enter to roll the dice...")

def update_money(current_money, current_multiplier):
    # Function to update the money based on the current multiplier
    money_earned = current_money * current_multiplier
    print(f"Congratulations! You've won x{current_multiplier}! You've earned {money_earned} coins.")
    return money_earned

class DoubleOrNothingGame:
    def __init__(self):
        self.current_money = 25
        self.current_multiplier = 1
        self.max_multiplier = 9
        self.max_amount = 15
        self.chances_dict = {i: 0.5 / i for i in range(1, self.max_multiplier + 1)}
        self.chances_dict[self.max_multiplier + 1] = 0.05

    def play_round(self):
        print(f"\nCurrent money: {self.current_money}")
        print(f"Current multiplier: x{self.current_multiplier}")
        roll_the_dice()
        chance = calculate_chance(self.current_multiplier, self.chances_dict)
        
        if random.random() < chance:
            self.current_money += update_money(self.current_money, self.current_multiplier)
            self.current_multiplier += 1
        else:
            print("Oh no! You didn't make it to the next tier.")
            input("Press Enter to continue...")
            clear_terminal()

    def play_game(self):
        print("Welcome to Double or Nothing!")
        while self.current_multiplier <= self.max_multiplier and self.current_money < self.max_amount:
            self.play_round()

        if self.current_multiplier > self.max_multiplier:
            print("\nCongratulations! You've reached the maximum multiplier.")
        elif self.current_money >= self.max_amount:
            print("\nCongratulations! You've reached the maximum amount.")

        print(f"\nGame over. Final amount: {self.current_money}")

if __name__ == "__main__":
    game = DoubleOrNothingGame()
    game.play_game()
