from itertools import groupby

def compress_stirng(prompt):
    
    group_tuples = []
    for elem ,qty in groupby(prompt):
        qty = len(list(qty))
        group_tuples.append((qty,elem))
    print(' '.join(f'({x}, {y})' for x,y in group_tuples))
    
if __name__ == '__main__':
    prompt = input()
    compress_stirng(prompt)
