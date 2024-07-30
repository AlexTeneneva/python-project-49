import random
import math

question = 'Find the greatest common divisor of given numbers.'
def data():
    number1 = random.randint(1, 100)
    number2 = random.randint(1, 100)
    expression = f"{number1} {number2}"
    correct_answer = str(math.gcd(number1, number2))
    return expression, correct_answer