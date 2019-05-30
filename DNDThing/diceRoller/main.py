import random

def calculate(numRolls, die):
    sum = 0
    display = []
    for x in range (0,numRolls):
        k = random.randrange(1,die+1)
        display.append(k)
        sum += k
    for y in range(0, len(display)-1):
        print(str(display[y])+' +'),

    print(str(display[len(display)-1]))
    print("Total: "+ str(sum)),
    print(" Average: "+ str(sum/numRolls))
    return

cont = 'y'

while cont=='y':
    while True:
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
