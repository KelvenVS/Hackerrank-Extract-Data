import re

def decode_matrix(matrix_arr,m,n):
    decode = []

    for col in range(m):  
        for row in range(n):
            decode.append(matrix_arr[row][col])  

    decode = ''.join(decode)
    pattern = r'(?<=\w)[^\w\d]+(?=\w)'
    decoded_text = re.sub(pattern, ' ', decode)
    
    return decoded_text

first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)

print(decode_matrix(matrix,m,n))

    
