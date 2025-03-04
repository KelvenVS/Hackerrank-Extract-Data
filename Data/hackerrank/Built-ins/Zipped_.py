def average_score(exams_list):
    for student_score in zip(*exams_list):
        print(sum(score for score in student_score)/ len(exams_list))

if __name__ == '__main__':
    students , exams = map(int,input().split())
    
    exams_list = []
    for _ in range(exams):
        exams_list.append(list(map(float,input().split())))
    
    average_score(exams_list)
