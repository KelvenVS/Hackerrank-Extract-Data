import numpy as np

def np_max_of_min_values(arr,axis):
    np_arr = np.array(arr)
    np_axis1_min = np.min(np_arr, axis = axis)
    return max(np_axis1_min)

if __name__ == '__main__':
    n , m = list(map(int ,input().split()))
    
    aux_list = []
    for _ in range(n):
        aux_list.append(list(map(int ,input().split())))
    
    
    print(np_max_of_min_values(aux_list,1))
    
