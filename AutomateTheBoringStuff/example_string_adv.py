#escape characters
print('Single quote \' Single quote')
print("Double quote \" Double quote")
print('Tab\tTab')
print('Newline\nNewline')
print('Backslash\\Backslash')

#raw string
print(r'raw string')
print(r'raw string\'s backslash')

#multiline string
print("""multiline string
asd
asd
asd
asd
asd
""")

gigantic = """many string
asd
asd
asd
asd
asd
"""

print(gigantic)

#string manipulation
spam = "hellow world"
print(spam)
print(spam[0])
print(spam[1:5])
print("x" in spam)
print("low" in spam)
print("HELLO" in spam)
print(str("HELLO").lower() in spam)
