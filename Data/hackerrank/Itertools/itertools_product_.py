from itertools import product

def product_mtx(a,b):
    prod = list(product(*[a,b]))
    return " ".join(f"({x}, {y})" for x, y in prod)
    
if __name__ == '__main__':
    a =  input().split()
    b =  input().split()
    
    print(product_mtx(a,b))
