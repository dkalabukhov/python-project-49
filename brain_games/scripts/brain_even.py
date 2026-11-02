from brain_games.engine.run_game import run_game
from brain_games.games.play_is_even import DESCRIPTION, play_is_even


def main():
    run_game(DESCRIPTION, play_is_even)

if __name__ == 'main':
    main()
