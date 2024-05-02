# from tkinter import Tk, Label, Entry, Button, Frame, messagebox
# from typing import List, Tuple
# from grade_calculator import GradeCalculator
# import csv
#
# class GradeGUI:
#     def __init__(self, master: Tk) -> None:
#         self.master = master
#         master.title("Grade Calculator")
#         master.geometry("300x300")
#         master.resizable(False, False)
#
#         self.student_entries: List[Entry] = []
#         self.info_labels: List[Label] = []
#         self.score_entries: List[Entry] = []
#
#         self.create_student_entries()
#
#     def create_student_entries(self) -> None:
#         self.label = Label(self.master, text="Enter Student Name:")
#         self.label.pack()
#
#         self.student_name_entry = Entry(self.master)
#         self.student_name_entry.pack()
#
#         self.label = Label(self.master, text="Enter Number of Attempts:")
#         self.label.pack()
#
#         self.attempts_entry = Entry(self.master)
#         self.attempts_entry.pack()
#
#         self.submit_button = Button(self.master, text="Submit", command=self.create_score_entries)
#         self.submit_button.pack()
#
#         self.error_label = Label(self.master, text="", fg="red")
#         self.error_label.pack()
#
#         self.info_frame = Frame(self.master)
#         self.info_frame.pack()
#
#     def create_score_entries(self) -> None:
#         student_name: str = self.student_name_entry.get().strip()
#         attempts: str = self.attempts_entry.get().strip()
#
#         if not student_name.isalpha():
#             self.display_error_message("Student name must contain only alphabets.")
#             return
#
#         if not attempts.isdigit() or int(attempts) < 1:
#             self.display_error_message("Number of attempts must be a positive integer.")
#             return
#
#         self.error_label.config(text="")
#
#         self.submit_button.destroy()
#         self.student_name_entry.config(state="disabled")
#         self.attempts_entry.config(state="disabled")
#
#         self.label = Label(self.info_frame, text=f"Student: {student_name}")
#         self.label.pack()
#         self.info_labels.append(self.label)
#
#         self.label = Label(self.info_frame, text=f"Number of Attempts: {attempts}")
#         self.label.pack()
#         self.info_labels.append(self.label)
#
#         for i in range(int(attempts)):
#             label = Label(self.master, text=f"Enter score for Attempt {i+1}:")
#             label.pack()
#             entry = Entry(self.master)
#             entry.pack()
#             self.score_entries.append(entry)
#
#         self.submit_button = Button(self.master, text="Calculate Grades", command=self.calculate_grades)
#         self.submit_button.pack()
#
#     def calculate_grades(self) -> None:
#         scores: List[int] = []
#         for entry in self.score_entries:
#             score = entry.get().strip()
#             if not score.isdigit() or int(score) < 0 or int(score) > 100:
#                 self.display_error_message("Scores must be integers between 0 and 100.")
#                 return
#             scores.append(int(score))
#
#         calculator = GradeCalculator(scores)
#         best_score = calculator.get_best_score()
#         avg_score = calculator.get_average_score()
#         results = calculator.get_grades(best_score)
#
#         student_name: str = self.student_name_entry.get().strip()
#         attempts: str = self.attempts_entry.get().strip()
#
#         # Write to CSV
#         with open('grades.csv', mode='a', newline='') as file:
#             writer = csv.writer(file)
#             writer.writerow([f'Student: {student_name}', f'Number of Attempts: {attempts}'])
#             for i, (score, grade) in enumerate(results, start=1):
#                 writer.writerow([f'Attempt {i}', score, grade])
#             writer.writerow(['Highest Score', best_score, ''])
#             writer.writerow(['Average Score', avg_score, ''])
#             writer.writerow([])  # Empty row for separation
#
#         messagebox.showinfo("Grades Calculated", "Grades have been calculated and saved to grades.csv.")
#
#     def display_error_message(self, message: str) -> None:
#         self.error_label.config(text=message)
#
# def main() -> None:
#     root = Tk()
#     gui = GradeGUI(root)
#     root.mainloop()
#
# if __name__ == "__main__":
#     main()
from tkinter import Tk, Label, Entry, Button, Frame, messagebox
from grade_calculator import *
import csv

