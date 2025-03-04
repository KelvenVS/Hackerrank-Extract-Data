import re

def check_number(number):
    pattern = r'^[987][\d]{9}$'
    check = re.match(pattern,number)
    return 'YES' if check else 'NO'
    
if __name__ == '__main__':
    lines = int(input())
    
    for _ in range(lines):
        print(check_number(''.join(input().split())))
