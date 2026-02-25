print("WELCOME!")
print("Guess The Hidden Number Game")
print("Rules:")
print("1. You have 10 chances to guess the number.")
print("2. Enter only digits.")
print()

secret_number = 7
print("Are you ready? Let's start!")

for attempt in range(1, 11):
    guess = int(input(f"Attempt {attempt}: Enter your guess: "))

    if guess == secret_number:
        print("🎉 Congratulations! You won the game!")
        break
    else:
        print("Wrong guess. Try again!")

else:
    print(" You lost! The correct number was", secret_number)
