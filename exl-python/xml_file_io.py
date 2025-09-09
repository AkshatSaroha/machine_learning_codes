import xml.etree.ElementTree as ET

persons = [
    {'Name': 'Abc', 'Age': 20, 'Gender': 'Male'},
    {'Name': 'Def', 'Age': 22, 'Gender': 'Female'},
    {'Name': 'Ghi', 'Age': 24, 'Gender': 'Male'}
]

root = ET.Element('Persons')

root = ET.Element("Persons")

for p in persons:
    person = ET.SubElement(root, "Person")
    ET.SubElement(person, "Name").text = p["Name"]   
    ET.SubElement(person, "Age").text = str(p["Age"])
    ET.SubElement(person, "Gender").text = p["Gender"]

tree= ET.ElementTree(root)
tree.write("person-data.xml")

print("Data written to XML-data.xml successfully.")