import tkinter as tk
import random

# this function pulls data from the database and generates a random hot dog
def displayRandomHotDog(cursor, text):
    text.delete("1.0", "end")
    text.insert("insert", str(random.randint(0, 10)))


def displayHotDogsWindow(cursor, window):
    newWindow = tk.Toplevel(window)
    newWindow.title("Hot Dog Table")

    hotdog_text = tk.Text(newWindow)
    hotdog_text.pack()

    # query the HotDog table and display the results in the text widget
    hotdog_text.insert("insert", "PUT TEXT OUTPUT HERE")

def addIngredientToTable(cursor, type):
    # check what type of ingredient, open that table and add item
    print("")

# Used to start a gui with tkinter as tk. Only displays content of db currently
def gui(cursor):
    # create a new window
    root = tk.Tk()  # create root window
    root.title("Hot Dog Hero")  # title of the GUI window
    root.config(bg="skyblue")  # specify background color

    # Create left and right frames

    # the right frame will hold the text that gets updated with each button press
    right_frame = tk.Frame(root)
    right_frame.pack(side='right')

    text = tk.Text(right_frame)
    text.pack()

    # The left frame will hold all of the button for our functions
    left_frame = tk.Frame(root, width=200, height=400,)
    left_frame.pack(side='left')

    genHotDog = tk.Button(left_frame, text="Generate Hot Dog", command=lambda: displayRandomHotDog(cursor, text))
    genHotDog.pack(side='top')

    addCondimentBTN = tk.Button(left_frame, text="Add Condiment",
                                command=lambda: addIngredientToTable(cursor, "condiment"))
    addCondimentBTN.pack(side='top')

    displayAllDogs = tk.Button(left_frame, text="See all Hot Dogs", command=lambda: displayHotDogsWindow(cursor, root))
    displayAllDogs.pack(side='bottom')

    # run the main event loop
    # This will process events to update the user interface allowing user input
    root.mainloop()
