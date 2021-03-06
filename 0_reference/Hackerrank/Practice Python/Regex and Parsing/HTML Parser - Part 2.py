# https://www.hackerrank.com/challenges/html-parser-part-2/problem?isFullScreen=true
# Problem : Print the single-line comments, multi-line comments and the data

# Sample Input
# 4
# <!--[if IE 9]>IE9-specific content
# <![endif]-->
# <div> Welcome to HackerRank</div>
# <!--[if IE 9]>IE9-specific content<![endif]-->

# Sample Output
# >>> Multi-line Comment
# [if IE 9]>IE9-specific content
# <![endif]
# >>> Data
#  Welcome to HackerRank
# >>> Single-line Comment
# [if IE 9]>IE9-specific content<![endif]


from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_comment(self, data):
        print(">>> Multi-line Comment" if "\n" in data else ">>> Single-line Comment" )
        print(data)
    def handle_data(self, data):
        if len(data.strip()) > 0:
            print(">>> Data\n" + data)


html = ""       
for i in range(int(input())):
    html += input().rstrip()
    html += '\n'
    
parser = MyHTMLParser()
parser.feed(html)
parser.close()