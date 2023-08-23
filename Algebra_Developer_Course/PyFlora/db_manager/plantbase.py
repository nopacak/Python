import sqlite3


plant_data = {1:["Daffodil", "assets\\plant_images\\Daffodil.jpeg", "23.1", "15.5", "65", "19.5", False],
              2:["Daisy", "assets\\plant_images\\Daisy.jpeg", "16.5", "12.3", "78", "25.3", False],
              3:["Gladiolus", "assets\\plant_images\\Gladiolus.jpeg", "13.03", "20.6", "25", "32.4", False],
              4:["Lilly", "assets\\plant_images\\Lilly.jpeg", "9.08", "18.9", "16", "22.9", False],
              5:["Magnolia", "assets\\plant_images\\Magnolia.jpeg", "31", "27.5", "80", "14.5", False],
              6:["Orchid", "assets\\plant_images\\Orchid.jpeg", "18.3", "25.3", "100", "34.2", False],
              7:["Peony", "assets\\plant_images\\Peony.jpeg", "3.7", "30.2", "55", "22.7", False],
              8:["Poppy", "assets\\plant_images\\Poppy.jpeg", "10.85", "22.5", "15", "30.5", False],
              9:["Sunflower", "assets\\plant_images\\Sunflower.jpeg", "22.4", "31.7", "100", "35.9", False],
              10:["Violet", "assets\\plant_images\\Violet.jpeg", "4.79", "29.4", "20", "15.4", False]}


def create_connection():
    try:
        connection = sqlite3.connect("PyFlora.db")
        return connection
    except sqlite3.Error as e:
        print(e)
        return None


def create_table():
    connection = create_connection()
    if connection is not None:
        cursor = connection.cursor()
        try:
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS Plants (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    plant_name TEXT UNIQUE,
                    photo TEXT,
                    soil_moisture TEXT,
                    soil_temperature TEXT,
                    brightness TEXT,
                    temperature TEXT,
                    fertilizer BOOL
                );
            """)
            connection.commit()
        except sqlite3.Error as e:
            print(e)
        finally:
            connection.close()


def add_plant(plant_name, photo, soil_moisture, soil_temperature, brightness, temperature, fertilizer):
    connection = create_connection()
    if connection is not None:
        cursor = connection.cursor()
        try: 
            cursor.execute("INSERT INTO Plants (plant_name, photo, soil_moisture, soil_temperature, brightness, temperature, fertilizer) VALUES (?, ?, ?, ?, ?, ?, ?)",
                           (plant_name, photo, soil_moisture, soil_temperature, brightness, temperature, fertilizer))
            connection.commit()
            print("plant added successfully")
        except sqlite3.Error as e:
            print(e)
        finally:
            connection.close()


def get_plant_id(plant_name):
    connection= create_connection()
    if connection is not None:
        cursor = connection.cursor()
        try:
            cursor.execute("SELECT id FROM Plants WHERE plant_name = ?", (plant_name,))
            plant_id = cursor.fetchone()
            if plant_id is not None:
                return plant_id[0]
            else:
                return None
        except sqlite3.Error as e:
            print(e)
        finally:
            connection.close()


def update_plant(plant_id, soil_moisture, soil_temperature, brightness, temperature, fertilizer):
    connection = create_connection()
    if connection is not None:
        cursor = connection.cursor()
        try:
            cursor.execute("""
            UPDATE Plants
            SET soil_moisture = ?, soil_temperature = ?, brightness = ?, temperature = ?, fertilizer = ?
            WHERE id = ?
            """, (soil_moisture, soil_temperature, brightness, temperature, fertilizer, plant_id))
            connection.commit()
            print("Plants updated successfully.")
        except sqlite3.Error as e:
            print(e)
        finally:
            connection.close()


def get_plants():
    connection= create_connection()
    display_rows = []
    if connection is not None:
        cursor = connection.cursor()
        try:
            cursor.execute("SELECT * FROM Plants")
            rows = cursor.fetchall()
            for display_id, row in enumerate (rows, start=1):
                
                display_row = (display_id,) + row
                display_rows.append(display_row)
            
        except sqlite3.Error as e:
            print(e)
        finally:
            connection.close()
    return display_rows


def get_plant_by_id(plant_id):
    connection = create_connection()
    if connection is not None:
        cursor = connection.cursor()
        try:
            cursor.execute("SELECT * FROM Plants WHERE id = ?", (plant_id,))
            plant = cursor.fetchone()
            return plant
        except sqlite3.Error as e:
            print(e)
        finally:
            connection.close()


def delete_plant(plant_id):
    connection = create_connection()
    if connection is not None:
        cursor = connection.cursor()
        try:
            cursor.execute("DELETE FROM Plants WHERE id=?;", (plant_id,))
            connection.commit()
        except sqlite3.Error as e:
            print(e)
        finally:
            connection.close()


def is_plants_table_empty() -> bool:
    """
    Checks if the 'Plants' table in the database is empty.

    Returns:
        bool: True if the table is empty, False otherwise.
    """
    connection = create_connection()
    if connection is not None:
        cursor = connection.cursor()
        try:
            cursor.execute("SELECT COUNT(*) FROM Plants")
            count = cursor.fetchone()[0]
            return count == 0
        except sqlite3.Error as e:
            print(e)
        finally:
            connection.close()


def add_data_if_needed() -> None:
    """
    Adds test data to the 'Plants' table if it is empty.
    """
    if is_plants_table_empty():
        add_plant_data()


def add_plant_data():
    for i in plant_data:
        add_plant(plant_data[i][0], plant_data[i][1], plant_data[i][2], plant_data[i][3], plant_data[i][4], plant_data[i][5], plant_data[i][6])
        i += 1


create_table()
add_data_if_needed()
# for i in plant_data:
#     print(plant_data[i][0], plant_data[i][1], plant_data[i][2], plant_data[i][3], plant_data[i][4], plant_data[i][5], plant_data[i][6])
#     i += 1

