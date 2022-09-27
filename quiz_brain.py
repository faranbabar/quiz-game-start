class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list

    def still_has_question(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}:{current_question.text} (true/false):").lower()
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):

        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print(
                f'You are right\nThe correct answer was {correct_answer}\nYour current score is {self.score}/{self.question_number}')
        else:
            print(
                f'You are wrong\nThe correct answer was {correct_answer}\nYour current score is {self.score}/{self.question_number}')

