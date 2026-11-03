from random import randint

DESCRIPTION = 'What is the result of the expression?'


def play_calc() -> tuple[str, str]:
    random_number1 = randint(1, 100)
    random_number2 = randint(1, 100)
    operators = ('+', '-', '*')

    operator = operators[randint(0, len(operators) - 1)]
    match operator:
        case '+':
            return (
                f'{random_number1} + {random_number2}',
                str(random_number1 + random_number2)
            )
        case '-':
            return (
                f'{random_number1} - {random_number2}',
                str(random_number1 - random_number2)
            )
        case '*':
            return (
                f'{random_number1} * {random_number2}',
                str(random_number1 * random_number2)
            )