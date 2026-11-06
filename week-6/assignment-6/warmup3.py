
x = "global variable"

def is_test(y):
    y ="local varible "
#File "/Users/akwasi/python_class/python_homework/python-intro-homework/week-6/assignment-6/warmup3.py", line 4, in <module>
#print(y)   NameError: name 'y' is not defined
#print(y)


def get_variable():
    y = "local variable"
    return y  # Sends the value out of the function

# Assigning the returned value to an outer scope variable
outer_y = get_variable()
print(outer_y)