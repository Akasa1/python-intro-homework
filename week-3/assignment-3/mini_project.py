# taking user input for the day of the week and the time of the day.
day_of_week = input("Enter the day of the week! monday, wednesday and friday ").lower()
time_of_day = input ("Enter the time of the day! morning, afternoon and evening ").lower()

# suggestions for Monday.
if day_of_week == "monday" and time_of_day == "morning":
     print(f"Suggestion: cardio training")
elif day_of_week == "monday" and time_of_day == "afternoon":
     print(f"Suggestion: go for Swimming")
elif day_of_week == "monday" and time_of_day == "evening":
     print(f"Suggestion: Outdoor walk for fresh air")

# this is for wednesday
elif day_of_week == "wednesday" and time_of_day == "morning":
     print(f"Suggestion: Bike ride")
elif day_of_week == "wednesday" and time_of_day == "afternoon":
     print(f"Suggestion: Park picnic ")
elif day_of_week == "wednesday" and time_of_day == "evening":
     print(f"Suggestion: Board game night ")

# this is for friday
elif day_of_week == "friday" and time_of_day == "morning":
     print(f"Suggestion: Hiking")
elif day_of_week == "friday" and time_of_day == "afternoon":
     print(f"Suggestion: Beach day")
elif day_of_week == "friday" and time_of_day == "evening":
     print(f"Suggestion: Movie night")
else :
      print("Sorry, I don't recognize that day or time. Try: Monday, Wednesday, Friday and morning, afternoon, evening...")
