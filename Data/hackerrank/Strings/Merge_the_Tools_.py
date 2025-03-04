def merge_the_tools(string, k):

    for i in range(0,len(string),k):
        sub_string = ''.join(string[i:i+k])
        
        seen = []
        for char in sub_string:
            if char not in seen:
                seen.append(char)
        print(''.join(seen))
        
    

