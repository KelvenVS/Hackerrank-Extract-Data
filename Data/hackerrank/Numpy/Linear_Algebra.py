import numpy as np

def np_det_mtx(np_arr):
    det = np.linalg.det(np_arr)
    return f'{det:.2f}' \
    if det != 0 and det != int(det) \
    else det


if __name__ == '__main__':
    n = int(input())
    
    aux_list = []
    for _ in range(n):
        aux_list.append(list(map(float, input().split())))
    
    print(np_det_mtx(np.array(aux_list)))
