# https://www.hackerrank.com/challenges/xml-1-find-the-score/problem?isFullScreen=true
# Refernce : https://docs.python.org/3/library/xml.etree.elementtree.html
# Problem : Output the number of attributes of a given XML document.

# NOTE : In terminal after pasting Sample Input, on a newline press Ctrl+Z, then press ENTER again.
# Sample Input
# 6
# <feed xml:lang='en'>
#     <title>HackerRank</title>
#     <subtitle lang='en'>Programming challenges</subtitle>
#     <link rel='alternate' type='text/html' href='http://hackerrank.com/'/>
#     <updated>2013-12-25T12:00:00</updated>
# </feed>

# Sample Output
# 5


import sys
import xml.etree.ElementTree as etree

def get_attr_number(node):
    # your code goes here
    # for _ in node.iter():
        # print(_.attrib)        
    return sum(len(_.attrib) for _ in node.iter())

if __name__ == '__main__':
    sys.stdin.readline()
    xml = sys.stdin.read()
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    print(get_attr_number(root))