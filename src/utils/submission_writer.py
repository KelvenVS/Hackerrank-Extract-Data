import os

def save_submission_as_py(submission, base_dir):
    contest = submission.get('contest')
    challenge = submission.get('challenge')
    code = submission.get('code')

    # Nome do arquivo com base no contest e challenge
    filename = f"{contest}_{challenge}.py".replace(" ", "_").replace("\"", "")

    # Caminho completo do arquivo
    file_path = os.path.join(base_dir, 'data/hackerrank', filename)

    # Cria a pasta se não existir
    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    # Salva o código no arquivo
    with open(file_path, 'w') as file:
        file.write(code)