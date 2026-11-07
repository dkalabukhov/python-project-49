from math import sqrt
from random import randint

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(num: int) -> bool:
    if num < 2:
        return False
    for i in range(2, int(sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


def play_is_prime() -> tuple[str, str]:
    random_number = randint(1, 100)
    return (
        str(random_number),
        'yes' if is_prime(random_number) else 'no'
    )

