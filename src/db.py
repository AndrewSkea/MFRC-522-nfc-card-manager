import sqlite3


def setup_connection():
    try:
        sqliteConnection = sqlite3.connect('rfid_cards.db')
        cursor = sqliteConnection.cursor()
        print("Database created and Successfully Connected to SQLite")

        sqlite_select_Query = "select sqlite_version();"
        cursor.execute(sqlite_select_Query)
        record = cursor.fetchall()
        print("SQLite Database Version is: ", record)

        sqlite_select_Query = "CREATE TABLE IF NOT EXISTS cards (id INTEGER PRIMARY KEY AUTOINCREMENT, content TEXT NOT NULL);"
        cursor.execute(sqlite_select_Query)
        cursor.commit()
        cursor.close()

    except sqlite3.Error as error:
        print("Error while connecting to sqlite", error)
    finally:
        if (sqliteConnection):
            sqliteConnection.close()
            print("The SQLite connection is closed")


def get_db_cursor():
    try:
        sqliteConnection = sqlite3.connect('rfid_cards.db')
        cursor = sqliteConnection.cursor()
    except sqlite3.Error as error:
        print("Error while connecting to sqlite", error)
        cursor = None
    return cursor


def update_card(card_id, text):
    cursor = get_db_cursor()
    sqlite_select_Query = 'REPLACE INTO positions (id, content) VALUES({}, "{}");'.format(str(card_id), str(text))
    cursor.execute(sqlite_select_Query)
    cursor.commit()
    cursor.close()


def get_card(card_id):
    cursor = get_db_cursor()
    sqlite_select_Query = 'SELECT * FROM cards WHERE id = {}'.format(str(card_id))
    cursor.execute(sqlite_select_Query)
    record = cursor.fetchall()
    cursor.close()
    return record


def get_all_cards():
    cursor = get_db_cursor()
    sqlite_select_Query = 'SELECT * FROM cards'
    cursor.execute(sqlite_select_Query)
    record = cursor.fetchall()
    cursor.close()
    return record