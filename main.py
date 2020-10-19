<<<<<<< HEAD
import os
import time

x1Done = False
y1Done = False
x2Done = False
y2Done = False
undefined = False
imported = False
point1 = []
point2 = []

def clear_screen():
    os.system('clear')


while True:
    # gets integers from users
    if imported == False:
        x1 = False
        y1 = False
        x2 = False
        y2 = False

        #finding the first point of x
        while x1Done is False:
            x1 = input("Insert the x of the first point \n")
            try:
                int(x1)
                x1Done = True
            except ValueError:
                try:
                    float(x1)
                    x1Done = True
                except ValueError:
                    print("not an integer. please try again \n")
                    x1Done = False
                    time.sleep(2)
                    clear_screen()
        #finding the first point of y
        while y1Done is False:
            y1 = input("Insert the y of the first point \n")
            try:
                int(x1)
                y1Done = True
            except ValueError:
                try:
                    float(y1)
                    y1Done = True
                except ValueError:
                    print("not an integer. please try again \n")
                    y1Done = False
                    time.sleep(2)
                    clear_screen()
        #appends the variables to array 
        point1.append(x1)
        point1.append(y1)
        print("First point: ", point1, "\n")

        #finding the second point of x 
        while x2Done is False:
            x2 = input("Insert the x of the second point\n")
            try:
                int(x2)
                x2Done = True
            except ValueError:
                try:
                    float(x2)
                    x2Done = True
                except ValueError:
                    print("not an integer. please try again")
                    x2Done = False
                    time.sleep(2)
                    clear_screen()
        #finding the second point of y
        while y2Done is False:
            y2 = input("Insert the y of the second point \n")
            try:
                int(y2)
                y2Done = True
            except ValueError:
                try:
                    float(y2)
                    y2Done = True
                except ValueError:
                    print("not an integer. please try again")
                    y2Done = False
                    time.sleep(2)
                    clear_screen()
        #appends the variables to array 
        point2.append(x2)
        point2.append(y2)
        print("Second point: ", point2, "\n")
        time.sleep(3)
        clear_screen()
        imported = True

    #program to make a better environment 
    print("Line: ", point1, point2)
    try:
        command = input("What would you like to do? type 'help' to get help \n")
    except KeyboardInterrupt:
        command = input("What would you like to do? type 'help' to get help \n")
    #input solve to solve 
    if command == "solve" or command == "Solve":
        try:
            numerator = int(point2[1]) - int(point1[1])
        except ValueError:
            numerator = float(point2[1]) - float(point1[1])

        if numerator == 0:
            pass

        #defining if there are decimals or not 
        try:
            denominator = int(point2[0]) - int(point1[0])
        except ValueError:
            denominator = float(point2[0]) - float(point1[0])

        #defining if there is 0 or -1 in denominator 
        if denominator == 0:
            undefined = True
        elif denominator < 0:
            denominator *= -1
            numerator *= -1

        print("Result: ", numerator, " / ", denominator)
        print("Undefined: ", undefined, "\n")
    #input for resetting the points 
    elif command == "new" or command == "New":
        imported = False
        point1.remove(x1)
        point1.remove(y1)
        point2.remove(x2)
        point2.remove(y2)
        x1Done = False
        y1Done = False
        x2Done = False
        y2Done = False
        print("Points Reset \n")
    elif command == "help" or command == "Help": #input for help
        print("commands:")
        print("Solve | solves and finds the answer for slope")
        print("New | clears the points and put new input")
        print("Help | ;) \n")
    elif command == "exit" or command == "Exit": #input for exiting the program
        break
    else:
        print("invalid input. please try again.")
        #put this at else in case someone exits by accident 
=======
>>>>>>> parent of 621a94f... added new things
