# taking user input for their score
score = int(input("Enter your score from 0 -100 "))

def is_valid_score(score):
     if score < 0:
         return False
     elif score >100: 
        return False
     else:
          return True
if is_valid_score(score):
 print("Valid score.")
else:
 print("Invalid score — must be between 0 and 100.")  
