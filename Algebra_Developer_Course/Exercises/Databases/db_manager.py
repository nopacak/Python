import sqlite3

def create_connection(db_file: str) -> sqlite3.Connection | None:
    sql_connection = None

    try:
        sql_connection = sqlite3.connect(db_file)
        return sql_connection
    
    except sqlite3.Error as error:
        print(f"Error!!! -> {error}")
        return sql_connection
    


def create_table(sql_connection: sqlite3.Connection, create_table_query: str) -> bool:
    try:
        cursor = sql_connection.cursor()
        cursor.execute(create_table_query)
        sql_connection.commit()
        cursor.close()
        return True

    except sqlite3.Error as error:
        print(f"Error!! -> {error}")
        return False
    


def insert_into_table(sql_connection: sqlite3.Connection, insert_query: str, data: list) -> bool:
    try:
        cursor = sql_connection.cursor()

        for item in data:
            cursor.execute(insert_query, item)

        sql_connection.commit()
        cursor.close()
        return True

    except sqlite3.Error as error:
        print(f"Error!! -> {error}")
        return False



def select_all_from_table(sql_connection: sqlite3.Connection, select_all_query: str) -> list | None:
    try:
        cursor = sql_connection.cursor()
        cursor.execute(select_all_query)
        records = cursor.fetchall()
        cursor.close()

        return records
    except sqlite3.Error as error:
        print(f"Error!!! -> {error}")
        return None
    
