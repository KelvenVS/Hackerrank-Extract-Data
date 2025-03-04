from collections import namedtuple

def average(list_obj):
    sum_obj = sum(int(obj.MARKS) for obj in list_obj)
    avg = sum_obj / len(list_obj)
    print(f"{avg:.2f}")

if __name__ == '__main__':
    qty_ids = int(input())
    names_tpl = input().split()
    
    Std_sheet = namedtuple('Std_sheet',names_tpl)
    
    aux = []
    for _ in range(qty_ids):
        data = input().split()
        obj = Std_sheet(*data)
        aux.append(obj)
    
    average(aux)
