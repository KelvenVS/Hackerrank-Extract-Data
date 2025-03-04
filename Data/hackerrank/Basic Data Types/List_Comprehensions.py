def fctn1(xs,ys,zs,n):
    aux_list = []
    
    for x in range(0,xs+1):
        for y in range(0,ys+1):
            for z in range(0,zs+1):
                if x+y+z != n: 
                    aux_list.append([x,y,z])     
                        
    return print(aux_list)

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    fctn1(x,y,z,n)
