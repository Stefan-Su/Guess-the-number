# Iteration 2
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
        hint(random_number, int(user_number))
        get_user_number(random_number, 'Guessed wrong, try again. Enter a number: ')


def hint(random_number, user_number):
    hints = [
        ["Extreme cold", 50, 99],
        ["Very cold", 35, 49],
        ["Cold", 25, 34],
        ["Warm", 15, 24],
        ["Very warm", 6, 14],
        ["Extreme warm", 1, 5]
    ]
    directions = [": go up", ": go down"]
    difference = random_number - int(user_number)
    converted_difference_to_str = str(difference)
    striped_difference = converted_difference_to_str.strip('-')
    converted_difference_to_int = int(striped_difference)
    if converted_difference_to_int >= hints[0][1] and converted_difference_to_int <= hints[0][2]:
        if difference <= 0:
            direction = directions[1]
        else:
            direction = directions[0]
        print(f'{hints[0][0]}{direction}')
    elif converted_difference_to_int >= hints[1][1] and converted_difference_to_int <= hints[1][2]:
        if difference <= 0:
            direction = directions[1]
        else:
            direction = directions[0]
        print(f'{hints[1][0]}{direction}')
    elif converted_difference_to_int >= hints[2][1] and converted_difference_to_int <= hints[2][2]:
        if difference <= 0:
            direction = directions[1]
        else:
            direction = directions[0]
        print(f'{hints[2][0]} {direction}')
    elif converted_difference_to_int >= hints[3][1] and converted_difference_to_int <= hints[3][2]:
        if difference <= 0:
            direction = directions[1]
        else:
            direction = directions[0]
        print(f'{hints[3][0]} {direction}')
    elif converted_difference_to_int >= hints[4][1] and converted_difference_to_int <= hints[4][2]:
        if difference <= 0:
            direction = directions[1]
        else:
            direction = directions[0]
        print(f'{hints[4][0]} {direction}')
    elif converted_difference_to_int >= hints[5][1] and converted_difference_to_int <= hints[5][2]:
        if difference <= 0:
            direction = directions[1]
        else:
            direction = directions[0]
        print(f'{hints[5][0]} {direction}')


# Welcome message
print('Welcome to the program: guess the number!')
# Generates the random number between 1 and 100
random_number = generate_random_number()
get_user_number(random_number, 'A number between 1 and 100 has been generated, try to guess it now: ')
