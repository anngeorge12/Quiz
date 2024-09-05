from questionmodel import Question
from data import question_data
from quiz_brain import QuizBrain
question_bank = []
for data in question_data:
    q = Question(data["text"], data["answer"])
    question_bank.append(q)

quiz = QuizBrain(question_bank)
quiz.next_question()

while quiz.go_on():
    quiz.next_question()