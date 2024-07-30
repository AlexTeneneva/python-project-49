import random

question = 'Answer "yes" if given number is prime. Otherwise answer "no".'
def Check_Prime(n):
    d = 2
    while n % d != 0:
        d += 1
    return d == n


def data ():
    expression = random.randint(1, 100)
    if Check_Prime(expression) == True:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return expression, correct_answer