from random import randint


DESCRIPTION = 'What number is missing in the progression?'


def generate_question_answer():
    first_number = randint(1, 100)
    n = randint(2, 10)
    count = randint(5, 10)
    answer_index = randint(1, count - 1)
    question = f"{first_number}"
    correct_answer = ''
    for num in range(1, count):
        first_number += n
        if num == answer_index:
            question = f"{question} .."
            correct_answer = str(first_number)
        else:
            question = f"{question} {first_number}"

    return question, correct_answer
