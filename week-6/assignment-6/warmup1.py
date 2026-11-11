#function that takes 2 Parameters
def greet(name, greeting="Hello"):
    print( f"{greeting}, {name}!")

greet("Aka")
greet("Aka", "Good morning")
greet("Aka", greeting = "Hi")