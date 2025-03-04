from itertools import combinations

def possibilities(string,k):
    comb_list = list(combinations(string,k))
    #print(comb_list)
    
    count = 0
    for elem in comb_list:
        #Check first element of string on elem
        #or Check 'char'
        if 'a' in elem:
            count+=1
    result = count/len(comb_list)
    print(f'{result:.4f}')

if __name__ == '__main__':
    n  = input()
    string = ''.join(input().split())
    k = int(input())
    
    possibilities(string,k)
