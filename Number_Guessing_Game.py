import random

def user_guess():
    while True:
        try:
            return int(input("Guess the number: "))
        except:
            print("Invalid input! Enter a number.")

while True:
    # difficulty selection
    while True:
        ask = input("Level of Difficulty: (easy/hard): ").lower()

        if ask == "easy":
            comp = random.randint(1, 20)
            print("Guess a number between 1 and 20")
            break
        elif ask == "hard":
            comp = random.randint(1, 100)
            print("Guess a number between 1 and 100")
            break
        else:
            print("Invalid difficulty! Choose easy or hard.")

    attempt = 0

    while True:
        gue = user_guess()
        attempt += 1

        if gue == comp:
            print("You got it!")
            print("Attempts:", attempt)
            break

        elif gue < comp:
            print("Too LOW")
        else:
            print("Too HIGH")

        if attempt == 5:
            print("You lose! The number was:", comp)
            break

    # replay system
    while True:
        user_choice = input("Do you want to play again? (y/n): ").lower()

        if user_choice == "y":
            break
        elif user_choice == "n":
            print("Game ended.")
            exit()
        else:
            print("Invalid input!")