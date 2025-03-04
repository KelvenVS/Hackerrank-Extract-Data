def average(query,student_marks):
    return f'{sum(student_marks[query])/3:.2f}'
    
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    print(average(query_name,student_marks))
