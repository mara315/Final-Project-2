from tkinter import *
import csv

class Gui:

    def __init__(self, window):

        self.window = window
        self.score_entries = []

        '''
        Make student names
        '''

        self.frame_one = Frame(window)

        self.label_name = Label(
            self.frame_one,
            text="Student Name:"
        )

        self.input_name = Entry(
            self.frame_one,
            width=20
        )

        self.label_name.pack(side='left')
        self.input_name.pack(side='left')

        self.frame_one.pack(pady=5)

        '''
        Keeping track of attempts
        '''

        self.frame_two = Frame(window)

        self.label_attempts = Label(
            self.frame_two,
            text="No of Attempts:"
        )

        self.input_attempts = Entry(
            self.frame_two,
            width=5
        )

        self.button_generate = Button(
            self.frame_two,
            text="Generate",
            command=self.generate_scores
        )

        self.label_attempts.pack(side='left')
        self.input_attempts.pack(side='left')
        self.button_generate.pack(side='left')

        self.frame_two.pack(pady=5)

        

