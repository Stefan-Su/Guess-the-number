# Iteration 1
import random


def generate_random_number():
    random_number = random.randint(1, 100)
    return random_number


def get_user_number(random_number, text):
    user_number = input(text)
    check_user_number(random_number, user_number)


def check_user_number(random_number, user_number):
    try:
        int(user_number)
        if int(user_number) < 1 or int(user_number) > 100:
            get_user_number(random_number, 'Error: Only numbers between 1 and 100 allowed. try again. Enter a number: ')
        else:
            evaluation(random_number, user_number)
    except ValueError:
        get_user_number(random_number, 'Error: Only numbers allowed. try again. Enter a number: ')


def evaluation(random_number, user_number):
    if random_number == int(user_number):
        print(f"You guessed right. The random number was {random_number}!")
    else:
        get_user_number(random_number, 'Guessed wrong, try again. Enter a number: ')


# Welcome message
print('Welcome to the program: guess the number!')
# Generates the random number between 1 and 100
random_number = generate_random_number()
get_user_number(random_number, 'A number between 1 and 100 has been generated, try to guess it now: ')
