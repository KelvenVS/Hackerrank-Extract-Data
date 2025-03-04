from itertools import permutations

def permutations_tool(promt):
    string , r = prompt
    
    permut_list = list(permutations(string,int(r)))
    permut_list.sort()
    for elem in permut_list:
        print(''.join(elem))
    

if __name__ == '__main__':
    prompt = tuple(input().split())
    permutations_tool(prompt)
    
