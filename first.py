#doorgame
import random
life = 5
while life > 0:
            b = random.randint(1, 5)
            print(b)
            life = life-1
            a = int(input("enter a number: "))
            if a == b:
                print("you won want to play again")
                c = input("yes or no: ")[0]
                if c == "y":
                    life = 5
                else:
                    life = 0
            else:
                print("wrong guess")

if life == 0:
            print(" game over ")
            #d= input("enter y or n")
            #if c == "y":
            #life = 5