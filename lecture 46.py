winning_number=27
user_input=int(input("enter"))
if user_input==winning_number:
    print("you win")
else:
    if user_input < winning_number:
        print("too low")
    else:
        print("too high")
