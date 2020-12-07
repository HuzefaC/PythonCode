class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def still_has_question(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        next_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {next_question.text} (True/False)?: ")
        self.check_answer(user_answer, next_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("Correct answer.")
            self.score += 1
        else:
            print("Wrong answer.")
        print(f"The correct answer was {correct_answer}")
        print(f"Score: {self.score}/{self.question_number}\n")
