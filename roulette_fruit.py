from random import choice
from os import system, name

def roulette_attempts():
    print("Welcome to the Lucky Wheel. Please enter how many times you want to play.")
    selections = 0
    options_list = list(range(1,5))
    
    while True:
        try:
            while selections not in options_list:
                system('cls' if name == 'nt' else 'clear')
                selections = int(input("Enter the number of times to play (from 1 to 4 times maximum): ")) 
            return selections
        except ValueError:
            print("Please enter a valid number between 1 and 4.")
        except Exception:
            print("Unexpected error, please try again.")

def roulette():
    list_emoji = ['🍎', '🍏', '🍉', '🍇', '🥥','🍒', '🍋', '🍓', '🍊', '🍌', '🥝']
    return [choice(list_emoji) for _ in range(3)]

""" Main Game """
attempts = roulette_attempts()
jackpot = 0

for i in range(attempts):  
    result = roulette()
    print(f"Intento {i + 1}: {result}")              
    if result[0] == result[1] == result[2]:
      print("🎉 Jackpot! Congratulations, all match! 🎉")
      jackpot += 1
    else:
        print("😢 Not this time.")
    print(f"Total Jackpots found: {jackpot}")