from collections import OrderedDict

if __name__ == '__main__':
    qty_orders = int(input())
    
    ord_dict = OrderedDict()
    
    for _ in range(qty_orders):
        *item_name, price = input().split()
        item_name = ' '.join(item_name)
        price = int(price)
        
        ord_dict[item_name] = ord_dict.get(item_name, 0) + price
        
    for item, total_price in ord_dict.items():
        print(item, total_price)
