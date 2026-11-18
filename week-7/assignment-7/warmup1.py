    
with open('../data/notes.txt', 'r') as file:
    content = file.read()  # Read the entire file as one string
    for number,line in enumerate(content.splitlines(), start=1):
         print(f"Line {number}: {line.strip()}") 
      
        