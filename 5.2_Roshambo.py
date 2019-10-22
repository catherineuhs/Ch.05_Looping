'''
ROSHAMBO PROGRAM
----------------

Create a program that randomly prints 1, 2, or 3.
Expand the program so it randomly prints rock, paper, or scissors using if statements. Don't select from a list.
Add to the program so it first asks the user their choice as well as if they want to quit.
(It will be easier if you have them enter 1 for rock, 2 for paper, and 3 for scissors.)
Add conditional statements to figure out who wins and keep the records
When the user quits print a win/loss record

'''

losses = 0
wins = 0
done = False
while not done:
    answer = int(input("rock(1), paper(2), or scissors(3)? press 4 to quit."))
    import random
    hand = random.randrange(1, 4)
    if answer == 4:
        print("you've chosen to quit. wins:", wins, "losses:", losses)
        done = True
    elif answer == hand:
        print("you got a tie")
    elif answer == 1 and hand == 2:
        print("you lose")
        losses = losses + 1
    elif answer == 1 and hand == 3:
        print("you win")
        wins = wins + 1
    elif answer == 2 and hand == 1:
        print("you win")
        wins = wins + 1
    elif answer == 2 and hand == 3:
        print("you lose")
        losses = losses + 1
    elif answer == 3 and hand == 1:
        print("you lose")
        losses = losses + 1
    elif answer == 3 and hand == 2:
        print("you win")
        wins = wins + 1





