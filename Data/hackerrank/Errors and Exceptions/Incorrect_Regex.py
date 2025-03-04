import re

if __name__ == "__main__":
    n = int(input())
    for _ in range(n):
        try:
            boolean = bool(re.compile(input()))
            print(True)
        except re.error:
            print(False)
