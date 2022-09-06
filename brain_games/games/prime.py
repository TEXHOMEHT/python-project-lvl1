from random import randint
from colorama import Fore
from math import sqrt
import prompt


def prime():
    print(Fore.GREEN + 'Welcome to the Brain Games!')  # Greet player
    name = prompt.string('May I have your name? ')  # Asking player's name
    print(f'Hello, {name}!')
    # Define game rules
    print('Answer "yes" if given number is prime. Otherwise answer "no".')

    i = 0  # Count of the game rounds
    while True:
        is_prime = True
        number = randint(2, 100)
        n = 2
        while n <= sqrt(number):
            if number % n == 0:
                is_prime = False
                break
            n += 1

        print(f'Question: {number}')

        answer = input('Your answer: ')  # Asking player's answer

        is_correct = True if (is_prime and answer == 'yes'
                              or not is_prime and answer == "no") else False

        if is_correct:  # Player's answer is correct
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
