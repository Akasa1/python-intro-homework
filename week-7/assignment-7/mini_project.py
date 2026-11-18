import os
import csv
import datetime

#check if ../data/expenses.csv exists
if os.path.exists("../data/expenses.csv"):
    print("expenses.csv found.")
else:
    print("expenses.csv not found.")
    exit()
    
#read into alist of dictonaries  
expenses = [] 
with open('../data/expenses.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        row['amount'] = float(row['amount'])  # Convert amount to float
        expenses.append(row)  
        
#filter for food expenses and print them       
food_expenses = []
for row in expenses:
    if row["category"].strip() == "Food":
        food_expenses.append(row)
        print(f"{row['date']}: ${row['amount']:.2f}")       

#calculate total food expenses
food_total = 0.0
for row in food_expenses:
    food_total += row["amount"]
print(f"Total: ${food_total:.2f}")

#write report to food_report.txt
today = datetime.datetime.now().strftime("%B %d, %Y")

with open('food_report.txt', 'w') as file:
    file.write(f'Food Expense Report — generated {today}\n')
    for row in food_expenses:
        file.write(f"{row['date']}: ${row['amount']:.2f}\n")
    file.write(f'Total: ${food_total:.2f}\n')