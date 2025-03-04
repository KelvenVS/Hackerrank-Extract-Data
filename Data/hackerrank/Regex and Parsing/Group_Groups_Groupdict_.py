import re

def first_rep(string):
    pattern = r"([a-zA-Z0-9])\1"
    
    m = re.search(pattern,string)
    
    if m is not None:
        return m.group(0)[0]
    else:
        return '-1'
        
if __name__ == '__main__':
    string = input()
    print(first_rep(string))
