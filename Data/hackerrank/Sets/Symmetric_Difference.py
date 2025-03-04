def symetric_diff(a,b):
    new_set = set()
    new_set.update(b.difference(a))
    new_set.update(a.difference(b))
    
    order_set = sorted(new_set)
    for item in order_set:
        print(item)
    
if __name__ == '__main__':
    m_size = int(input())
    m = set(map(int ,input().split()))
    n_size = int(input())
    n = set(map(int ,input().split()))
    
    symetric_diff(m,n)
