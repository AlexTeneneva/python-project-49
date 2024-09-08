import random

QUESTION = "What is the result of the expression"


def get_question_and_answer():
    number1 = random.randint(1, 100)
    number2 = random.randint(1, 100)
    operator = random.choice(['+', '-', '*'])
    expression = f"{number1} {operator} {number2}"
    correct_answer = eval(expression)
    return expression, correct_answer
