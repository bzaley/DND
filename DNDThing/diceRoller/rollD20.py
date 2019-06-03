cont = 'y'
while cont == 'y':
    while True:
    #Catch improper input and redirect user to try again
        try:
        filepath = raw_input("Give file path to character sheet: ")
        charFile = open(filepath, "rt")
        except ValueError:
        print("File not found!")
        continue
        else:
        #Proper input breaks from while true loop
        break
    print("File Found!")
    pendingRoll = raw_input("Please enter the roll you would like to make: ")

    advDisadv = raw_input("Select if the roll is modified. [Na/Advantage/Disadvantage]: ")
    
