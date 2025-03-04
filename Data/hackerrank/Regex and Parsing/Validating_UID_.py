import re

def check_UID(string):
    pattern = r'^(?=(?:.*[A-Z]){2})(?=(?:.*\d){3})(?!.*(.).*\1)[A-Za-z0-9]{10}$'
    check = re.match(pattern,string)
    
    if check:
        print('Valid')
    else:
        print('Invalid')

if __name__ == '__main__':
    lines = int(input())
    
    for _ in range(lines):
        check_UID(input())
