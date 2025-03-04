import string   

def print_rangoli(size):

    alphabet = list(string.ascii_lowercase)[:size]
    aph_sliced = alphabet[:size]
    aph_sli_rev = list(reversed(aph_sliced))
    
    rangnoli_list = []
    
    center_line = '-'.join(aph_sli_rev + aph_sliced[1:])
    
    #Cone Topo
    for i in range(size-1):
        
        center_char = aph_sli_rev[i]
        side1 = aph_sli_rev[:i-size]
        side2 = aph_sliced[size-i:]
        
        line_rangoli = '-'.join(side1 + [center_char] + side2)
        
        i = len(line_rangoli)
        while i < len(center_line):
            line_rangoli =  '-' + line_rangoli + '-'
            i+=2
        print(line_rangoli)
        
    #Cone Baixo
    for i in range(size-1,-1,-1):
        center_char = aph_sli_rev[i]
        side1 = aph_sli_rev[:i-size]
        side2 = aph_sliced[size-i:]

        line_rangoli = '-'.join(side1 + [center_char] + side2)

        i = len(line_rangoli)
        while i < len(center_line):
            line_rangoli =  '-' + line_rangoli + '-'
            i+=2
        print(line_rangoli)    
    
        
        
