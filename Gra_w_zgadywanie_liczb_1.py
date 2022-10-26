import random


computer = random.randint(1, 100)
guess = 0
while guess != computer:
    try:
        guess = int(input("Guess the number: "))
        if guess < computer:
            result = "Too small!"
        elif guess > computer:
            result = "Too high!"
        elif guess == computer:
            result = "You WIN!"
    except (ValueError, NameError):
        print("It's not a number!")
        continue
    print(result)
