# input requesting for users age
age = int (input ("What is your age "))


if age <= 12:
    print ("You are a child")
elif age <= 17:
    print("You are a Teen")
elif age <= 64:
    print("you are an Adult")
else:
    print("You are a Senior")
