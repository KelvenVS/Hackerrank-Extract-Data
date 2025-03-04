import re

def find_hex_collors(text):
    pattern = "(?<!#)[#][0-9A-Fa-f]{3,6}(?![{A-Za-z0-9 ])"
    
    hex_collors = re.findall(pattern, text)
    
    for item in hex_collors:
        print(item)

if __name__ == '__main__':
    lines = int(input())-1
    
    text = ''
    for _ in range(lines):
        text+= input()

    find_hex_collors(text)
