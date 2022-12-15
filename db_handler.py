import sqlite3
import tkinter as tk
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

# Used to generate a DB from the SQL script
def sql_exe():
    # connect to an existing SQLite database file or create a new one
    db = sqlite3.connect("HotDogSandwich.db")

    # create a cursor object
    cursor = db.cursor()

    # open the SQL script
    with open("HotDogSandwich.sql") as f:
        # read the SQL statements from the script
        sql = f.read()

    # execute the SQL statements
    cursor.executescript(sql)

    # commit the changes to the database
    db.commit()

    # close the database connection
    db.close()

# Used to start a gui with tkinter as tk. Only displays content of db currently
def gui():
    # create a new window
    window = tk.Tk()

    # connect to SQLite database file
    db = sqlite3.connect("HotDogSandwich.db")

    # create cursor object
    cursor = db.cursor()

    # create first table, "HotDog"
    # cursor.execute("CREATE TABLE HotDog (Bun TEXT, Condiments TEXT, Toppings TEXT, Meats TEXT)")

    # insert data into the table
    # cursor.execute("INSERT INTO HotDog VALUES ('Sesame', 'Mustard', 'Onions', 'Beef')")
    # cursor.execute("INSERT INTO HotDog VALUES ('Whole Wheat', 'Ketchup', 'Pickles', 'Pork')")

    # create second table, "Sandwich"
    # cursor.execute("CREATE TABLE Sandwich (Bread TEXT, Meat TEXT, Condiments TEXT, Toppings TEXT)")

    # insert data into the table
    # cursor.execute("INSERT INTO Sandwich VALUES ('White', 'Turkey', 'Mayonnaise', 'Lettuce')")
    # cursor.execute("INSERT INTO Sandwich VALUES ('Rye', 'Ham', 'Mustard', 'Tomato')")

    # commit changes
    # db.commit()

    # create a text widget to display the contents of the HotDog table
    hotdog_text = tk.Text(window)
    hotdog_text.pack()

    # query the HotDog table and display the results in the text widget
    cursor.execute("SELECT * FROM HotDog")
    results = cursor.fetchall()

    for row in results:
        hotdog_text.insert(tk.END, row[0] + " " + row[1] + " " + row[2] + " " + row[3] + "\n")

    # create a text widget to display the contents of the Sandwich table
    sandwich_text = tk.Text(window)
    sandwich_text.pack()

    # query the Sandwich table and display the results in the text widget
    cursor.execute("SELECT * FROM Sandwich")
    results = cursor.fetchall()

    for row in results:
        sandwich_text.insert(tk.END, row[0] + " " + row[1] + " " + row[2] + " " + row[3] + "\n")

    # close the database connection
    db.close()

    # run the main event loop
    # This will process events to update the user interface allowing user input
    window.mainloop()


# Main
# call sql_exe to generate the db file
sql_exe()
gui()
