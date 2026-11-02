import prompt


def welcome_user() -> None:
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ', empty=False).strip()
    print(f'Hello, {user_name}!')