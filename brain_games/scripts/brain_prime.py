#!/usr/bin/env python3

import random
from brain_games.game import game_engine
from brain_games.games import prime


def main():
    game_engine(prime)


if __name__ == '__main__':
    main()