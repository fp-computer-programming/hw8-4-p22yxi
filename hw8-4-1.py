# Yongdong Xi

import random
number = random.randint(1, 100)

while True:
    guess = input('what number do you guess? ')
    if guess == 'stop':
        print("the anwser is {0}". format(number))
        break
    if number > int(guess):
        print('Your number is less than the answer')
        continue
    if number < int(guess):
        print('Your number is bigger than the answer')
        continue
    if number == int(guess):
        print("Yeah, you are right")
    break

