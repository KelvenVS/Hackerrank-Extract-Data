from itertools import combinations_with_replacement

def comb_with_replace(prompt):
    string , r = prompt
    
    lex_string = list(string)
    lex_string.sort()
    
    rep_list = list(combinations_with_replacement(lex_string,int(r)))
    
    for elem in rep_list:
        print(''.join(elem))
    
if __name__ == '__main__':
    prompt = tuple(input().split())
    comb_with_replace(prompt)
    
    
    
