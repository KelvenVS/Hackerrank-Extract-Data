from itertools import product

def maxize_it(lst,module):
    
    #Convert string in int
    list_int = []
    for i in range(len(lst)):
        sublist_int = list(map(int, lst[i][1:]))
        list_int.append(sublist_int)
        
    max_val = 0
    for combination in product(*list_int):
        sum_quares = sum(x ** 2 for x in combination)
        value = sum_quares % module
        
        if value > max_val:
            max_val = value
        
    print(max_val)


if __name__ == '__main__':
    k , module = map(int, input().split())
    lst = [input().split() for i in range(k)]
    maxize_it(lst,module)
