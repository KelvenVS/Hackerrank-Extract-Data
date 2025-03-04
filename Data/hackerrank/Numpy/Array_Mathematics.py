import numpy as np

def printer_operatios(arr,n):
    mtx1 = np.array(arr[:n])
    mtx2 = np.array(arr[n:])
    
    print(np.add(mtx1, mtx2))
    print(np.subtract(mtx1, mtx2))
    print(np.multiply(mtx1, mtx2))
    print(np.floor_divide(mtx1, mtx2))
    print(np.mod(mtx1, mtx2))
    print(np.power(mtx1, mtx2))

if __name__ == '__main__':
    n , m = map(int, input().split())
    
    aux_list = []
    for _ in range(n*2):
        aux_list.append(list(map(int, input().split())))
        
    printer_operatios(aux_list,n)
