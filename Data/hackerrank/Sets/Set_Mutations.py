def cmd_py(set_a,scripts):
    
    for script in scripts:
        tpl_command , set_aux = script
        command , _ = tpl_command
        getattr(set_a, command)(set_aux)

    return sum(set_a)

if __name__ == '__main__':
    len_set_a = int(input())
    set_a = set(map(int, input().split()))
    
    qty_operation_set = int(input())
    
    script = []
    for _ in range(qty_operation_set):
        command = tuple(input().split())
        set_x = set(map(int, input().split()))
        script.append((command,set_x))
    
    print(cmd_py(set_a,script))
