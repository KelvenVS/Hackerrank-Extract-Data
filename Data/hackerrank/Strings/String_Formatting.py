def print_formatted(number):
    padding = len(bin(number)[2:])
    
    for i in range(1,number+1):
        num_oct = oct(i)[2:].upper()
        num_hex = hex(i)[2:].upper()
        num_bin = bin(i)[2:].upper()
        
        print(f'{i:>{padding}} {num_oct:>{padding}} {num_hex:>{padding}} {num_bin:>{padding}}')

