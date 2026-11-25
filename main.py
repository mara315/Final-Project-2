from tkinter import *
from gui import Gui

window = Tk()

window.title('Grades')
window.geometry('300x300')
window.resizable(width=False, height=False)

Gui(window)

window.mainloop()