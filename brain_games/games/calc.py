import random

def data():
    number1 = random.randint(1, 100)
    number2 = random.randint(1, 100)
    operator = random.choice(['+', '-', '*'])
    expression = f"{number1} {operator} {number2}"
    correct_answer = eval(expression)
    question = "What is the result of the expression"
    return expression, correct_answer, question