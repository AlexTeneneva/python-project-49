import prompt

round_count = 3


def welcome_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def game_engine(game):
    name = welcome_user()
    print(game.QUESTION)
    for _ in range(round_count):
        expression, correct_answer = game.get_question_and_answer()
        print(f"{'Question'}: {expression}")
        answer = prompt.string("Your answer: ")
        if answer != str(correct_answer):
            print(
                f"{answer} is wrong answer ;(."
                f" Correct answer was {correct_answer}."
                f" Let's try again, {name}!")
            break
        print("Correct!")
    else:
        print(f"Congratulations, {name}!")
