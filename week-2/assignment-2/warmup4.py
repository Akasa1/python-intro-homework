
"""
# Staff_name =input("what is your name?")
# print( "Hi, " + Staff_namee, "You are welcome to our team!" )

# this is the error message what is your name?Akwasi
#Traceback (most recent call last):
  File "/Users/akwasi/python_class/python_homework/python-intro-homework/week-2/assignment-2/warmup4.py", line 2, in <module>
# print( "Hi, " + Staff_namee, "You are welcome to our team!" )                  ^^^^^
# NameError: name 'Staff_namee' is not defined. Did you mean: 'Staff_name'?

#the cause of the error is that I used namee instead of name. I will fix it by changing namee to name.
"""

# here is the fixed code:
Staff_name = input("What is your name? ")
print(f"Hi, {Staff_name}, you are welcome to our team!")