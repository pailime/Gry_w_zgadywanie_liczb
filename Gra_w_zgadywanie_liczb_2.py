import random


def user_input():
    possible = ["1", "2", "3"]
    while True:
        user = input()
        if user in possible:
            break
        print("You chose wrong hint")
    return user


def menu():
    main = """
    Imagine number between 0 and 1000!
    Press 1 - if my number is too small
    Press 2 - if my number is too big
    Press 3 - if my number is correct
    Press 'Enter' to START this game!
    """
    print(main)
    input()
    min = 0
    max = 1001
    user = ""
    while user != "3":
        for i in range(10):
            guess = int((max - min) // 2) + min
            print(f"Is your number {guess}?")
            user = user_input()
            if user == "2":
                max = guess
            elif user == "1":
                min = guess
            elif user == "3":
                break
        else:
            print("Are you cheating? :-)")
            return menu()
    print("Yay, I won!")


if __name__ == '__main__':
    menu()
