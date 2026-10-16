# this is the score file 
#take input from the user on the score 
Score = 88 

#make a decision based on the score and print the grade 
if Score >= 90:
    print(f"Score: {Score}")
    print("Grade: A")
elif Score >= 80:
    print(f"Score: {Score}")
    print("Grade: B")
elif Score >= 70:
    print(f"Score: {Score}")    
    print("Grade: C")
elif Score >= 60:
    print(f"Score: {Score}")
    print("Grade: D")
else:
    print(f"Score: {Score}")
    print("Grade: F")