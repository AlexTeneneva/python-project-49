import random
import math


def data():
    question = 'Find the greatest common divisor of given numbers.'
    number1 = random.randint(1, 100)
    number2 = random.randint(1, 100)
    expression = f"{number1} {number2}"
    correct_answer = str(math.gcd(number1, number2))
    return question, expression, correct_answer