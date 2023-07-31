import os
import random

def clear_terminal():
    # Function to clear the terminal based on the OS type (Windows or Unix-like systems)
    os.system('cls' if os.name == 'nt' else 'clear')

def calculate_chance(current_multiplier, chances_dict):
    # Function to calculate the chance of moving to the next multiplier
    return chances_dict.get(current_multiplier, 0.05)

def roll_the_dice():
    # Function to prompt the player to press Enter to roll the dice
    input("Press Enter to roll the dice...")

def update_money(current_money, current_multiplier):
    # Function to update the money based on the current multiplier
    money_earned = current_money * current_multiplier
    print(f"Congratulations! You've won x{current_multiplier}! You've earned {money_earned} coins.")
    return money_earned

def play_double_or_nothing(current_money, current_multiplier, chances_dict):
    # Function to play a round of the Double or Nothing game
    print(f"\nCurrent money: {current_money}")
    print(f"Current multiplier: x{current_multiplier}")

    roll_the_dice()
    chance = calculate_chance(current_multiplier, chances_dict)

    if random.random() < chance:
        # Player succeeded to move to the next multiplier
        return update_money(current_money, current_multiplier)
    else:
        # Player failed to move to the next multiplier
        print("Oh no! You didn't make it to the next tier.")
        input("Press Enter to continue...")
        clear_terminal()
        return 0

def main():
    print("Welcome to Double or Nothing!")
    current_money = 25
    current_multiplier = 1
    max_multiplier = 9
    max_amount = 15

    # Define a dictionary to store multipliers and their respective chances
    chances_dict = {i: 0.5 / i for i in range(1, max_multiplier + 1)}
    chances_dict[max_multiplier + 1] = 0.05

    while current_multiplier <= max_multiplier and current_money < max_amount:
        # Play the Double or Nothing game until the max multiplier or max amount is reached
        current_money += play_double_or_nothing(current_money, current_multiplier, chances_dict)
        current_multiplier += 1

    if current_multiplier > max_multiplier:
        print("\nCongratulations! You've reached the maximum multiplier.")
    elif current_money >= max_amount:
        print("\nCongratulations! You've reached the maximum amount.")

    print(f"\nGame over. Final amount: {current_money}")

if __name__ == "__main__":
    main()
