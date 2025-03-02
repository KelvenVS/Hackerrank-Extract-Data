import json , os

def open_json(file_location):
    
    base_dir = os.path.dirname(os.path.abspath(__file__))
    full_path = os.path.join(base_dir, file_location)
    
    with open(full_path, 'r') as file:
        data = json.load(file)
    return data

if __name__ == '__main__':
    
    data = open_json('../data/kelvenserejo_data.json')

    submissions = data.get('submissions', []) 

    
    # Itera sobre as submissões e imprime as informações
    for submission in submissions:
        score = submission.get('score')
        if score >= 1:
            contest = submission.get('contest')
            challenge = submission.get('challenge')
            code = submission.get('code')
            language = submission.get('language')
            
            print(f"Contest: {contest}")
            print(f"Challenge: {challenge}")
            print(f"Code:\n {code}")
            print(f"Score: {score}")
            print(f"Language: {language}")
            print("-" * 50)  # Separador entre submissões