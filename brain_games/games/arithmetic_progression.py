from random import randint
from colorama import Fore
import prompt


def arithmetic_progression():
    print(Fore.GREEN + 'Welcome to the Brain Games!')  # Greet player
    name = prompt.string('May I have your name? ')  # Asking player's name
    print(f'Hello, {name}!')
    print('What is the result of the expression?')  # Define game rules

    i = 0  # Count of the game rounds
    while True:
        first_number = randint(1, 49)
        second_number = randint(50, 100)
        n = randint(2, 10)
        progression = range(first_number, second_number, n)
        len_progression = len(progression)
        index = randint(2, len_progression - 1)
        correct_answer = progression[index]

        if len_progression >= 5 and len_progression <= 10:
            # Removing [ and ]
            str_progression = str(list(progression))[1:-1]  # Removing [ and ]
            # Formating question
            question = (str_progression.replace(str(correct_answer), ".."))
            comma = ','
            # Removing commas and asking a question
            print(f'Question: {question.replace(comma,"")}')
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
