from brain_games.engine.run_game import run_game
from brain_games.games.play_progression import DESCRIPTION, play_progression


def main():
    run_game(DESCRIPTION, play_progression)


if __name__ == 'main':
    main()