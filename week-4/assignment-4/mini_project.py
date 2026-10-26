# Online Python - IDE, Editor, Compiler, Interpreter
students = [
    { "name" : "Jazmine" , "score" : 88 , "subject" : "Python" } ,
    { "name" : "Luis" , "score" : 74 , "subject" : "Data" } ,
    { "name" : "Sara" , "score" : 91 , "subject" : "Python" } ,
    { "name" : "Marcus" , "score" : 68 , "subject" : "Web" } ,
    { "name" : "Priya" , "score" : 95 , "subject" : "Data" } ,
    { "name" : "Devon" , "score" : 72 , "subject" : "Python" } ,
    { "name" : "Mia" , "score" : 83 , "subject" : "Web" } ,
    { "name" : "Eli" , "score" : 79 , "subject" : "Data" } ,
]

max_score = 0
max_score_name = ""
total = 0

# 1 & 2. Find top scorer and accumulate total score inside the loop
for score in students:
    if score["score"] > max_score:
        max_score = score["score"]
        max_score_name = score["name"]
    total += score["score"]

# Calculate average of students
average = total / len(students)

print(f"Top scorer: {max_score_name} ({max_score})")
print(f"Class average: {average}")

# 3. Unique Subjects offered using a set as required
new_subject = set()
for subjects in students:
    new_subject.add(subjects["subject"])
    
print(f"Subjects offered: {{ {', '.join(f"'{sub}'" for sub in new_subject)} }}")

# 4. Find all students with high score 
high_scorers = []
for student in students:
    if student["score"] > 75:
        high_scorers.append(student["name"])

print(f"High scorers: {high_scorers}")