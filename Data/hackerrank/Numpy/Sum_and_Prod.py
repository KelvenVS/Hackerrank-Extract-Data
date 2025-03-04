import numpy as np

def np_sum_prod(arr):
    np_arr = np.array(arr)
    np_arr = np.sum(np_arr , axis = 0)
    return np.prod(np_arr)

if __name__ == '__main__':
    n , m = list(map(int, input().split()))
    
    aux_list = []
    for _ in range(n):
        aux_list.append(list(map(int, input().split())))
        
    print(np_sum_prod(aux_list))
