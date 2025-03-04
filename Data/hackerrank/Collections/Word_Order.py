from collections import Counter


def counter_appears(lst):
    word_count = Counter(lst)
    
    print(len(word_count))
    for _ in word_count.values():
        print(_ , end = ' ')
        
if __name__ ==  '__main__':
    qty_lines = int(input())
    
    lst =[]
    for _ in range(qty_lines):
        lst.append(input())
        
    counter_appears(lst)
