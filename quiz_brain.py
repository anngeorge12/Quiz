class QuizBrain:
    def __init__(self, quest):
        self.question_no = 0
        self.question_list = quest
        self.score = 0
        self.pop = True

    def go_on(self):
        return self.question_no < len(self.question_list) and self.pop

    def check_answer(self, ans, real):
        if real == ans:
            print("your answer is right")
            self.score += 1
            print(f"score: {self.score}/{self.question_no}")
        else:
            print("your answer is wrong")
            print(f"the correct answer is {real}")
            print(f"score: {self.score}/{self.question_no}")
            self.pop = False

    def next_question(self):
        cur_question = self.question_list[self.question_no]
        self.question_no += 1
        ans = input(f"Q.{self.question_no}: {cur_question.Text} (True/False): ")

        self.check_answer(ans, cur_question.Answer)

