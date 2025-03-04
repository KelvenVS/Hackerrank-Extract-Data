qty = input()
arr = list(map(int, input().split()))
print(all(elem >= 0 for elem in arr) and any(str(elem)[::-1]==str(elem) for elem in arr))
