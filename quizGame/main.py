from data import question_data


class Question:
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer


question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    # creating object
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)


# print(question_bank)


class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list

    def still_has_questions(self):
        if self.question_number < len(self.question_list):
            return True
        else:
            return False

    def next_question(self):
        crnt_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {crnt_question.text} (Type True or false or answer itself) ").lower()
        self.check_answer(user_answer, crnt_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer == correct_answer.lower():
            self.score += 1
            print("Yaay you are right!")
        else:
            print("Oops You're wrong!")
            print(f"The right answer was {correct_answer}")
        print(f"You're score is {self.score}/{self.question_number}")
        print("\n")


# creating new object
quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the game")
print(f"You're score is {quiz.score}/{quiz.question_number}")
