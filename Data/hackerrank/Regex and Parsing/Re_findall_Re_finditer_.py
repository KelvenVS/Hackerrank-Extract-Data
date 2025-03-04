import re

def finder(pattern,string):
    results = re.findall(pattern,string)
    
    if results:
        for elem in results:
            print(elem)
    else:
        print('-1')  

if __name__ == '__main__':
    string = input()
    pattern = r"(?<=[^aeiouAEIOU])([aeiouAEIOU]{2,})(?=[^aeiouAEIOU])"
    finder(pattern,string)
