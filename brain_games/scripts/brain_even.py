#!/usr/bin/env python3
from random import randint


correct_answer = str()

random_number = randint(1, 100)


def brain_even(random_number):
    print('Answer "yes" if the number is even, otherwise answer "no".')
    print(f'Question: {random_number}')
    answer = input()
    i = 0
    while True:
        if random_number % 2 == 0 and answer == 'yes':
            True
            print('Correct!')
            i += 1
            if i == 3:
                print('Congratulations, name!')
                break
        elif random_number % 2 != 0 and answer == 'no':
            True
            print('Correct!')
            i += 1
            if i == 3:
                print('Congratulations, Sam!')
                break
        else: 
            False 
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.\nLet's try again, name!")
            break

brain_even(random_number)
