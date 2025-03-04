from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Start :", tag)
        for attr, value in attrs:
            print(f"-> {attr} > {value if value else 'None'}")

    def handle_endtag(self, tag):
        print("End   :", tag)

    def handle_startendtag(self, tag, attrs):
        print("Empty :", tag)
        for attr, value in attrs:
            print(f"-> {attr} > {value if value else 'None'}")

if __name__ == '__main__':
    lines = int(input())
    
    html_text = ''
    for _ in range(lines):
        html_text += input()
    
    parser = MyHTMLParser()
    parser.feed(html_text)
