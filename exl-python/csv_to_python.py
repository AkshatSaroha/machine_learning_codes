import csv
import xml.etree.ElementTree as ET
import json

students = []

with open('students.csv', mode='r') as file:
    csv_reader = csv.DictReader(file)

    for row in csv_reader:
        student = {
            'Name': row['Name'],
            'Age': row['Age'],
            'Math': int(row['Math']),
            'Science': int(row['Science']),
            'English': int(row['English'])
        }
        students.append(student)

for student in students:
    for subject in ['Math', 'Science', 'English']:
        student[subject] += 5

root = ET.Element('Students')
for student in students:
    student_elem = ET.SubElement(root, 'Student')
    name_elem = ET.SubElement(student_elem, 'Name')

    clean_name = student['Name'].replace("Mr. ", "").replace("Ms. ", "")
    name_elem.text = clean_name

    age_elem = ET.SubElement(student_elem, 'Age')
    age_elem.text = str(student['Age'])

    marks_elem = ET.SubElement(student_elem, 'Marks')

    for subject in ['Math', 'Science', 'English']:
        subject_elem = ET.SubElement(marks_elem, subject)
        subject_elem.text = str(student[subject])

# Saving the XML to a file
tree = ET.ElementTree(root)
tree.write('students.xml')

# Reading the XML file and converting it to JSON
xml_tree = ET.parse('students.xml')
xml_root = xml_tree.getroot()

students_json_data = []
for student_elem in xml_root.findall('Student'):
    name = student_elem.find('Name').text
    age = int(student_elem.find('Age').text)
    marks = student_elem.find('Marks')

    if name in ["Amit", "Ravi"]:
        name = "Mr. " + name
    elif name in ["Sneha", "Meera"]:
        name = "Ms. " + name

    student_dict = {
        'Name': name,
        'Age': age,
        'Math': int(marks.find('Math').text),
        'Science': int(marks.find('Science').text),
        'English': int(marks.find('English').text)
    }
    students_json_data.append(student_dict)

with open('students.json', 'w') as file:
    json.dump(students_json_data, file, indent=4)