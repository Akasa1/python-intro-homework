

#this code use the try/ except ZeroDivisionErrorto catch division by zero.
num = float(input ("Enter the numerator: "))
denum = float(input ("Enter the denominator: "))
try:
  result = (num / denum)
  print(f"{num} ÷ {denum} = {result}")
except ZeroDivisionError:
        print("Can't divide by zero — please try a non-zero denominator.")