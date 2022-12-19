import tkinter as tk
import random

# this function pulls data from the database and generates a random hot dog
def displayRandomHotDog(cursor, text):
    text.delete("1.0", "end")
    text.insert("insert", str(random.randint(0, 10)))

# Used to start a gui with tkinter as tk. Only displays content of db currently
def gui(cursor):
    # create a new window
    root = tk.Tk()  # create root window
    root.title("Hot Dog Hero")  # title of the GUI window
    root.config(bg="skyblue")  # specify background color

    # Create left and right frames

    # the right frame will hold the text that gets updated with each button press
    right_frame = tk.Frame(root, bg='grey')
    right_frame.pack(side='right')

    text = tk.Text(right_frame)
    text.pack()

    # The left frame will hold all of the button for our functions
    left_frame = tk.Frame(root, width=200, height=400, bg='grey')
    left_frame.pack(side='left')

    genHotDog = tk.Button(left_frame, text="Generate Hot Dog", command=lambda: displayRandomHotDog(cursor, text))
    genHotDog.pack()

    # run the main event loop
    # This will process events to update the user interface allowing user input
    root.mainloop()
