import numpy

def calc_dot_matrix(arr,qty_lines):
    mtx1 = numpy.array(arr[:qty_lines])
    mtx2 = numpy.array(arr[qty_lines:])
    
    return numpy.dot(mtx1,mtx2)


if __name__ == '__main__':
    qty_lines = int(input())
    
    aux_arr = []
    for _ in range(qty_lines*2):
        aux_arr.append(list(map(int, input().split())))
  
    print(calc_dot_matrix(aux_arr,qty_lines))
    
