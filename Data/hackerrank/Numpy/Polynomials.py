import numpy as np


if __name__ == '__main__':
    np_arr = np.array(list(map(float, input().split())))
    x = int(input())
    
    print(np.polyval(np_arr, x))
