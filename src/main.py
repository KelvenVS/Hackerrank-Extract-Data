# src/main.py
from utils.file_manager import load_json
from controllers.submission_controller import SubmissionController
import os

def main():
    # Caminho relativo para o arquivo JSON
    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_dir, '../data/kelvenserejo_data.json')

    # Carrega os dados do JSON
    data = load_json(file_path)

    # Cria e carrega o controlador de submissões
    controller = SubmissionController(data)
    controller.load_submissions()
    
    # Exibe as submissões
    controller.display_submissions()

    # Caminho para salvar os arquivos Python
    save_directory = os.path.join(base_dir, '../data/hackerrank')
    
    # Salva as submissões em arquivos Python
    controller.save_submissions_to_files(save_directory)

if __name__ == "__main__":
    main()