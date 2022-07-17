import random

random_number = random.randint(0, 50)
print("Guess the number between 0 and 50. You will have 7 tries.")


def game():
    for item in range(7):
        user_input = int(input("Enter the number below:\n"))
        if user_input < random_number:
            print("The value is too low")
        elif user_input > random_number:
            print("The value is too high")
        elif user_input == random_number:
            print("You guessed correctly")
            return
    print("You were not able to guess the number."
          "\nRestart the game to continue, the number will be reset.")


game()
