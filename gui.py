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
            text='Student Name:'
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
            text='No of Attempts:'
        )

        self.input_attempts = Entry(
            self.frame_two,
            width=5
        )

        self.button_generate = Button(
            self.frame_two,
            text='Generate',
            command=self.generate_scores
        )

        self.label_attempts.pack(side='left')
        self.input_attempts.pack(side='left')
        self.button_generate.pack(side='left')

        self.frame_two.pack(pady=5)

        '''
        Makes scores dynamic
        '''

        self.frame_three = Frame(window)
        self.frame_three.pack(pady=5)

        '''
        Makes the submit button
        '''
        self.frame_four = Frame(window)

        self.button_submit = Button(
            self.frame_four,
            text='SUBMIT',
            width=15,
            command=self.submit
        )

        self.button_submit.pack()
        self.frame_four.pack(pady=5)

        '''
        Makes the status labels
        '''
        self.frame_five = Frame(window)

        self.label_message= Label(
            self.frame_five,
            text='Ready',
            fg='blue'
        )

        self.label_message.pack()
        self.frame_five.pack()

    def generate_scores(self):
        '''
        Removes old scores.
        '''

        for widget in self.frame_three.winfo_children():
            widget.destroy()

        self.score_entries.clear()

        try:

            attempts = int(
                self.input_attempts.get()
            )

            if attempts < 1 or attempts > 4:
                raise ValueError

            for i in range(attempts):
                score_frame = Frame(
                    self.frame_three
                )

                score_label = Label(
                    score_frame,
                    text=f'Score {i + 1}:'
                )

                score_entry = Entry(
                    score_frame,
                    width=10
                )

                score_label.pack(side='left')
                score_entry.pack(side='left')

                score_frame.pack(anchor='w')

                self.score_entries.append(
                    score_entry
                )

            self.label_message.config(
                text='Scores generated.',
                fg='green'
            )

        except:

            self.label_message.config(
                text='Attempts must be 1-4.',
                fg='red'
            )

    def submit(self):

        try:

            name = self.input_name.get().strip()

            if name == '':
                raise ValueError(
                    'Name cannot be empty.'
                )

            scores = []

            for entry in self.score_entries:

                score = float(
                    entry.get()
                )

                if score < 0 or score > 100:
                    raise ValueError(
                        'Scores must be 0-100.'
                    )

                scores.append(score)

            best_score = max(scores)

            average = sum(scores) / len(scores)

            with open(
                    'grades.csv',
                    'a',
                    newline=''
            ) as file:

                writer = csv.writer(file)

                writer.writerow([
                    name,
                    *scores,
                    best_score,
                    average
                ])

            self.label_message.config(
                text='Submitted',
                fg='green'
            )

        except Exception as error:

            self.label_message.config(
                text=str(error),
                fg='red'
            )
