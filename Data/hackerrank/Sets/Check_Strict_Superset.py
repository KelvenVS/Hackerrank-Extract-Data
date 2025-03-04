def check_superset(set_a,other_set):
    return set_a.issuperset(other_set)

if __name__ == '__main__':
    set_a = set(map(int, input().split()))
    qty_sets = int(input())

    for _ in range(qty_sets):
        other_set = set(map(int, input().split()))
        bool_check = check_superset(set_a, other_set)
        if not bool_check:
            break 
    print(bool_check)
