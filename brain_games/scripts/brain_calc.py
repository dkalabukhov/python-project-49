from brain_games.engine.run_game import run_game
from brain_games.games.play_calc import DESCRIPTION, play_calc


def main():
    run_game(DESCRIPTION, play_calc)


if __name__ == 'main':
    main()