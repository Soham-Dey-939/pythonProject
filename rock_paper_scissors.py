import random


def check(cmp, ply):
    if ply > 2:
        print("Invalid input!")
    else:
        if cmp == 0 and ply == 0 or cmp == 1 and ply == 1 or cmp == 2 and ply == 2:
            print("Its a tie!")
        elif ply == 0 and cmp == 2 or ply == 1 and cmp == 0 or ply == 2 and cmp == 1:
            print("You win!")
        else:
            print("You lose!")


if __name__ == "__main__":
    player = int(input(f"Enter 0 for rock 1 for paper and 2 for scissors -> \n"))
    comp = random.randint(0, 2)
    print(comp)
    check(comp, player)
