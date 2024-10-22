#rock, paper, scissor
import random
options=("rock","paper","scissor")
running=True

while running:
    players=None
    computer=random.choice(options)

    while players not in options:
        players=input("enter a choice(rock,paper,scissor):")
        print(f"players:{players}")
        print(f"computer:{computer}")
        if players==computer:
            print("it's a tie!")
        elif players=="rock" and computer=="scissor":
            print("you win!")

        elif players=="paper"and computer=="rock":
            print("you win")
        elif players=="scissor" and computer=="paper":
            print("you win")
        else:
            print("you lose!")
            if not input("play again ?(y/n):").lower()=="y":
                running=False

                print("thank you!")









                         

                           
