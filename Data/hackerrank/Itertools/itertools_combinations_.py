from itertools import combinations

def comb_func(prompt):
    string , r = prompt
    
    string = list(string)
    string.sort()
    
    comb_list = []
    for i in range(1,int(r)+1):
        comb_list+= list(combinations(string,int(i)))
    
    for elem in comb_list:
        print(''.join(elem))
    

if __name__ ==  '__main__':
    prompt = tuple(input().split())
    comb_func(prompt)
