import os
print(os.getcwd()) # /Users/akwasi/python_class/python_homework/python-intro-homework/week-7/data

#check if ../data/expenses.csv exists
if os.path.exists("../data/expenses.csv"):
    print("expenses.csv found.")
else:
    print("expenses.csv not found.")

#print the path to expenses.csv
path = os.path.join("..", "data", "expenses.csv")
print(path)


