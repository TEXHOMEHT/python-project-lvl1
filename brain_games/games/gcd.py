from random import randint
import math


DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def generate_question_answer():
    first_number = randint(1, 100)
    second_number = randint(1, 100)
    correct_answer = math.gcd(first_number, second_number)

    question = f'{first_number} {second_number}'

    return question, correct_answer
