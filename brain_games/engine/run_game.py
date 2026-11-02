from collections.abc import Callable

import prompt


def run_game(
        description: str,
        game_function: Callable[[], tuple[str, str]]) -> None:
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ', empty=False).strip()
    print(f'Hello, {user_name}!')
    print(description)

    for _ in range(3):
        task, solution = game_function()
        print(f'Question: {task}')
        user_answer = prompt.string('Your answer: ', empty=False).strip()
        if user_answer == solution:
            print('Correct!')
        else:
            print(f"'{user_answer}' is wrong answer ;(.\
                Correct answer was '{solution}'.")
            print(f"Let's try again, {user_name}!")
            break
    else:
        print(f"Congratulations, {user_name}!")
