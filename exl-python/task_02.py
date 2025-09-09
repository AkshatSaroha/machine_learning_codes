import csv
import json
import mysql.connector

def read_and_modify_csv(filename):
    modified_data = []
    with open(filename, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            row['salary'] = int(int(row['salary']) + 10000)  
            modified_data.append(row)
    return modified_data

def store_in_mysql(data):
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='16122003',
        database='exl'
    )
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS employees (
            emp_id INT PRIMARY KEY,
            name VARCHAR(50),
            department VARCHAR(50),
            salary INT
        )
    """)

    for row in data:
        cursor.execute("""
            INSERT INTO employees (emp_id, name, department, salary)
            VALUES (%s, %s, %s, %s)
            ON DUPLICATE KEY UPDATE name=%s, department=%s, salary=%s
        """, (int(row['emp_id']), row['name'], row['department'], int(row['salary']),
              row['name'], row['department'], int(row['salary'])))
    
    connection.commit()
    cursor.close()
    connection.close()

def read_from_mysql():
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='16122003',
        database='exl'
    )
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM employees")
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data

def add_bonus_flag(data):
    for row in data:
        row['eligible_for_bonus'] = row['salary'] >= 55000
    return data

def save_to_json(data, filename='employees_final.json'):
    with open(filename, 'w') as json_file:
        json.dump(data, json_file, indent=4)


if __name__ == "__main__":
    csv_file = 'salary.csv'
    
    modified_data = read_and_modify_csv(csv_file)

    store_in_mysql(modified_data)

    db_data = read_from_mysql()

    final_data = add_bonus_flag(db_data)

    save_to_json(final_data)
