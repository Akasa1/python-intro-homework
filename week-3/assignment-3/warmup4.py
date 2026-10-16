# Requesting user input for a number
number = int(input("hi, Enter a number"))

#check if number is positive, negative or zero
if number > 0:
    print(f"{number} : is positive ")
elif number < 0:
    print(f"{number }: is negative ")
else:
    print(f"{number }: is zero ")

#check if number is even or odd 
if number % 2 == 0:
    print (f"{number }: is even")
else:
    print (f"{number }: is odd")
