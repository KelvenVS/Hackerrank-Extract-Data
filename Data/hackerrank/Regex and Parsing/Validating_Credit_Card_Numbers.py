import re

def check_card(string):
    
    clean_number = string.replace("-", "")
    if re.search(r"(\d)\1{3}", clean_number):
        return "Invalid"
    
    pattern = r"^(?!.*(\d)(\1{3}))[456][0-9]{3}-?[0-9]{4}-?[0-9]{4}-?[0-9]{4}$"
    check = re.match(pattern,string)
        
    return 'Valid' if check else 'Invalid'
    
if __name__ == '__main__':
    lines = int(input())
    
    for _ in range(lines):
        print(check_card(input()))
