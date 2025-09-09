import mysql.connector

# try:
mysqldb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="16122003",
    database="college"
)
#     cursor = mysqldb.cursor()
# except mysql.connector.Error as err:
#     print(f"Error: {err}")

# except Exception as e:
#     print(f"An unexpected error occurred: {e}")

# finally:
#     if mysqldb.is_connected():
#         print('MySQL Connector/Python is installed and working!')
#     else:
#         print('Failed to connect to the database.')

cursor = mysqldb.cursor()
print('MySQL Connector/Python is installed and working!')

def insert_data(name, age, department, percentage):
    sql = "INSERT INTO students (name, age, department, percentage) VALUES (%s, %s, %s, %s)"
    value = (name, age, department, percentage)
    cursor.execute(sql, value)
    mysqldb.commit()
    print(f"Data inserted: {name}, {age}, {department}, {percentage}")

def read_data():
    cursor.execute('SELECT * FROM students')
    result = cursor.fetchall()
    for row in result:
        print('ID:', row[0], 'Name:', row[1], 'Age:', row[2], 'Department:', row[3], 'Percentage:', row[4])

def update_data(name, age, department, percentage):
    sql = "UPDATE students SET age = %s, department = %s, percentage = %s WHERE name = %s"
    value = (age, department, percentage, name)
    cursor.execute(sql, value)
    mysqldb.commit()
    print(f"Data updated: {name}, {age}, {department}, {percentage}")

def delete_data(name):
    sql = "DELETE FROM students WHERE name = %s"
    value = (name,)
    cursor.execute(sql, value)
    mysqldb.commit()
    print(f"Data deleted: {name}")

def search_data(name):
    sql = "SELECT * FROM students WHERE name = %s"
    value = (name,)
    cursor.execute(sql, value)
    result = cursor.fetchall()
    if result:
        for row in result:
            print('ID:', row[0], 'Name:', row[1], 'Age:', row[2], 'Department:', row[3], 'Percentage:', row[4])
    else:
        print(f"No data found for name: {name}")

insert_data("Alice", 20, "Computer Science", 85.5)
insert_data("Bob", 22, "Mathematics", 90.0)
insert_data("Charlie", 21, "Physics", 88.0)
insert_data("David", 23, "Chemistry", 92.0)
print("Reading data from database:")
read_data()

update_data("Alice", 29, "AI / ML", 90.0)
delete_data("Bob")

print('\nAfter update and delete operations:')
read_data()

print('\nSearching for Charlie:')
search_data("Charlie")



cursor.close()
mysqldb.close()
print("Database connection closed.")