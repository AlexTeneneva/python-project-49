import prompt


def welcome_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def game_engine(game):
    name = welcome_user()
    index = 0
    print(game.question)
    while index < 3:
        expression, correct_answer = game.data()
        print(f"{'Question'}: {expression}")
        answer = prompt.string("Your answer: ")
        if answer == str(correct_answer):
            print("Correct!")
        else:
            print(
                f"{answer} is wrong answer ;(."
                f" Correct answer was 'yes'."
                f" Let's try again, {name}!")
            return
        index += 1
    print(f"Congratulations, {name}!")
