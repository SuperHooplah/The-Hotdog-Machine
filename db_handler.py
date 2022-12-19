import sqlite3
from typing import Tuple


# this method creates a table based off an SQL file
def open_db(filename: str) -> Tuple[sqlite3.Connection, sqlite3.Cursor]:
    # opens the connection to the database and sets up a cursor
    db_connection = sqlite3.connect(filename + ".db")  # connect to existing DB or create new one
    open_cursor = db_connection.cursor()  # get ready to read/write data

    # populate tables based off sql
    with open(filename + ".sql") as f:
        # read the SQL statements from the script
        sql = f.read()

    # execute the SQL statements
    open_cursor.executescript(sql)

    return db_connection, open_cursor


def close_db(connection: sqlite3.Connection):
    # closes the connection to the database
    connection.commit()  # make sure any changes get saved
    connection.close()


def interrupt_exterior_script(filename: str):
    # reads an .sql file and applies it to the database
    print()
