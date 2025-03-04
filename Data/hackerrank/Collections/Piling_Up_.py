from collections import deque

def make_tower(blocks, qty_blocks):
    deq_blocks = deque(blocks)
    last_block = float('inf')
    
    while deq_blocks:
        if deq_blocks[0] >= deq_blocks[-1]:
            current_block = deq_blocks.popleft()
        else:
            current_block = deq_blocks.pop()
        
        if current_block > last_block:
            print('No')
            return
        
        last_block = current_block
        
    print('Yes')

if __name__ == '__main__':
    num_teste = int(input())
    
    for _ in range(num_teste):
        qty_blocks = int(input())
        blocks = list(map(int, input().split()))
        
        make_tower(blocks, qty_blocks)
