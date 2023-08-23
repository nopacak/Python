import sqlite3

def create_connection():
    try:
        connection = sqlite3.connect("PyFlora.db")
        return connection
    except sqlite3.Error as e:
        print(e)
        return None
    
def create_pots_table():
    connection = create_connection()
    if connection is not None:
        cursor = connection.cursor()
        try:
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS Pots (
                    id INTEGER PRIMARY KEY,
                    material TEXT,
                    placement TEXT,
                    size INTEGER,
                    plant_id INTEGER,
                    FOREIGN KEY (plant_id) REFERENCES Plants(id)
                );
            """)
            connection.commit()
        except sqlite3.Error as e:
            print(e)
        finally:
            connection.close()


def add_pot(material, placement, size, plant_id=None):
    connection = create_connection()
    if connection is not None:
        cursor = connection.cursor()
        try: 
            cursor.execute("INSERT INTO Pots (material, placement, size, plant_id) VALUES (?, ?, ?, ?)",
                           (material, placement, size, plant_id))
            connection.commit()
            print("Pot added successfully")
        except sqlite3.Error as e:
            print(e)
        finally:
            connection.close()


def get_pots():
    connection = create_connection()
    display_rows = []
    if connection is not None:
        cursor = connection.cursor()
        try:
            cursor.execute("""
                SELECT Pots.id, Pots.material, Pots.placement, Pots.size, Plants.id, Plants.plant_name, Plants.photo
                FROM Pots
                LEFT JOIN Plants ON Pots.plant_id = Plants.id;
            """)
            rows = cursor.fetchall()
            if rows is not None:  # Check if rows is not None before trying to enumerate
                for display_id, row in enumerate(rows, start=1):
                    display_row = (display_id,) + row
                    display_rows.append(display_row)
        except sqlite3.Error as e:
            print(e)
        finally:
            connection.close()
    return display_rows



def get_pot_by_id(pot_id):
    connection = create_connection()
    if connection is not None:
        cursor = connection.cursor()
        try:
            cursor.execute("SELECT * FROM Pots WHERE id = ?", (pot_id,))
            plant = cursor.fetchone()
            return plant
        except sqlite3.Error as e:
            print(e)
        finally:
            connection.close()


def get_pot_by_display_id(display_id):
    pots = get_pots()
    for pot in pots:
        if pot[0] == display_id:
            return pot

    return None

def change_pot_placement(placement, pot_id):
    connection = create_connection()
    if connection is not None:
        cursor = connection.cursor()
        try:
            cursor.execute("UPDATE Pots SET placement=? WHERE id=?", (placement, pot_id))
            connection.commit()
            print("pot moved")
        except sqlite3.Error as e:
            print(e)
        finally:
            connection.close

def update_pot_with_plant(pot_id, plant_id):
    connection = create_connection()
    if connection is not None:
        cursor = connection.cursor()
        try:
            cursor.execute("UPDATE Pots SET plant_id=? WHERE id=?", (plant_id, pot_id))
            connection.commit()
            print("pot updated")
        except sqlite3.Error as e:
            print(e)
        finally:
            connection.close
                          

def delete_pot(pot_id):
    connection = create_connection()
    if connection is not None:
        cursor = connection.cursor()
        try:
            cursor.execute("DELETE FROM Pots WHERE id=?;", (pot_id,))
            connection.commit()
        except sqlite3.Error as e:
            print(e)
        finally:
            connection.close()


def remove_plant_from_pot(pot_id):
    connection = create_connection()
    if connection is not None:
        cursor = connection.cursor()
        try:
            cursor.execute("UPDATE Pots SET plant_id=NULL WHERE id=?", (pot_id,))
            connection.commit()
            print("plant removed from pot")
        except sqlite3.Error as e:
            print(e)
        finally:
            connection.close()


def is_pots_table_empty() -> bool:
    """
    Checks if the 'Pots' table in the database is empty.

    Returns:
        bool: True if the table is empty, False otherwise.
    """
    connection = create_connection()
    if connection is not None:
        cursor = connection.cursor()
        try:
            cursor.execute("SELECT COUNT(*) FROM Pots")
            count = cursor.fetchone()[0]
            return count == 0
        except sqlite3.Error as e:
            print(e)
        finally:
            connection.close()

def add_data_if_needed() -> None:
    """
    Adds test data to the 'Pots' table if it is empty.
    """
    if is_pots_table_empty():
        generate_pots()

def generate_pots():
    add_pot("clay", "balcony", "medium", None)


create_pots_table()
add_data_if_needed()