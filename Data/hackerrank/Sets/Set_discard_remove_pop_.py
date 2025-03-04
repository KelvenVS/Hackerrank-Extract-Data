def cmd_py(lst,commands):
    
    for script in commands:
        if len(script) == 1:
            command = script[0]
            getattr(lst,command)()
        else:
            command , key = script
            getattr(lst, command)(int(key))
    
    print(sum(lst))
    
if __name__ == '__main__':
    
    size_set = int(input())
    lst = set(map(int, input().split()))
    
    lines_commands = int(input())
    
    commands = []
    for _ in range(lines_commands):
        commands.append(tuple(input().split()))
    cmd_py(lst,commands)
