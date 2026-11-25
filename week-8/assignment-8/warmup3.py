# This program attempts to read a file named "missing.txt" and handles the case where the file does not exist by catching the FileNotFoundError exception and printing an error message.
try:
    with open("../data/missing.txt", "r") as f:
        content = f.read()
    print("File read successfully.")
except FileNotFoundError:
    print('Error: "missing.txt", was not found. Please check the file path and try again.')
  