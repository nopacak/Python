import sqlite3

sql_query = "SELECT sqlite_version();"

try:
    sql_connection = sqlite3.connect("SQLite_Python_Test.db")
    print("We have connected to the database")

    cursor = sql_connection.cursor()
    cursor.execute(sql_query)
    records = cursor.fetchall()

    print(f"SQLite version: {records}")
    cursor.close()

except sqlite3.Error as error:
    print(f"Error!! - {error}")

finally:
    if sql_connection:
        sql_connection.close()


#--------------------------------------------------------------------------


create_sql_query = """
CREATE TABLE IF NOT EXISTS Employees(
    id INTEGER PRIMARY KEY,
    Name TEXT NOT NULL,
    Email TEXT NOT NULL UNIQUE
);
"""

database_name = "CompanyDB.db"

try:
    sql_connection = sqlite3.connect(database_name)
    cursor = sql_connection.cursor()
    cursor.execute(create_sql_query)
    sql_connection.commit()
    cursor.close()

except sqlite3.Error as error:
    print(f"Error!! - {error}")

finally:
    if sql_connection:
        sql_connection.close()


insert_sql_query = """
INSERT INTO Employees (Name, Email)
VALUES(?,?);
"""  # ? is a placeholder

employee_list = [
     ("Nikolina Opačak", "nikolina@valcon.com"),
     ("Hrvoje Horvat", "hrvoje@email.com"),
     ("Marija Marić", "marija@email.com")
 ]

try:
    sql_connection = sqlite3.connect(database_name)
    cursor = sql_connection.cursor()

    for employee in employee_list:
        cursor.execute(insert_sql_query, employee)
    
    sql_connection.commit()
    cursor.close()

except sqlite3.Error as error:
    print(f"Error!! - {error}")

finally:
    if sql_connection:
        sql_connection.close()
    

select_all_query = "SELECT * FROM Employees"

try:
    sql_connection = sqlite3.connect(database_name)
    cursor = sql_connection.cursor()

    cursor.execute(select_all_query)
    records = cursor.fetchall()

    for record in records:
        print(record)
    
    cursor.close()

except sqlite3.Error as error:
    print(f"Error!! - {error}")

finally:
    if sql_connection:
        sql_connection.close()




update_sql_query = """
UPDATE Employees SET Name = ?, Email = ?
WHERE Id = ?;
"""  


try:
    sql_connection = sqlite3.connect(database_name)
    cursor = sql_connection.cursor()

    cursor.execute(update_sql_query, ("Ana Anić Horvat", "ana.anic.horvat@gmail.com", 2))
    
    sql_connection.commit()
    cursor.close()

except sqlite3.Error as error:
    print(f"Error!! - {error}")

finally:
    if sql_connection:
        sql_connection.close()




delete_sql_query = """
DELETE FROM Employees WHERE Id = ?;
"""  


try:
    sql_connection = sqlite3.connect(database_name)
    cursor = sql_connection.cursor()

    cursor.execute(delete_sql_query, (1,))
    
    sql_connection.commit()
    cursor.close()

except sqlite3.Error as error:
    print(f"Error!! - {error}")

finally:
    if sql_connection:
        sql_connection.close()
