def fctn1(arr):
    arr.sort(key=lambda x: x[1])
    #print(arr)
    
    seclow_score = None
    for i in range(len(arr) - 1):
        if arr[i][1] != arr[i+1][1]:
            seclow_score = arr[i+1][1]
            break

    if seclow_score is not None:
        students_alphabetic = []
        for student,score in arr:
            if score == seclow_score:
                students_alphabetic.append(student)
        
        students_alphabetic.sort()
        for student in students_alphabetic:
            print(student)
    else: 
        print("There is no second lowest grade in the class")
    
    
if __name__ == '__main__':
    student_arr = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        student_arr.append([name,score])
    
    fctn1(student_arr)
