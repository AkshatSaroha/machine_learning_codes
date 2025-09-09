import mysql.connector

mysqldb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="16122003",
    database="exl"
)

cursor = mysqldb.cursor()
print('MySQL Connector/Python is installed and working!')

def insert_data(name, age):
    sql = "INSERT INTO person (name, age) VALUES (%s, %s)"
    value = (name, age)
    cursor.execute(sql, value)
    mysqldb.commit()
    print(f"Data inserted: {name}, {age}")

def read_data():
    cursor.execute('SELECT * FROM person')
    result = cursor.fetchall()
    for row in result:
        print('ID:', row[0], 'Name:', row[1], 'Age:', row[2])


def update_data(name, age):
    sql = "UPDATE person SET age = %s WHERE name = %s"
    value = (age, name)
    cursor.execute(sql, value)
    mysqldb.commit()
    print(f"Data updated: {name}, {age}")

def delete_data(name):
    sql = "DELETE FROM person WHERE name = %s"
    value = (name,)
    cursor.execute(sql, value)
    mysqldb.commit()
    print(f"Data deleted: {name}")


# insert_data("Akshat", 21)
# insert_data("John", 22)
# insert_data('Harry Potter', 20)
# print("Reading data from database:")

print('Before update and delete operations:')
read_data()

update_data("Akshat", 25)
delete_data("John")

print('After update and delete operations:')
read_data()

cursor.close()
mysqldb.close()
print("Database connection closed.")