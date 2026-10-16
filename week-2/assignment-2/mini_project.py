# requesting user input.
temperature = float (input("What is the temperature in Fahrenheit? "))

# converting the input to Celsius.
celsius = ((temperature) - 32) * 5 / 9
rounded_celsius = round(celsius, 1)

#the output of the conversion.
print(f"The {temperature} in Celsius is: {rounded_celsius}")