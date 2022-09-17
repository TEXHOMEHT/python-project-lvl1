from random import randint


DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def generate_question_answer():
    number = randint(2, 100)
    for i in range(2, number):
        if number % i == 0:
            correct_answer = "no"
            break
    else:
        correct_answer = "yes"

    question = f'{number}'

    return question, correct_answer
