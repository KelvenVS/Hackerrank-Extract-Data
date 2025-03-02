import json

def open_json(file_location):
    with open(file_location, 'r') as file:
        data = json.load(file)
    return data

if __name__ == '__main__':
    
    data = open_json('../data/kelvenserejo_data.json')

    submissions = data.get('submissions', []) 

    
    # Itera sobre as submissões e imprime as informações
    for submission in submissions:
        contest = submission.get('contest')
        challenge = submission.get('challenge')
        code = submission.get('code')
        score = submission.get('score')
        language = submission.get('language')
        
        print(f"Contest: {contest}")
        print(f"Challenge: {challenge}")
        print(f"Code:\n {code}")
        print(f"Score: {score}")
        print(f"Language: {language}")
        print("-" * 20)  # Separador entre submissões