# https://www.hackerrank.com/challenges/detect-html-tags-attributes-and-attribute-values/problem?isFullScreen=true
# Problem : Print the HTML tags, attributes and attribute values

# Sample Input
# 9
# <head>
# <title>HTML</title>
# </head>
# <object type="application/x-flash" 
#   data="your-file.swf" 
#   width="0" height="0">
#   <!-- <param name="movie" value="your-file.swf" /> -->
#   <param name="quality" value="high"/>
# </object>

# Sample Output
# head
# title
# object
# -> type > application/x-flash
# -> data > your-file.swf
# -> width > 0
# -> height > 0 
# param
# -> name > quality
# -> value > high

from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        for _ in attrs:
            print("->", _[0], ">", _[1])

parser = MyHTMLParser()
for _ in range(int(input())):
    parser.feed(input())
parser.close()