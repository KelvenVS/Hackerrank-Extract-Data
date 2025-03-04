import numpy

def printer(arr):
    print(numpy.zeros((arr), dtype = int))
    print(numpy.ones((arr), dtype = int))

if __name__ == '__main__':
    aux_list = numpy.array(list(map(int, input().split())))
    
    printer(aux_list)
