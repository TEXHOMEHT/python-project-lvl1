from brain_games.cli import welcome_user
from colorama import Fore


def greet():
    print(Fore.GREEN + 'Welcome to the Brain Games!')  # Greet player


def launch_game(game):
    greet()
    name = welcome_user()
    print(game.DESCRIPTION)  # Неособо понял, что это и как оно работает.
    i = 0  # Count of the game rounds
    while True:
        question, correct_answer = game.generate_question_answer()
        print(question, end='')
        user_answer = input('\nYour answer: ')  # Asking player's answer
        if user_answer == str(correct_answer):  # Player's answer is correct
            print('Correct!')
            i += 1
        else:  # Player's answer is incorrect
            print(f"'{user_answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'."
                  f"\nLet's try again, {name}!")
            break
        if i == 3:
            print(f'Congratulations, {name}!')
            break
