import tkinter as tk
from login import login_window

# Main window constructor
root = tk.Tk()  # Make temporary window for app to start
root.withdraw()  # WithDraw the window


if __name__ == "__main__":

    login_window()

    root.mainloop()