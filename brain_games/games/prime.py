import random

question = 'Answer "yes" if given number is prime. Otherwise answer "no".'
def Check_Prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def data():
    expression = random.randint(1, 100)
    correct_answer = 'yes' if Check_Prime(expression) else 'no'
    return expression, correct_answer


# if Check_Prime(expression):
#    correct_answer = 'yes'
#else:
#    correct_answer = 'no'