import numpy

if __name__ == '__main__':
    mtx1 = numpy.array(list(map(int,input().split())))
    mtx2 = numpy.array(list(map(int,input().split())))
    
    print(numpy.inner(mtx1,mtx2))
    print(numpy.outer(mtx1,mtx2))
