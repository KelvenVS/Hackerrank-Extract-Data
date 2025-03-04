if __name__ == '__main__':
    lines = int(input())
    
    for _ in range(lines):
        x , y = input().split()
        
        try:
            result = int(x) // int(y)
            print(result)
        except (ZeroDivisionError , ValueError) as e:
            print('Error Code:',e)
            
