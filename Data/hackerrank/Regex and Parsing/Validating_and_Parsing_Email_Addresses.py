import email.utils
import re

def validate_email(aux_email):
    name , adress = email.utils.parseaddr(aux_email)
    pattern = r"^[A-Za-z][A-Za-z0-9._-]*@[A-Za-z]+\.[A-Za-z]{1,3}$"
    
    re_check = re.match(pattern,adress)
    
    if re_check:
        print(aux_email)
        
if __name__ == '__main__':
    lines = int(input())
    
    for _ in range(lines):
        aux_email = input()
        validate_email(aux_email)
