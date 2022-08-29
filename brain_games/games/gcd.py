from random import randint
from colorama import Fore
import prompt
import math


def gcd():
    print(Fore.GREEN + 'Welcome to the Brain Games!')  # Greet player
    name = prompt.string('May I have your name? ')  # Asking player's name
    print(f'Hello, {name}!')
    # Define game rules
    print('Find the greatest common divisor of given numbers.')

    i = 0  # Count of the game rounds
    while True:
        first_number = randint(1, 100)
        second_number = randint(1, 100)
        correct_answer = math.gcd(first_number, second_number)

        print(f'Question: {first_number} {second_number}')
        answer = (input('Your answer: '))  # Asking player's answer

        if answer == str(correct_answer):  # Player's answer is correct
            print('Correct!')
            i += 1
        else:  # Player's answer is incorrect
            print(f"'{answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'."
                  f"\nLet's try again, {name}!")
            break
        if i == 3:
            print(f'Congratulations, {name}!')
            break
