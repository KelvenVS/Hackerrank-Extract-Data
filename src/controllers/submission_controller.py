from models.submission_model import Submission
from views.submission_view import SubmissionView
import os
import re

class SubmissionController:
    def __init__(self, data):
        self.data = data
        self.submissions = []

    def load_submissions(self):
        for sub in self.data.get('submissions', []):
            submission = Submission(
                contest=sub.get('contest'),
                challenge=sub.get('challenge'),
                code=sub.get('code'),
                score=sub.get('score'),
                language=sub.get('language')
            )
            self.submissions.append(submission)

    def display_submissions(self):
        for submission in self.submissions:
            SubmissionView.display(submission)

    def save_submissions_to_files(self, directory):
        if not os.path.exists(directory):
            os.makedirs(directory)
        
        for submission in self.submissions:
            # Criar um nome de arquivo válido a partir do nome do desafio
            file_name = re.sub(r'\W+', '_', submission.challenge) + ".py"
            file_path = os.path.join(directory, file_name)
            with open(file_path, 'w') as file:
                file.write(submission.code)
