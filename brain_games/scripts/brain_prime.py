from brain_games.engine.run_game import run_game
from brain_games.games.play_is_prime import DESCRIPTION, play_is_prime


def main():
    run_game(DESCRIPTION, play_is_prime)


if __name__ == 'main':
    main()