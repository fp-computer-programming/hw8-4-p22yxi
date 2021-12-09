from random import randint


def rock_paper_scissors():
    """Play rock paper scissors""" 
    computer = randint(0, 2) 
    while True: 
        player = int(input("Enter 0 for rock, 1 for paper, and 2 for scissors: "))
        if player > 2:
            continue   
        if player == computer:
            print("It's a tie!")
            return "tie"
        elif player == 0:
            if computer == 1:
                print("You lose, paper covers rock.\n")
                return "loss"
            else:
                print("You win, rock crushes scissors!\n")
                return "win"
        elif player == 1:
            if computer == 2:
                print("You lose, scissors cuts paper.\n")
                return "loss"
            else:
                print("You win, paper covers rock!\n")
                return "win"
        elif player == 2:
            if computer == 0:
                print("You lose, rock crushes scissors.\n")
                return "loss"
            else:
                print("You win, scissors cuts paper!\n")
                return "win"


rock_paper_scissors()