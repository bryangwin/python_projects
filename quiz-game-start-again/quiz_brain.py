class QuizBrain:
    def __init__(self, q_list) -> None:
        self.question_number = 0
        self.score = 0
        self.user_answer = ""
        self.question_list = q_list

    def next_question(self):
        self.question_number += 1
        self.user_answer = input(
            f"Q.{self.question_number}: {self.question_list[self.question_number - 1].text} (True/False): ")
        self.check_answer()

    def check_answer(self): 
        if self.user_answer.lower() == self.question_list[self.question_number-1].answer.lower():
            self.score += 1
            print("Thats right!")
        else:
            print("That is wrong. Idiot.")
        print(f"Your score is {self.score}/{self.question_number}\n")

    def end_game(self):
        if self.question_number == len(self.question_list):
            print(
                f"That is the end of the questions. Your final score was {self.score}/{self.question_number}")
            return True
        else:
            return False
