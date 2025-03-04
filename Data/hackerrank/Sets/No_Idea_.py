def rabbit_hole(comp,a,b):
    hapiness = 0
    for elem in comp:
        if elem in a:
            hapiness+=1
        elif elem in b:
            hapiness-=1
    print(hapiness)

if __name__ ==  '__main__':
    prompt = input().split()
    n_integers = input().split()
    #M
    a_integers = set(input().split())
    b_integers = set(input().split())
    
    rabbit_hole(n_integers,a_integers,b_integers)
