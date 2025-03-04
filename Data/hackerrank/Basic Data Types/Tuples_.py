if __name__ == '__main__':
    #qtd de elmentos
    n = int(raw_input())

    #map
    t = list(map(int, raw_input().split()))

    aux = tuple(t)
    print(hash(aux))
