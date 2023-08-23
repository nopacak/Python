import sqlite3

def create_connection():
    """
    Creates a connection to the SQLite database.

    Returns:
        The connection object or None if an error occurred.
    """
    try:
        connection = sqlite3.connect("PyFlora.db")
        return connection
    except sqlite3.Error as e:
        #print(e)
        return None


def create_table() -> None:
    """
    Creates the 'Users' table in the database. If the table already exists, this function does nothing.
    """
    connection = create_connection()
    if connection is not None:
        cursor = connection.cursor()
        try:
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS Users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    first_name TEXT,
                    last_name TEXT,
                    username TEXT NOT NULL UNIQUE,
                    password TEXT NOT NULL
                );
            """)
            connection.commit()
        except sqlite3.Error as e:
            #print(e)
            return None
        finally:
            connection.close()



def add_user(first_name: str, last_name: str, username: str, password: str) -> bool:
    """
    Adds a new user to the 'Users' table.

    Args:
        first_name (str): The first name of the user.
        last_name (str): The last name of the user.
        username (str): The username of the user.
        password (str): The password of the user.
    """
    create_table()
    connection = create_connection()
    if connection is not None:
        cursor = connection.cursor()
        try:
            cursor.execute("INSERT INTO Users (first_name, last_name, username, password) VALUES (?, ?, ?, ?)",
                           (first_name, last_name, username, password))
            connection.commit()
            #print("User added successfully.")
            return True
        except sqlite3.Error as e:
            #print(e)
            return False
        finally:
            connection.close()


def get_user_id(username: str) -> int:
    """
    Retrieves the ID of a user by their username.

    Args:
        username (str): The username of the user.

    Returns:
        The ID of the user or None if the user does not exist.
    """
    connection = create_connection()
    if connection is not None:
        cursor = connection.cursor()
        try:
            cursor.execute("SELECT id FROM Users WHERE username = ?", (username,))
            user_id = cursor.fetchone()
            if user_id is not None:
                return user_id[0]
            else:
                return None
        except sqlite3.Error as e:
            #print(e)
            return None
        finally:
            connection.close()


def update_user(user_id: int, first_name: str, last_name: str, username: str, password: str) -> None:
    """
    Updates the details of a user.

    Args:
        user_id (int): The ID of the user to update.
        first_name (str): The new first name of the user.
        last_name (str): The new last name of the user.
        username (str): The new username of the user.
        password (str): The new password of the user.
    """
    connection = create_connection()
    if connection is not None:
        cursor = connection.cursor()
        try:
            cursor.execute("""
                UPDATE Users
                SET first_name = ?, last_name = ?, username = ?, password = ?
                WHERE id = ?
            """, (first_name, last_name, username, password, user_id))
            connection.commit()
            #print("User updated successfully.")
        except sqlite3.Error as e:
            #print(e)
            return None
        finally:
            connection.close()


# def check_password(username: str, password: str) -> bool:
#     """
#     Checks if a password matches the stored password for a given username.

#     Args:
#         username (str): The username to check.
#         password (str): The password to check.

#     Returns:
#         bool: True if the password matches, False otherwise.
#     """
#     connection = create_connection()
#     if connection is not None:
#         cursor = connection.cursor()
#         try:
#             cursor.execute("SELECT password FROM Users WHERE username=?", (username,))
#             db_password = cursor.fetchone()
#             if db_password is None:
#                 return False
#             stored_password = db_password[0]
#         except sqlite3.Error as e:
#             print(f"An error occurred while checking password: {e}")
#             return False
#         finally:
#             connection.close()
#         return stored_password == password


# def check_user(username: str, password: str) -> bool:
#     """
#     Checks if a username matches the stored username for a given password.

#     Args:
#         username (str): The username to check.
#         password (str): The password to check.

#     Returns:
#         bool: True if the username matches, False otherwise.
#     """
#     connection = create_connection()
#     if connection is not None:
#         cursor = connection.cursor()
#         try:
#             cursor.execute("SELECT username FROM Users WHERE password=?", (password,))
#             db_user = cursor.fetchone()
#             if db_user is None:
#                 return False
#             stored_user = db_user[0]
#         except sqlite3.Error as e:
#             print(f"An error occurred while checking password: {e}")
#             return False
#         finally:
#             connection.close()
#         return stored_user == username

def delete_user(username: str) -> bool:
    connection = create_connection()
    if connection is not None:
        cursor = connection.cursor()
        try:
            cursor.execute(f"DELETE FROM Users WHERE username='{username}'")
            connection.commit()
            return True
        except sqlite3.Error as e:
            #print(e)
            return False
        finally:
            connection.close()


def check_login(username: str, password: str) -> bool:
    """
    Checks if entered username and password exist in the database 
    """
    connection = create_connection()
    if connection is not None:
        cursor = connection.cursor()
        try:
            cursor.execute(f"SELECT count(username) FROM Users WHERE username='{username}' and password='{password}'")
            if cursor.fetchone()[0] == 1:
                return True
            else:
                return False
        except sqlite3.Error as e:
            #print(e)
            return False
        finally:
            connection.close()

#create_table()
#add_user("Nikolina", "Opacak", "admin", "admin")
