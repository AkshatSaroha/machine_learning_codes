import json

student = { 
    "name": "John",
    "age": 21, 
    "courses": ["Math", "Science"],
    "marks": [90, 85]
}

# Writing into JSON file
with open('student.json', 'w') as file:
    json.dump(student, file)


# Reading from JSON file
with open('student.json', 'r') as file:
    data = json.load(file)

# print(data)

print('====== Student Data =====')
print("Name: ", data['name'])
print("Age: ", data['age'])
print("Courses: ", data['courses'])
print("Marks: ", data['marks'])