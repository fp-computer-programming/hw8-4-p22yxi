# Yongdong Xi
from random import randint

def rock_paper_scissors():
    win = 0
    lose = 0
    tie = 0
    total = 0
    """Play rock paper scissors""" 
    computer = randint(0, 2) 
    while True: 
        player = input("Enter 0 for rock, 1 for paper, and 2 for scissors: ")
        if int(player) <= 2:
            total += 1
            print(total)
        if int(player) > 2:
            continue
        if player == computer:
            print("It's a tie!")
            tie += 1
            continue
        elif int(player) == 0:
            if computer == 1:
                print("You lose, paper covers rock.\n")
                lose += 1 
            else:
                print("You win, rock crushes scissors!\n")
                win += 1
        elif int(player) == 1:
            if computer == 2:
                print("You lose, scissors cuts paper.\n")
                lose += 1
            else:
                print("You win, paper covers rock!\n")
                win += 1
        elif int(player) == 2:
            if computer == 0:
                print("You lose, rock crushes scissors.\n")
                lose += 1
            else:
                print("You win, scissors cuts paper!\n")
                win += 1
        anotherplay = input("Enter Y if you want to continue the game, and enter N if you want to end the game: ")
        if anotherplay == "Y":
            continue
        if anotherplay == 'N':
            print('You play {3} games totally, win {0} games, lose {1} games and tie {2} games.'.format(win, lose, tie, total))
            break
        

rock_paper_scissors()