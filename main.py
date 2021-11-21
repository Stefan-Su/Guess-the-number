# Iteration 3
import random


class text_collors:
    YELLOW = '\033[93m'
    GREEN = '\033[92m'
    RED = '\033[1;31m'
    ENDC = '\033[0m'


def generate_random_number():
    random_number = random.randint(1, 100)
    return random_number


def get_user_number(random_number, text, score_list):
    user_number = input(text)
    check_user_number(random_number, user_number, score_list)


def check_user_number(random_number, user_number, score_list):
    try:
        int(user_number)
        if int(user_number) < 1 or int(user_number) > 100:
            message = '\nError: Only numbers between 1 and 100 allowed. try again. Enter a number: '
            get_user_number(random_number, message, score_list)
        else:
            evaluation(random_number, user_number, score_list)
    except ValueError:
        message = '\nError: Only numbers allowed. try again. Enter a number: '
        get_user_number(random_number, message, score_list)


def evaluation(random_number, user_number, score_list):
    if random_number == int(user_number):
        print(f'\nYou guessed right. The random number was {random_number}!\n'
              f'Your score is {text_collors.GREEN}{100 - sum(score_list) + 100} points{text_collors.ENDC}\n'
              f'After {len(score_list)} tries you guessed the correct number.')
    else:
        hint(random_number, int(user_number), score_list)
        message = '\nGuessed wrong, try again. Enter a number: '
        get_user_number(random_number, message, score_list)


def hint(random_number, user_number, score_list):
    # Schema: Name, difference from, difference to
    hints = [
        [f'{text_collors.RED}Extreme cold:{text_collors.ENDC}', 50, 99, 10],
        [f'{text_collors.RED}Very cold:{text_collors.ENDC}', 35, 49, 8],
        [f'{text_collors.RED}Cold:{text_collors.ENDC}', 25, 34, 6],
        [f'{text_collors.RED}Warm:{text_collors.ENDC}', 15, 24, 4],
        [f'{text_collors.RED}Very warm:{text_collors.ENDC}', 6, 14, 2],
        [f'{text_collors.RED}Extreme warm:{text_collors.ENDC}', 1, 5, 1]
    ]
    directions = [f'{text_collors.RED} go up {text_collors.ENDC}',
                  f'{text_collors.RED} go down {text_collors.ENDC}']
    difference = random_number - int(user_number)
    converted_difference_to_str = str(difference)
    striped_difference = converted_difference_to_str.strip('-')
    converted_difference_to_int = int(striped_difference)
    if converted_difference_to_int >= hints[0][1] and converted_difference_to_int <= hints[0][2]:
        if difference <= 0:
            direction = directions[1]
        else:
            direction = directions[0]
        score(score_list, hints, 0, 3)
        print(f'Your number is {text_collors.GREEN}{user_number}{text_collors.ENDC} and its {hints[0][0]} {direction}')
    elif converted_difference_to_int >= hints[1][1] and converted_difference_to_int <= hints[1][2]:
        if difference <= 0:
            direction = directions[1]
        else:
            direction = directions[0]
        score(score_list, hints, 1, 3)
        print(f'Your number is {text_collors.GREEN}{user_number}{text_collors.ENDC} and its {hints[1][0]} {direction}')
    elif converted_difference_to_int >= hints[2][1] and converted_difference_to_int <= hints[2][2]:
        if difference <= 0:
            direction = directions[1]
        else:
            direction = directions[0]
        score(score_list, hints, 2, 3)
        print(f'Your number is {text_collors.GREEN}{user_number}{text_collors.ENDC} and its {hints[2][0]} {direction}')
    elif converted_difference_to_int >= hints[3][1] and converted_difference_to_int <= hints[3][2]:
        if difference <= 0:
            direction = directions[1]
        else:
            direction = directions[0]
        score(score_list, hints, 3, 3)
        print(f'Your number is {text_collors.GREEN}{user_number}{text_collors.ENDC} and its {hints[3][0]} {direction}')
    elif converted_difference_to_int >= hints[4][1] and converted_difference_to_int <= hints[4][2]:
        if difference <= 0:
            direction = directions[1]
        else:
            direction = directions[0]
        score(score_list, hints, 4, 3)
        print(f'Your number is {text_collors.GREEN}{user_number}{text_collors.ENDC} and its {hints[4][0]} {direction}')
    elif converted_difference_to_int >= hints[5][1] and converted_difference_to_int <= hints[5][2]:
        if difference <= 0:
            direction = directions[1]
        else:
            direction = directions[0]
        score(score_list, hints, 5, 3)
        print(f'Your number is {text_collors.GREEN}{user_number}{text_collors.ENDC} and its {hints[5][0]} {direction}')


def score(score_list, hints, index_a, index_b):
    score_list.append(hints[index_a][index_b])
    print(f'\nYour score reduced by {text_collors.GREEN}{hints[index_a][index_b]} points{text_collors.ENDC}, '
          f'and is now: {text_collors.GREEN}{100 - sum(score_list) + 100} points{text_collors.ENDC}')
    return score_list


score_list = [100]
# Welcome message
welcome_message = f'Welcome to the program: guess the number!\nYour score is ' \
                  f'{text_collors.GREEN}{sum(score_list)} points{text_collors.ENDC}. ' \
                  f'Points will be deducted for every wrong guess. If you run out of points, you lost'
print(welcome_message)
start_message = 'A number between 1 and 100 has been generated, try to guess it now: '
# Generates the random number between 1 and 100
random_number = generate_random_number()
get_user_number(random_number, start_message, score_list)
