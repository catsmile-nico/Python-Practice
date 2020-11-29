import re

message = "My number is 415-555-1011"

###Single group
#create regex object
phoneNumRegex = re.compile(r"\d\d\d-\d\d\d-\d\d\d\d")
mo = phoneNumRegex.search(message)
#get matched string
print(mo.group())

###Multiple group - using parenthesis to mark out where group begin and end
phoneNumRegex = re.compile(r"(\d\d\d)-(\d\d\d-\d\d\d\d)")
mo = phoneNumRegex.search(message)
print(mo.group())
print(mo.group(1))
print(mo.group(2))

#lookup literal parenthesis
phoneNumRegex2 = re.compile(r"\(\d\d\d\) (\d\d\d-\d\d\d\d)")
mo2 = phoneNumRegex2.search("My number is (415) 555-1011")
print(mo2.group())

#pipes
batRegex = re.compile(r"Bat(man|mobile|copter|bat)")
mo3 = batRegex.search("Batmobile lost a wheel")
print(mo3.group())
mo3 = batRegex.search("Batmotorcycle lost a wheel")
print(mo3 == None)
