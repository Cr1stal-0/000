import sqlite3
import settings

def send_to_database(name, phone):
    connection = sqlite3.connect(f"./database/{settings.database_name}.db")
    cursor = connection.cursor()

    request = """
        INSERT INTO users
        VALUES (?, ?)
    """

    cursor.execute(request, (name, phone,))

    connection.commit()
    connection.close()

def get_data_from_db():
    connection = sqlite3.connect(f"./database/{settings.database_name}.db")
    cursor = connection.cursor()

    request = """
        SELECT * FROM users
    """
    c = cursor.execute(request)
    for i in c:
        print(i)

    connection.commit()
    connection.close()
