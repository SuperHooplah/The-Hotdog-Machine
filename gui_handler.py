import tkinter as tk


# Used to start a gui with tkinter as tk. Only displays content of db currently
def gui():
    # create a new window
    root = tk.Tk()  # create root window
    root.title("Hot Dog Hero")  # title of the GUI window
    root.config(bg="skyblue")  # specify background color

    # Create left and right frames
    left_frame = tk.Frame(root, width=200, height=400, bg='grey')
    left_frame.grid(row=0, column=0, padx=10, pady=5)

    right_frame = tk.Frame(root, width=900, height=400, bg='grey')
    right_frame.grid(row=0, column=1, padx=10, pady=5)

    # run the main event loop
    # This will process events to update the user interface allowing user input
    root.mainloop()