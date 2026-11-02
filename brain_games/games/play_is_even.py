from random import randint


DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'

def play_is_even() -> tuple[str, str]:
    random_number = randint(1, 100)
    solution = 'yes' if random_number % 2 == 0 else 'no'

    return (str(random_number), solution)

