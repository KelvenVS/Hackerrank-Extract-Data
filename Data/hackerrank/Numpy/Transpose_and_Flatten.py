import numpy

def transpose_arrr(arr):
    arr_aux = numpy.array(arr)
    return numpy.transpose(arr_aux)

def flatten_arr(arr):
    arr_aux = numpy.array(arr)
    return arr_aux.flatten()

if __name__ == '__main__':
    mtx_size = tuple(map(int,input().split()))
    
    aux_list = []
    for _ in range(mtx_size[0]):
        aux_list.append(list(map(int,input().split())))

    print(transpose_arrr(aux_list))
    print(flatten_arr(aux_list))
