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
            return print(answer + " is wrong answer ;(. Correct answer was 'yes'. Let's try again")
        else:
            if number % 2 != 0 and answer == "no":
                print("Correct!")
            else:
                return print(answer + " is wrong answer ;(. Correct answer was 'no'. Let's try again")
        index += 1
    print("Congratulation, " + name + "!")


# calc module
question = "What is the result of the expression?"
number1 = random.randint(1, 100)
number2 = random.randint(1, 100)
operator = random.choice(['+', '-', '*'])
expression = str(number1) + operator + str(number2)
correct_answer = eval(str(number1) + operator + str(number2))


def game():
    index = 0
    name = welcome_user()
    print(question)

    while index < 3:
        print("Question: " + expression)
        answer = prompt.string("Your answer: ")
        if answer == correct_answer:
            print("Correct!")
        else:
            return print(
                answer + " is wrong answer ;(. Correct answer was " + str(correct_answer) + ". Let's try again")
        index += 1
    print("Congratulation, " + name + "!")