from db_manager.db_manager import *

db_file = "Pokemon.db"


create_table_query = """
CREATE TABLE IF NOT EXISTS Pokemons(
    id INTEGER PRIMARY KEY,
    Name TEXT NOT NULL,
    Type TEXT NOT NULL,
    Power REAL NOT NULL
);
"""

insert_into_table_query = """
INSERT INTO Pokemons(Name, Type, Power)
VALUES (?,?,?);
"""

sql_connection = create_connection(db_file)
success = create_table(sql_connection, create_table_query)
if success:
    print("Table successfully created!")
else:
    print("Table hasn't been created")


data = [
    ("Pikachu", "electric", 7.5),
    ("Bulbasaur", "grass", 6.3),
    ("Charizard", "fire", 8.9)
]


success = insert_into_table(sql_connection, insert_into_table_query, data)
if success:
    print("Data successfully imported into the table!")
else: 
    print("Data unsuccessfully imported into the table.")





select_all_query = "SELECT * FROM Pokemons;"
records_from_table = select_all_from_table(sql_connection, select_all_query)
print(f"Fetched data from database: {records_from_table}")


sql_connection.close()
