#!/usr/bin/env python3

from colorama import Fore
from brain_games.cli import welcome_user

def main():
    print(Fore.GREEN + 'Welcome to the Brain Games!')
    welcome_user()

if __name__ == '__main__':
    main()

