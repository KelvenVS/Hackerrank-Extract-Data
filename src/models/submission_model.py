class Submission:
    def __init__(self, contest, challenge, code, score, language):
        self.contest = contest
        self.challenge = challenge
        self.code = code
        self.score = score
        self.language = language

    def __str__(self):
        return f"Contest: {self.contest}, Challenge: {self.challenge}, Score: {self.score}, Language: {self.language}"