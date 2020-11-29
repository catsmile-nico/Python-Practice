import re

message = "Call me 415-555-1011 tomorrow, or at 415-555-9999 for my office line"

#create regex object
phoneNumRegex = re.compile(r"\d\d\d-\d\d\d-\d\d\d\d")
mo = phoneNumRegex.search(message)
#get matched string
print(mo.group())
mo = phoneNumRegex.findall(message)
print(mo)
