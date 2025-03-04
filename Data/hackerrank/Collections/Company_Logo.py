from collections import Counter

def count_elem(string):
    string = list(string)
    string.sort()
    c =  Counter(string).most_common(3)
    
    for tuple_char in c:
        char , qty = tuple_char
        print(char , qty)

if __name__ == '__main__':
    s = input()
    count_elem(s)
