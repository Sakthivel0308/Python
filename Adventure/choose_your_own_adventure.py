name = input("Type your Name: ")
print("welcome", name,"to this adventure")

answer = input("Yor are on a dirt road, it has come to an end and you can go left or right. Which way would you like to go? ").lower()

if answer == "left":
    answer = input("you come to an river, you can walk around it or swim across. Type walk to walk around and swim to swim across: ").lower()
    if answer == "swim":
        print("You swim across and were eaten by an alligator.")
    elif answer == "walk":
        print("you walked for many miles, ran out of water and ypu lost the game.")
    else:
        print("Not a valid option. You Loss")
elif answer == "right":
    answer = input("you come to a bridge, it looks wobble, do you want to cross it or head back (cross/back)? ").lower()
    if answer == "back":
        print("You go back and loos")
    elif answer == "cross":
        answer = input("you cross the bridge and meet a strange. Do you talk to them or not? (yes/no) ").lower()
        if answer == "yes":
            print("you talk to the stranger, the give you a gold. You Win!")
        elif answer == "no":
            print("you ignore the stranger. they are offended. You loos ")
        else:
            print("not a valid option. You loss")
    else:
        print("Not a valid option. You Loss")
    print()
else:
    print("Not a valid answer. You loos")

print("Thank you", name)