import random

#Calculates and diplays the total for a roll, the average, and all the rolls made
def calculate(numRolls, die):
    sum = 0
    display = []

    for x in range (0,numRolls):
        k = random.randrange(1,die+1)
        display.append(k)
        sum += k

    disadvantage = display[0]
    advantage = display[0]
    for y in range(0, len(display)):
        if display[y] > advantage:
            advantage = display[y]
        elif display[y] < disadvantage:
            disadvantage = display[y]

    for z in range(0, len(display)-1):
        print(str(display[z])+' +'),

    print(str(display[len(display)-1]))
    print("Total: "+ str(sum)),
    print(" Average: "+ str(sum/numRolls)),
    print(" Advantage: " + str(advantage)),
    print(" Disadvantage: " + str(disadvantage))
    return

cont = 'y'

while cont=='y':
    while True:
        #Catch improper input and redirect user to try again
        try:
            roll = raw_input("Enter number of dice and die type (Ex. 3d10): ")
            numRolls, die = roll.split('d')
            numRolls = int(numRolls)
            die = int(die)
        except ValueError:
            print("Improper input, try again.")
            continue
        else:
            #Proper input breaks from while true loop
            break



    if numRolls> 0 and die>0:
        calculate(numRolls, die)
        cont = raw_input("Would you like to roll more dice? [y/n]: ")

    else:
        print("Cannot have a negative input.")
