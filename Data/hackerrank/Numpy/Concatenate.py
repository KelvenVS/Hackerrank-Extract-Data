import numpy

def concat_mtx(arr,x,y):
    mtx1 = numpy.array(arr[:x])
    mtx2 = numpy.array(arr[x:x+y])
    return numpy.concatenate((mtx1,mtx2), axis = 0)    

if __name__ == '__main__':
    m, n, p = list(map(int,input().split()))
    
    aux_arr = []
    for _ in range(m+n):
        aux_arr.append(list(map(int,input().split())))
    
    print(concat_mtx(aux_arr,m,n))
    
