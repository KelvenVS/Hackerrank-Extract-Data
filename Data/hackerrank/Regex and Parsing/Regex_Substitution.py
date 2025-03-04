import re

def sub_logic(string):
    string = re.sub(r"(?<= )&&(?= )", "and", string)
    string = re.sub(r" \|\| ", " or ", string)
    return string

if __name__ == '__main__':
    lines = int(input())
    html_text = '\n'.join(sub_logic(input()) for _ in range(lines))
    print(html_text)
