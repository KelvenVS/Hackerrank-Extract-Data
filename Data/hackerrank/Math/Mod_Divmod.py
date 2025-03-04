if __name__ ==  '__main__':
    a = int(input())
    b = int(input())
    
    quotient , remainder = divmod(a,b)
    print(quotient)
    print(remainder)
    print((quotient,remainder))
