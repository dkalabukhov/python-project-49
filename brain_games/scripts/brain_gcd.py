from brain_games.engine.run_game import run_game
from brain_games.games.play_gcd import DESRIPTION, play_gcd


def main():
    run_game(DESRIPTION, play_gcd)


if __name__ == 'main':
    main()