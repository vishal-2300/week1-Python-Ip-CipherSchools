#import random
#winning_number=random.randint(2,20)
winning_number=25
guess=int(input("enter no"))
if winning_number==guess:
    print("you won")
else:
    if guess>winning_number:
        print("to high")
    if guess<winning_number:
        print("to low")

