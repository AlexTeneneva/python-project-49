import random

question = 'What number is missing in the progression?'


def create_progression(start, step, length):
    progression = []
    for _i in range(length):
        progression.append(str(start))
        start += step
    return progression


def data():
    start = random.randint(1, 99)
    step = random.randint(1, 10)
    length = random.randint(8, 10)
    progression = create_progression(start, step, length)
    hide_symbol_index = random.randint(0, len(progression) - 1)
    correct_answer = progression.pop(hide_symbol_index)
    progression.insert(hide_symbol_index, '..')
    expression = ' '.join(progression)

    return expression, correct_answer
