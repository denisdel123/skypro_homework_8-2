class Question:

    def __init__(self, text, difficulty, correct_answer):
        self.text = text
        self.difficulty = int(difficulty)
        self.correct_answer = correct_answer

        self.is_question = False
        self.user_answer = None
        self.score = 0

    def point(self):
        self.score = self.difficulty * 10
        return self.score

    def is_correct(self):
        return self.user_answer == self.correct_answer

    def build_question(self):
        return f"Вопрос: {self.text} Сложность {self.difficulty}/5"

    def build_feedback(self):
        if self.is_correct():
            return f"Ответ верный, получено {self.point()} баллов."
        return f"Ответ неверный, верный ответ {self.correct_answer}"

