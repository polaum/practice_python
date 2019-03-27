import random

options = {"Rock": 1, "Paper": 2, "Scissors": 3}


class SameChoiceException(Exception):
    pass


def choose_winner(my_choice):
    winner = ''
    cmp_choice = int(random.randint(1, len(options)))
    print(cmp_choice)
    if my_choice == cmp_choice:
        raise SameChoiceException("It's a Tie!")
    elif my_choice == 1 and cmp_choice == 2:
        winner = 'Computer'
    elif my_choice == 1 and cmp_choice == 3:
        winner = 'You'
    elif my_choice == 2 and cmp_choice == 1:
        winner = 'You'
    elif my_choice == 2 and cmp_choice == 3:
        winner = 'Computer'
    elif my_choice == 3 and cmp_choice == 1:
        winner = 'Computer'
    elif my_choice == 3 and cmp_choice == 2:
        winner = 'You'
    return winner


def play():
    while True:
        choice = input("Welcome to Rock, Paper and Scissors game! \n"
                       "Choose one of the options: \n"
                       "1. Rock \n"
                       "2. Paper \n"
                       "3. Scissors \n"
                        "To quit, type \"quit\" \n")
        if choice == 'quit':
            break
        else:
            winner = choose_winner(int(choice))
            print(f"The winner is: {winner}")


play()