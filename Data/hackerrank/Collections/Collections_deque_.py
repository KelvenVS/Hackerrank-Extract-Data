from collections import deque

def cmd_col(script):
    d = deque()
    
    for command in script:
        if len(command) == 1:
            getattr(d,command[0])()
        else:
            getattr(d,command[0])(command[1])
            
    return ' '.join(d)


if __name__ ==  '__main__':
    qty_commands = int(input())
    
    list_com = []
    for _ in range(qty_commands):
        command = input().split()
        list_com.append(command)
    
    print(cmd_col(list_com))
    
