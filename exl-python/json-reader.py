import json

# with open('person_1.json', 'r') as file:
#     data = json.load(file)
#     print(data)

person_2 = {"name": "saroha", "age": 25, "gender": "male"}

with open('person_2.json', 'w') as file:
    json.dump(person_2, file)

print('Json data posted')