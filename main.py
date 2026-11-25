from tkinter import *
from gui import Gui

window = Tk()

window.title('Grades')
window.geometry('250x250')
window.resizable(width=False, height=False)

Gui(window)

window.mainloop()