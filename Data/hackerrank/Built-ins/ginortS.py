def sorting(lst):
    
    lower, upper, odd, even = [], [], [], []

    for elem in lst:
        if elem.isupper():
            upper.append(elem)
        elif elem.islower():
            lower.append(elem)
        elif elem.isnumeric():
            (even if int(elem) % 2 == 0 else odd).append(elem) 
                    
    print(''.join(sorted(lower) + sorted(upper) + sorted(odd) + sorted(even)))
    
if __name__ == '__main__':
    str_list = list(input())
    sorting(str_list)
