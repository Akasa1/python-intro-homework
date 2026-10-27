# hardcoded dictionary representing a student
student = {"name": "Aka", "grade": "A", "subjects": ["Maths"]}
for key, value in student.items():
    print(key, value)

# add a new key 
student["graduated"]= False
for key, value in student.items():
    print(key, value)  