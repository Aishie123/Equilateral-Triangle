def script():

    order = ["first", "second", "third"]
    sides = [] # list for the sides

    for i in range(len(order)):
        while True:
            s = input("Enter the " + order[i] + " side: ")
            try:
                if int(s) > 0:
                    sides.append(int(s)) # adds a side to the list
                    break
                else:
                    print("INVALID INPUT. Please enter a POSITIVE INTEGER.")
                    continue
            except ValueError: 
                print("INVALID INPUT. Please try again.")
                continue

    if len(set(sides)) == 1: # determines whether all elements(sides) from the list are identical
        print("The triangle is equilateral.")
    else:
        print("The triangle is not equilateral.")


    while True:
        restart = input("\nWould you like to restart this program? (y/n)\n")

        if restart == "y":
            print("")
            script()
            break
        if restart == "n":
            print("Script terminating. Goodbye.\n")
            break
        if restart != "y" or restart != "n":
            print("INVALID INPUT. Please try again.\n")
            continue

script()


