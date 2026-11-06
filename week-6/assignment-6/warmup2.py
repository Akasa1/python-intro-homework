#functions for converting celsius to farenheit 
def celsius_to_fahrenheit(c):
    farenheit = (c * 9/5) + 32
    rounded_farenheit = round(farenheit, 1)
    print(f"{c}°C = {rounded_farenheit}°F")
celsius_to_fahrenheit(0)
celsius_to_fahrenheit(100)

#functions for converting  farenheit to celsius 
def fahrenheit_to_celsius(f):
    celsius = ((f) - 32) * 5 / 9
    rounded_celsius = round(celsius, 1)
    print(f"{f}°F = {rounded_celsius}°C")
fahrenheit_to_celsius(72)