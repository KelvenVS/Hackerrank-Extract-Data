

# Complete the solve function below.
def solve(s):
    aux_string = []
    for char in s:
        aux_string.append(char)
    
    for i in range(len(aux_string)):
        if aux_string[i-1] == ' ' or i == 0:
            aux_string[i] = aux_string[i].upper()
    aux_string = ''.join(aux_string)
    
    return aux_string
    
