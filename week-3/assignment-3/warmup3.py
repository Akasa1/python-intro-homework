# Python reads this as:
print (not True and False) #False  Not True becomes False, then False and False is False

print(True or False and False) #True  False and False happens first and becomes False,then, True or False is true
 
print(not (5 > 3)) #False (5 > 3) is True, True and Not is  false
 
print(10 == 10 and 4 != 4) #False  (10 == 10) is True,  and (4!=4)is False, True and False is False

print(not False or not True) #True  Not False is True, Not True is False, True or False is True
