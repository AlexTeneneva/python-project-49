import random

QUESTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def check_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def get_question_and_answer():
    expression = random.randint(1, 100)
    correct_answer = 'yes' if check_prime(expression) else 'no'
    return expression, correct_answer
