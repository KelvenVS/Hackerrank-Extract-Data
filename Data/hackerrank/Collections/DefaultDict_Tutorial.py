from collections import defaultdict

def count_group(dictionary):
    result = defaultdict(list)
    
    for i in range(len(dictionary['A'])):
        char = dictionary['A'][i]
        result[char].append(i+1)
        
    for char in dictionary['B']:
        if char in result:
            print(' '.join(map(str,result[char])))
        else:
            print(-1)


if __name__ ==  '__main__':
    groups = list(map(int,input().split()))
    group_size = sum(groups)
    group_name = ['A','B']
    
    d = defaultdict(list)
    for name,group in zip(group_name ,groups):
        for _ in range(group):
            aux = input()
            d[f'{name}'].append(aux)
    
    count_group(d)
    
