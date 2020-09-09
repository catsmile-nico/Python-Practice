# https://www.hackerrank.com/challenges/html-parser-part-1/problem?isFullScreen=true
# https://docs.python.org/3/library/html.parser.html
# https://stackoverflow.com/questions/25675943/how-can-i-concatenate-str-and-int-objects
# Problem : Print the HTML tags, attributes and attribute values

# Sample Input
# 2
# <html><head><title>HTML Parser - I</title></head>
# <body data-modal-target class='1'><h1>HackerRank</h1><br /></body></html>

# Sample Output
# Start : html
# Start : head
# Start : title
# End   : title
# End   : head
# Start : body
# -> data-modal-target > None
# -> class > 1
# Start : h1
# End   : h1
# Empty : br
# End   : body
# End   : html

from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Start :", tag)
        for _ in attrs:
            print("->", _[0], ">", _[1])
    def handle_endtag(self, tag):
        print("End   :", tag)
    def handle_startendtag(self, tag, attrs):
        print("Empty :", tag)
        for _ in attrs:
            print("->", _[0], ">", _[1])

parser = MyHTMLParser()
for _ in range(int(input())):
    parser.feed(input())
parser.close()