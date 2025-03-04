import numpy

def reshape_arr(arr):
    return numpy.reshape(arr,(3,3))

if __name__ ==  '__main__':
    arr = list(map(int,input().split()))
    print(reshape_arr(arr))
