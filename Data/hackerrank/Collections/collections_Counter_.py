from collections import Counter

def sum_orders(orders,stock):
    stock = Counter(stock)
    
    cash_earned = 0
    for shoes , price in orders:
        if stock[shoes] > 0:
            stock[shoes]-=1
            cash_earned+=int(price)
            
    print(cash_earned)
        
if __name__ == '__main__':
    n_shoes = int(input())
    shoes_stock = input().split()
    n_costumers =  int(input())
    
    orders = []
    for _ in range(n_costumers):
        size , price = input().split()
        orders.append((size,price))
    
    sum_orders(orders,shoes_stock)
    
