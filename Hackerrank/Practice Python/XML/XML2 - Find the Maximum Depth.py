# https://www.hackerrank.com/challenges/xml2-find-the-maximum-depth/problem?isFullScreen=true
# Problem : Find maximum depth of XML elements

# Sample Input
# 6
# <feed xml:lang='en'>
#     <title>HackerRank</title>
#     <subtitle lang='en'>Programming challenges</subtitle>
#     <link rel='alternate' type='text/html' href='http://hackerrank.com/'/>
#     <updated>2013-12-25T12:00:00</updated>
# </feed>

# Sample Output
# 1


import xml.etree.ElementTree as etree

maxdepth = 0
def depth(elem, level):
    global maxdepth
    # your code goes here
    if (maxdepth < level+1):
        maxdepth = level+1
    for _ in elem:
        depth(_, level+1)

if __name__ == '__main__':
    n = int(input())
    xml = ""
    for i in range(n):
        xml =  xml + input() + "\n"
    tree = etree.ElementTree(etree.fromstring(xml))
    depth(tree.getroot(), -1)
    print(maxdepth)