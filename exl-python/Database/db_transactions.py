import mysql.connector
 
try:
    mysqldb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="16122003",  # replace with your MySQL password
        database="exl"
    )
    cursor = mysqldb.cursor()
   
   
    # sql = "UPDATE person SET gfdsuh = %s WHERE id = %s"
    # update_values  = (999, 3)  # Example values for age and id
    # cursor.execute(sql, update_values)
   
    # sql_insert = "INSERT INTO person (name, age) VALUES (%s, %s)"
    # insert_values = ("qwert", 35)  # Example values for name and age
    # cursor.execute(sql_insert, insert_values)
   
    sql = "SELECT * FROM person WHERE id = %s"
    cursor.execute(sql, (13,))  # Example id to fetch
    result = cursor.fetchall()
    for row in result:
        print("ID:", row[0], "Name:", row[1], "Age:", row[2])
       
   
    mysqldb.commit()
    print("Data updated and inserted successfully.")
except mysql.connector.Error as err:
    print(f"=====> Error: {err}")
    mysqldb.rollback()
except Exception as e:
    print(f"=====> An unexpected error occurred: {e}")
    mysqldb.rollback()
finally:
    print("Attempting to close the database connection...")
    if mysqldb.is_connected():
        cursor.close()
        mysqldb.close()
        print("Database connection closed.")
       
print("===> Script executed successfully.")
 