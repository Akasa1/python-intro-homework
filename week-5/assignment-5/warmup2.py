# a while loop that repeatedly asks the user to enter a positive integer
while True:
    try :
        pnum=int(input("Enter a positive integer")) 
        if pnum >0:
            print(f"Got it: {pnum}")
            break 
        else:
            print("That's not a positive integer. Try again.")
    except ValueError:
        print("That's not a positive integer. Try again.")
