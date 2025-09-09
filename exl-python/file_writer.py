import csv

persons = [
    ['Abc', 20, 'Male'],
    ['Def', 21, 'Male'],
    ['Ghi', 22, 'Female']
]

with open('data.csv', mode='w', newline='') as file:
    writer1 = csv.writer(file)
    writer1.writerow(persons)
    print(persons)

with open('data.csv', mode='a', newline='') as file:
    writer1 = csv.writer(file)
    writer1.writerow(persons)
    print(persons)

with open('data_02.csv', mode='x', newline='') as file:
    writer1 = csv.writer(file)
    writer1.writerow(persons)
    print(persons)

with open('data.csv', mode='r+', newline='') as file:
    writer1 = csv.writer(file)
    file.seek(0, 2) # Move cursor to the end of the file
    writer1.writerow(['Xyz', 25, 'Male'])
    print('New data added to data.csv')

    reader = csv.reader(file)
    for row in reader:
        print(row)

# Mode 1 --> r - To Read Data
# Mode 2 --> w - To Write Data
# Mode 3 --> a - To Append Data
# Mode 4 --> x - To Create a New File
# Mode 5 --> r+ - read and write together