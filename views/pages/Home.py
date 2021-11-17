import tkinter as tk


# Code here
class Home:

    def __init__(self):
        self.window = tk.Tk()


if __name__ == '__main__':
    window = tk.Tk()
    print(window.winfo_screenwidth(), window.winfo_screenheight())
    window.geometry('250x250+400+300') # can also set the position of the window
    label = tk.Label(window, text="Hello tkinter")
    label.pack()
    window.update()
    print(window.winfo_width(), window.winfo_height())
    window.mainloop()
