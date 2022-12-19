import sqlite3
import os
import random
from typing import Tuple


# Creates a table based the SQL file
def open_db(filename: str) -> Tuple[sqlite3.Connection, sqlite3.Cursor]:
    # check if the database file already exists
    if not os.path.exists(filename + ".db"):
        # open the connection to the database and sets up a cursor
        db_connection = sqlite3.connect(filename + ".db")  # create new DB
        open_cursor = db_connection.cursor()  # get ready to read/write data

        # populate tables based off sql
        with open(filename + ".sql") as f:
            # read the SQL statements from the script
            sql = f.read()

        # execute the SQL statements
        open_cursor.executescript(sql)
    else:
        # if the .db file is already there connect to the existing database and sets up a cursors
        db_connection = sqlite3.connect(filename + ".db")
        open_cursor = db_connection.cursor()

    return db_connection, open_cursor


def close_db(connection: sqlite3.Connection):
    # closes the connection to the database
    connection.commit()  # make sure any changes get saved
    connection.close()


def interrupt_exterior_script(filename: str):
    # reads an .sql file and applies it to the database
    print()


def create_random_hotdog(conn):
    c = conn.cursor()

    # Gets a random bun
    c.execute("SELECT * FROM buns ORDER BY RANDOM() LIMIT 1")
    bun = c.fetchone()
    bun_id = bun[0]

    # Gets a random meat
    c.execute("SELECT * FROM meats ORDER BY RANDOM() LIMIT 1")
    meat = c.fetchone()
    meat_id = meat[0]

    # Gets a random condiment
    c.execute("SELECT * FROM condiment ORDER BY RANDOM() LIMIT 1")
    condiment = c.fetchone()
    condiment_id = condiment[0]

    # Insert the hotdog into the HotDog table
    c.execute("INSERT INTO HotDog (name, bun, meat, condiments) VALUES (?, ?, ?, ?)",
              ("Random Hot Dog", bun_id, meat_id, condiment_id))
    conn.commit()
#