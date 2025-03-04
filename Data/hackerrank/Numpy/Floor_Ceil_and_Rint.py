import numpy as np
np.set_printoptions(legacy='1.13')

def print_floor_ceil_rint(np_arr):
    print(np.floor(np_arr))
    print(np.ceil(np_arr))
    print(np.rint(np_arr))

if __name__ == '__main__':
    np_arr = np.array(list(map(float, input().split())))
    print_floor_ceil_rint(np_arr)
