cube = lambda x: x**3

def fibonacci(n):   
    
    fibolist = []
    if n == 0:
        return fibolist
    elif n == 1:
        fibolist = [0]
        return fibolist
    else:
        fibolist = [0, 1]
        aux = 0
        for i in range(0,n-2):
            aux = fibolist[i] + fibolist[i+1]
            fibolist.append(aux)
        return fibolist
    
