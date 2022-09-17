#!/usr/bin/env python3
from brain_games.logic import launch_game
from brain_games.games import parity_check


def main():
    launch_game(parity_check)


if __name__ == '__main__':
    main()
