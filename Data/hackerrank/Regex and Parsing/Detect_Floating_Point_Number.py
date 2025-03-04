import re

def chk_float(string):
    patern = r"^[+-]?(\d*\.\d+|\.\d+)$"
    return print(bool(re.findall(patern,string)))

if __name__ == "__main__":
    for _ in range(int(input())):
        chk_float(input())
