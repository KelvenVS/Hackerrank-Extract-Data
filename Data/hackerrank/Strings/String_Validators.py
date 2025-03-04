def str_validator(s):
    aux_tuple = [
        (str.isalnum,False),
        (str.isalpha,False),
        (str.isdigit,False),
        (str.islower,False),
        (str.isupper,False)
    ]
    
    for char in list(s):
        for i in range(len(aux_tuple)):
            method , key = aux_tuple[i]
            if method(char):
                aux_tuple[i] = (method ,True)
    
    for method,value in aux_tuple:
        print(value)

            
if __name__ == '__main__':
    s = input()
    str_validator(s)
