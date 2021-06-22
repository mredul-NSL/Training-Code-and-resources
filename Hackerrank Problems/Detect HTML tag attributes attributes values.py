from html.parser import HTMLParser

# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print (tag)
        for i in attrs:
            print ('->',i[0],'>',i[1])
    def handle_startendtag(self, tag, attrs):
        print (tag)
        for i in attrs:
            print ('->',i[0],'>',i[1])

# instantiate the parser and fed it some HTML
parser = MyHTMLParser()

line = int(input())
sr = ""

for i in range(line):
    sr += input()
        
parser.feed(sr)