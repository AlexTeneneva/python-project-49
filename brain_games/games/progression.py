import random

QUESTION = 'What number is missing in the progression?'


def get_question_and_answer():
    start = random.randint(1, 99)
    step = random.randint(1, 10)
    length = random.randint(8, 10)
    stop = start + step * length
    progression = list(range(start, stop, step))
    hide_symbol_index = random.randrange(length)
    correct_answer, progression[hide_symbol_index] = (
        progression[hide_symbol_index], '..')
    expression = ' '.join([str(x) for x in progression])

    return expression, correct_answer
