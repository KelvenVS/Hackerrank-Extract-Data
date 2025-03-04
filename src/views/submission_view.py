# src/views/submission_view.py
class SubmissionView:
    @staticmethod
    def display(submission):
        print(f"Contest: {submission.contest}")
        print(f"Challenge: {submission.challenge}")
        print(f"Code:\n{submission.code}")
        print(f"Score: {submission.score}")
        print(f"Language: {submission.language}")
        print("-" * 40)