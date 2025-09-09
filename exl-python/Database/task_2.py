import csv
import json
import mysql.connector

mysqldb = mysql.connector.connect(
        host='localhost',
        user='root',
        password='16122003',
        database='exl'
    )
cursor = mysqldb.cursor()

# Read and modify the CSV file
def read_and_modify_csv(file):
    modified_data = []

    with open('salary.csv', 'r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            row['salary'] = int(int(row['salary']) + 10000) 
            modified_data.append(row)
        return modified_data

# insert modified data into MySQL
# Function to insert one employee record
def insert_employee(id, name, department, salary):
    sql = "INSERT INTO employee (id, name, department, salary) VALUES (%s, %s, %s, %s)"
    values = (id, name, department, salary)
    cursor.execute(sql, values)
    mysqldb.commit()
    print(f"Inserted: {id}, {name}, {department}, {salary}")

# Function to insert all modified employee
def insert_all_employees(data):
    for row in data:
        insert_employee(int(row['id']), row['name'], row['department'], int(row['salary']))

    cursor.close()
    mysqldb.close()


def read_from_mysql():
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='16122003',
        database='exl'
    )
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM employee")
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data

def add_bonus(data):
    for row in data:
        row['eligible_for_bonus'] = row['salary'] >= 55000
    return data

def save_to_json(data, filename='employees_final.json'):
    with open(filename, 'w') as json_file:
        json.dump(data, json_file, indent=4)


if __name__ == "__main__":
    csv_file = 'salary.csv'
    
    modified_data = read_and_modify_csv(csv_file)

    insert_all_employees(modified_data)

    db_data = read_from_mysql()

    final_data = add_bonus(db_data)

    save_to_json(final_data)
