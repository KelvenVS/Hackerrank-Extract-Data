def handler_list(N):
    hlist = []
    for _ in range(N):
        command = input().split()
        if command[0] == 'insert':
            hlist.insert(int(command[1]), int(command[2]))
        elif command[0] == 'print':   
            print(hlist)
        elif command[0] == 'remove':        
            hlist.remove(int(command[1]))
        elif command[0] == 'append':
            hlist.append(int(command[1])) 
        elif command[0] == 'sort':
            hlist.sort()
        elif command[0] == 'pop':
            hlist.pop()
        elif command[0] == 'reverse':
            hlist.reverse()

if __name__ == '__main__':
    N = int(input())
    handler_list(N)
