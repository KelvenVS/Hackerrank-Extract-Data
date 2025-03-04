def news_qty(list_a,list_b):
    return len(list_a.intersection(list_b))


if __name__ == '__main__':
    len_list_a = int(input())
    list_a = set(map(int, input().split()))
    len_list_b = int(input())
    list_b = set(map(int, input().split()))
    
    print(news_qty(list_a,list_b))
