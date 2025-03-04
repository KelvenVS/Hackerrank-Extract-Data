from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self , tag , attrs):
        print(tag)
        for attr, value in attrs:
            print(f"-> {attr} > {value if value else 'None'}")
    
    def handle_startendtag(self, tag , attrs):
        print(tag)
        for attr, value in attrs:
            print(f"-> {attr} > {value if value else 'None'}")

if __name__ == '__main__':
    lines = int(input())
    
    html_text = ''
    for _ in range(lines):
        html_text+= input().rstrip()
        html_text+= '\n'

    parser = MyHTMLParser()
    parser.feed(html_text)
    parser.close()
    
    
