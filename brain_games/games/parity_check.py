from random import randint
from colorama import Fore
import prompt


def parity_check():
    print(Fore.GREEN + 'Welcome to the Brain Games!')  # Greet player
    name = prompt.string('May I have your name? ')  # Asking player's name
    print(f'Hello, {name}!')
    # Define game rules
    print('Answer "yes" if the number is even, otherwise answer "no".')

    i = 0  # Count of the game rounds
    while True:
        random_number = randint(1, 100)
        print(f'Question: {random_number}')

        answer = input('Your answer: ')  # Asking player's answer
        is_answer_correct = (random_number % 2 == 0 and answer == 'yes'
                             or random_number % 2 != 0 and answer == 'no')

        if is_answer_correct:  # Player's answer is correct
            print('Correct!')
            i += 1
        else:  # Player's answer is incorrect
            correct_answer = 'no' if answer == 'yes' else 'yes'
            print(f"'{answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'."
                  f"\nLet's try again, {name}!")
            break
        if i == 3:
            print(f'Congratulations, {name}!')
            break
