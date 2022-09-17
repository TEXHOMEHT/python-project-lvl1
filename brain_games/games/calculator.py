from random import randint


DESCRIPTION = 'What is the result of the expression?'


def generate_question_answer():
    operaion = (randint(1, 3))  # Random arithmetic action
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
    question = f'Question: {first_number} {arithmetic_action} {second_number}'
    return question, correct_answer
