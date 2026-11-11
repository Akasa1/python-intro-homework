#functions for converting celsius to farenheit 
def celsius_to_fahrenheit(c):
    farenheit = (c * 9/5) + 32
    rounded_farenheit = round(farenheit, 1)
    return rounded_farenheit

#functions for converting  farenheit to celsius 
def fahrenheit_to_celsius(f):
    celsius = ((f) - 32) * 5 / 9
    rounded_celsius = round(celsius, 1)
    return rounded_celsius
    
print(f"0°C = {celsius_to_fahrenheit(0)}°F")
print(f"100°C = {celsius_to_fahrenheit(100)}°F")
print(f"72°F = {fahrenheit_to_celsius(72)}°C")