# input requesting for users age
age = int (input ("What is your age? ")) 

if age >= 0 and not age <= 12:
    print ("You are a child")
elif age >= 13 and age <= 17:
    print("You are a Teen")
elif age >= 18 and age <= 64:
    print("You are an Adult")
else:
    print("You are a Senior")
