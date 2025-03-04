def sample_design(dimension):
    #| . -
    n , m = dimension
    
    struct1 = '.|.'
    line_str = n-2
    #1 3 5 7 9 11
    str_central = 'WELCOME'
    
    #Cone
    for i in range(1,line_str+1,2):
        struct_line = struct1*i
        bar_len = (m - len(struct_line)) // 2
        bars = '-'*bar_len
        print(f'{bars}{struct_line}{bars}')
    
    #Central line
    bar_len = (m - len(str_central)) // 2
    bars = '-'*bar_len
    print(f'{bars}{str_central}{bars}')
    
    #Cone Inversed
    for i in range(line_str, 0,-2):
        struct_line = struct1*i
        bar_len = (m - len(struct_line)) // 2
        bars = '-'*bar_len
        print(f'{bars}{struct_line}{bars}')
            

if __name__ == "__main__":
    dimension = tuple(list(map(int,input().split())))
    sample_design(dimension)
