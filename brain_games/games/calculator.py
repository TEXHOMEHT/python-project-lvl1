from random import randint
from colorama import Fore
import prompt


def calculator():
    print(Fore.GREEN + 'Welcome to the Brain Games!')  # Greet player
    name = prompt.string('May I have your name? ')  # Asking player's name
    print(f'Hello, {name}!')
    print('What is the result of the expression?')  # Define game rules

    i = 0  # Count of the game rounds
    while True:
        operaion = (randint(1, 4))  # Random arithmetic action
        first_number = randint(1, 100)
        second_number = randint(1, 100)
        if operaion == 1:  # Addition
            arithmetic_action = '+'
            correct_answer = (first_number + second_number)
        if operaion == 2:  # Multiplication
            arithmetic_action = '*'
            correct_answer = (first_number * second_number)
        if operaion == 3:  # Subtraction
            arithmetic_action = '-'
            correct_answer = (first_number - second_number)
        if operaion == 4:  # Integer division
            arithmetic_action = '//'
            correct_answer = int(first_number // second_number)

        print(f'Question: {first_number} {arithmetic_action} {second_number}')
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
