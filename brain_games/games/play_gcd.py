from random import randint


DESRIPTION = 'Find the greatest common divisor of given numbers.'

def find_gcd(num_a: int, num_b: int) -> int:
    if (num_b == 0):
        return num_a
    else:
        return find_gcd(num_b, num_a % num_b)


def play_gcd() -> tuple[str, str]:
    random_number1 = randint(1, 100)
    random_number2 = randint(1, 100)

    return (
        f"{random_number1} {random_number2}",
        f"{find_gcd(random_number1, random_number2)}"
    )
