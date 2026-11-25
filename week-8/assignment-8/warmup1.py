# This program prompts the user to enter a number and checks if the input is a valid number. If the input is not a valid number, it will prompt the user to try again until a valid number is entered.
while True:
  user_num = input("Enter a number: ")
  try:
        #int(user_num)
        num = float(user_num)
        print(f"You entered: { num}") 
        break      
  except ValueError:
        print("That's not a valid number. Try again.")