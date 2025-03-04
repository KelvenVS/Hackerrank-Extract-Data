def is_subset(set_a,set_b):
    return set_a.issubset(set_b)

if __name__ ==  '__main__':
    qty_test = int(input())
    
    for _ in range(qty_test):
        len_a = int(input())
        set_a = set(map(int ,input().split()))
        len_b = int(input())
        set_b = set(map(int ,input().split()))
        
        print(is_subset(set_a,set_b))
