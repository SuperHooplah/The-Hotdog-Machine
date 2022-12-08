import sqlite3
from typing import Tuple


def open_db(filename: str) -> Tuple[sqlite3.Connection, sqlite3.Cursor]:
    # opens the connection to the database
    db_connection = sqlite3.connect(filename)  # connect to existing DB or create new one
    open_cursor = db_connection.cursor()  # get ready to read/write data
    return db_connection, open_cursor


def close_db(connection: sqlite3.Connection):
    # closes the connection to the database
    connection.commit()  # make sure any changes get saved
    connection.close()


def interrupt_exterior_script(filename: str):
    # reads an .sql file and applies it to the database
    print()
