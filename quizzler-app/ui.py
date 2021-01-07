from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"


class QuizAppUI:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("QuizApp")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text=f"Score: {self.quiz.score}",
                                 bg=THEME_COLOR, fg="white")
        self.score_label.grid(row=0, column=1)

        self.quiz_canvas = Canvas(height=250, width=300, bg="white")
        self.question_text = self.quiz_canvas.create_text(150, 125,
                                                          width=280,
                                                          text="Quiz question",
                                                          font=("Arial", 20, "italic"),
                                                          fill=THEME_COLOR)
        self.quiz_canvas.grid(row=1, column=0, columnspan=2, pady=50)

        true_img = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_img, highlightthickness=0,
                                  command=self.check_answer_true)
        self.true_button.grid(row=2, column=0)

        false_img = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_img, highlightthickness=0,
                                   command=self.check_answer_false)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.quiz_canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.quiz_canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.quiz_canvas.itemconfig(self.question_text,
                                        text="You have reached the end of the quiz")
            self.false_button.config(state="disabled")
            self.true_button.config(state="disabled")

    def check_answer_true(self):
        is_right = self.quiz.check_answer("True")
        self.update_score(self.quiz.score)
        self.feedback(is_right)

    def check_answer_false(self):
        is_right = self.quiz.check_answer("False")
        self.update_score(self.quiz.score)
        self.feedback(is_right)

    def update_score(self, score):
        self.score_label.config(text=f"Score: {score}")

    def feedback(self, is_right):
        if not is_right:
            self.quiz_canvas.config(bg="red")
        else:
            self.quiz_canvas.config(bg="green")
        self.window.after(1000, self.get_next_question)
