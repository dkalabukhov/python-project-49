import prompt


def welcome_user() -> None:
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ', empty=False)
    print(f'Hello, {name.strip()}!')