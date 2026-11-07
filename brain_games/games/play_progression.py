from random import randint

DESCRIPTION = 'What number is missing in the progression?'


def create_progression(elements: int = 10) -> list[str]:
    progression: list[str] = []
    start = randint(-100, 100)
    step = randint(-10, 10)

    for index in range(elements):
        progression.append(str(start + index * step))

    return progression


def play_progression() -> tuple[str, str]:
    progression = create_progression()
    index_to_hide = randint(0, len(progression) - 1)

    hidden_number = progression[index_to_hide]

    progression[index_to_hide] = '..'

    return (
        ' '.join(progression),
        str(hidden_number)
    )