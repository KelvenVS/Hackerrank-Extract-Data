import numpy
numpy.set_printoptions(legacy='1.13')

def print_eye_identity(n,m):
    if n == m:
        print(numpy.identity(n))
    else:
        print(numpy.eye(n,m))


if __name__ == '__main__':
    n , m = list(map(int, input().split()))
    print_eye_identity(n,m)
