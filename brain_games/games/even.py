import random
import prompt


def welcome_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def even ():
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
      index+=1
    print("Congratulations, " + name + "!")

def main ():
    even ()

if __name__ == '__main__':
    main()