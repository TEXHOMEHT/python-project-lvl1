from random import randint
from colorama import Fore
import prompt


def parity_check():
    print(Fore.GREEN + 'Welcome to the Brain Games!')  #Greet user
    name = prompt.string('May I have your name? ')  #Asking user's name
    print(f'Hello, {name}!')
    random_number = randint(1, 100)
    print('Answer "yes" if the number is even, otherwise answer "no".')  #Define game rules
    i = 0  #Count of the game rounds
    while True:
        print(f'Question: {random_number}') #
        answer = input('Your answer: ') #Asking user's answer
        if random_number % 2 == 0 and answer == 'yes' or random_number % 2 != 0 and answer == 'no':  #User's answer is correct
            True
            print('Correct!')
            i += 1
            random_number = randint(1, 100)
            if i == 3:
                print('Congratulations, name!')
                break
        else:  #User's answer is incorrect
            False
            if answer == 'yes':
                correct_answer = str('no')
                print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.\nLet's try again, {name}!")
                break
            else:
                correct_answer = str('yes')
                print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.\nLet's try again, {name}!")
                break
