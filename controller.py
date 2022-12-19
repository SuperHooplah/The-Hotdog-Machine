import db_handler
import gui_handler

def main():
    # connect to an existing SQLite database file or create a new one
    db, cursor = db_handler.open_db("HotDogSandwich")
    gui_handler.gui(cursor)
    # commit any changes and close the database
    db_handler.close_db(db)

if __name__ == '__main__':
    main()