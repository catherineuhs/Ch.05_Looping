'''
CAMEL GAME
----------
The pseudo-code for how to code this game is in Chapter 5 of the Python Jedi book

'''
done = False
miles_traveled = 0
thirst = 0
camel_tiredness = 0
natives_travel = -20
drinks_in_canteen = 5
import random
natives_movement = random.randrange(7, 15)
camel_fullspeed = random.randrange(10, 21)
tiredness_from_fullspeed_run = random.randrange(1, 6)
camel_forward = random.randrange(5, 13)
print("Ride your camel accross the desert while being chased. You need to manage your thirst, how tired the camel is, and how far ahead of the natives you are.")
while not done:
    print("\n \nChoose an option: ")
    print("A. Drink from your canteen.")
    print("B. Ahead moderate speed.")
    print("C. Ahead full speed.")
    print("D. Stop for the night.")
    print("E. Status check.")
    print("F. Quit.")
    choice = input( "\n Option: ")
    if choice.lower() == "f": #why doesnt this work :I
        print("You've chosen to quit.")
        done = True
    elif choice.lower() == "e":
        print("Miles traveled:", miles_traveled)
        print("Drinks in canteen:", drinks_in_canteen)
        print("The natives are", natives_travel, "miles behind you.")
    elif choice.lower() == "d":
        camel_tiredness = 0
        print("the camel is happy :)!")
        natives_travel = natives_travel + natives_movement
    elif choice.lower() == "c":
        miles_traveled = miles_traveled + camel_fullspeed
        print("you have traveled", miles_traveled, "miles")
        thirst = thirst + 1
        camel_tiredness = camel_tiredness + tiredness_from_fullspeed_run
        natives_travel = natives_travel + natives_movement
    elif choice.lower() == "b":
        miles_traveled = miles_traveled + camel_forward
        print("you have traveled", miles_traveled, "miles")
        thirst = thirst + 1
        camel_tiredness = camel_tiredness + 1
        natives_travel = natives_travel + natives_movement
    elif choice.lower() == "a":
        if drinks_in_canteen > 0:
            drinks_from_canteen = drinks_in_canteen - 1
            thirst = 0
        else:
            print("Error. No drinks left!")
    if not done and thirst > 4:
        print("You are thirsty.")
    elif not done and thirst > 6:
        print("You died of thirst!")
        done = True
    if not done and camel_tiredness > 5:
        print("Your camel is getting tired.")
    elif not done and camel_tiredness > 8:
        "Your camel is dead :,("
        done = True
    if (miles_traveled-natives_travel) == 0:
        print("The natives have caught you.")
        done = True
    elif (miles_traveled-natives_travel) <= 15: ##is this right? step 21##
        print("The natives are getting close!")
    if miles_traveled >= 200:
        print("You won!")
        done = True
