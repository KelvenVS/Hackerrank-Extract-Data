def count_substring(string, sub_string):
    aux_string = list(string)
    
    count = 0
    for i in range(len(aux_string)):
        sliced_str = "".join(aux_string[i:i+len(sub_string)])
        if  sliced_str == sub_string:
            count+=1
    return count
            
        

