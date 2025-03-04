import re

def start_end(string,see):
    
    matches = list(re.finditer(f"(?=({see}))",string))
    
    if matches:
        for _ in matches:
            print((_.end(), _.start() + len(see) - 1 ))
    else:
        print((-1, -1))
        
if __name__ == '__main__':
    s = input()
    k = input()
    
    start_end(s,k)