class GradeGUI:
    def __init__(self, master):

        self.master = master
        master.title("Grade Calculator")
        master.geometry("300x300")
        master.resizable(False, False)

        self.student_entries = []  # List[Entry]
        self.info_labels = []  # List[Label]
        self.score_entries = []  # List[Entry]

        self.create_student_entries()

    def create_student_entries(self):
        """Create entry fields for student name and number of attempts."""
        self.label = Label(self.master, text="Enter Student Name:")
        self.label.pack()

        self.student_name_entry = Entry(self.master)
        self.student_name_entry.pack()

        self.label = Label(self.master, text="Enter Number of Attempts:")
        self.label.pack()

        self.attempts_entry = Entry(self.master)
        self.attempts_entry.pack()

        self.submit_button = Button(self.master, text="Submit", command=self.create_score_entries)
        self.submit_button.pack()

        self.error_label = Label(self.master, text="", fg="red")
        self.error_label.pack()

        self.info_frame = Frame(self.master)
        self.info_frame.pack()

    def create_score_entries(self):
        """Create entry fields for scores based on the number of attempts."""
        student_name = self.student_name_entry.get().strip()
        attempts = self.attempts_entry.get().strip()

        if not student_name.isalpha():
            self.display_error_message("Student name must contain only alphabets.")
            return

        if not attempts.isdigit() or int(attempts) < 1:
            self.display_error_message("Number of attempts must be a positive integer.")
            return

        self.error_label.config(text="")

        self.submit_button.destroy()
        self.student_name_entry.config(state="disabled")
        self.attempts_entry.config(state="disabled")

        self.label = Label(self.info_frame, text=f"Student: {student_name}")
        self.label.pack()
        self.info_labels.append(self.label)

        self.label = Label(self.info_frame, text=f"Number of Attempts: {attempts}")
        self.label.pack()
        self.info_labels.append(self.label)

        for i in range(int(attempts)):
            label = Label(self.master, text=f"Enter score for Attempt {i+1}:")
            label.pack()
            entry = Entry(self.master)
            entry.pack()
            self.score_entries.append(entry)

        self.submit_button = Button(self.master, text="Calculate Grades", command=self.calculate_grades)
        self.submit_button.pack()

    def calculate_grades(self):
        """Calculate grades based on the scores entered."""
        scores = []
        for entry in self.score_entries:
            score = entry.get().strip()
            if not score.isdigit() or int(score) < 0 or int(score) > 100:
                self.display_error_message("Scores must be integers between 0 and 100.")
                return
            scores.append(int(score))

        calculator = GradeCalculator(scores)
        best_score = calculator.get_best_score()
        avg_score = round(calculator.get_average_score(), 2)  # Round to 2 decimal places
        results = calculator.get_grades(best_score)

        student_name = self.student_name_entry.get().strip()
        attempts = self.attempts_entry.get().strip()

        # Write to CSV
        with open('grades.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([f'Student: {student_name}', f'Number of Attempts: {attempts}'])
            for i, (score, grade) in enumerate(results, start=1):
                writer.writerow([f'Attempt {i}', score, grade])
            writer.writerow(['Highest Score', best_score, ''])
            writer.writerow(['Average Score', avg_score, ''])
            writer.writerow([])  # Empty row for separation

        messagebox.showinfo("Grades Calculated", "Grades have been calculated and saved to grades.csv.")

    def display_error_message(self, message):
        """Display error message on the GUI."""
        self.error_label.config(text=message)

def main():
    """Initialize the Tkinter root window and GradeGUI instance."""
    root = Tk()
    gui = GradeGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
