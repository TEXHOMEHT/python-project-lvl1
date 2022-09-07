from random import randint
from colorama import Fore
import prompt


def arithmetic_progression():
    print(Fore.GREEN + 'Welcome to the Brain Games!')  # Greet player
    name = prompt.string('May I have your name? ')  # Asking player's name
    print(f'Hello, {name}!')
    print('What number is missing in the progression?')  # Define game rules

    i = 0  # Count of the game rounds
    while True:
        first_number = randint(1, 100)
        n = randint(2, 10)
        count = randint(5, 10)
        answer_index = randint(1, count - 1)
        question = f"{first_number}"
        correct_answer = ""

        for num in range(1, count):
            first_number += n
            if num == answer_index:
                question = f"{question} .."
                correct_answer = str(first_number)
            else:
                question = f"{question} {first_number}"

        print(f"Question: {question}")
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
