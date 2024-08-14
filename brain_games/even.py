import random
import prompt


def welcome_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def even():
    index = 0
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')

    while index < 3:
        number = random.randint(1, 100)
        print("Question: " + str(number))
        answer = input("Your answer: ")
        if number % 2 == 0 and answer == "yes":
            print("Correct!")
        elif number % 2 == 0 and answer != "yes":
            return print(
                f"{answer} is wrong answer ;(."
                f" Correct answer was 'yes'."
                f" Let's try again, {name}!")
        else:
            if number % 2 != 0 and answer == "no":
                print("Correct!")
            else:
                return print(
                    f"{answer} is wrong answer ;(."
                    f" Correct answer was 'yes'."
                    f" Let's try again, {name}!")
        index += 1
    print("Congratulations, " + name + "!")
