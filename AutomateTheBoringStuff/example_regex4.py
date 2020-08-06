import re

#the ? indicates the group can appear 0 or 1 times
batRegex = re.compile(r"Bat(wo)?man")
mo = batRegex.search("The Adventures of Batman")
print(mo.group())
mo = batRegex.search("The Adventures of Batwoman")
print(mo.group())
mo = batRegex.search("The Adventures of Batwowoman")
print(mo == None)

#phone example
phoneRegex = re.compile(r"\d\d\d-\d\d\d-\d\d\d\d")
mo = phoneRegex.search("My phone number is 415-555-1234. Call me tmr")
print(mo.group())
mo = phoneRegex.search("My phone number is 555-1234. Call me tmr")
print(mo == None)

phoneRegex = re.compile(r"(\d\d\d-)?\d\d\d-\d\d\d\d")
mo = phoneRegex.search("My phone number is 555-1234. Call me tmr")
print(mo.group())

#the * indicates group can appear 0 or more times
batRegex = re.compile(r"Bat(wo)*man")
mo = batRegex.search("The Adventures of Batman")
print(mo.group())
mo = batRegex.search("The Adventures of Batwoman")
print(mo.group())
mo = batRegex.search("The Adventures of Batwowoman")
print(mo.group())

#the + indicates group can appear 1 or more times
batRegex = re.compile(r"Bat(wo)+man")
mo = batRegex.search("The Adventures of Batman")
print(mo == None)
mo = batRegex.search("The Adventures of Batwoman")
print(mo.group())
mo = batRegex.search("The Adventures of Batwowoman")
print(mo.group())

#match characters that are used in regex
regex = re.compile(r"\+\*\?")
mo = regex.search("I learnt about +*? regex syntax")
print(mo.group())

#match exactly x times
regex = re.compile(r"(Ha){3}")
mo = regex.search("He said 'HaHa'")
print(mo == None)
mo = regex.search("He said 'HaHaHa'")
print(mo.group())
mo = regex.search("He said 'HaHaHaHa'")
print(mo.group())

#match example x times - Groups
regex = re.compile(r"((\d\d\d-)?\d\d\d-\d\d\d\d(,)?){3}")
mo = regex.search("Mason: 555-123-4123,123-532-5423")
print(mo == None)
mo = regex.search("Mason: 415-555-1234,555-123-4123,123-532-5423")
print(mo.group())

#match x~x times
regex = re.compile(r"(Ha){3,5}")
mo = regex.search("He said 'HaHa'")
print(mo == None)
mo = regex.search("He said 'HaHaHa'")
print(mo.group())
mo = regex.search("He said 'HaHaHaHa'")
print(mo.group())
mo = regex.search("He said 'HaHaHaHaHa'")
print(mo.group())
mo = regex.search("He said 'HaHaHaHaHaHa'") #only match first 5
print(mo.group())

#match x or more times
regex = re.compile(r"(Ha){3,}")
mo = regex.search("He said 'HaHaHa'")
print(mo.group())
mo = regex.search("He said 'HaHaHaHa'")
print(mo.group())
mo = regex.search("He said 'HaHaHaHaHa'")
print(mo.group())
mo = regex.search("He said 'HaHaHaHaHaHa'")
print(mo.group())

#match smallest/fastest possible match
regex = re.compile(r"(\d){3,5}") 
mo = regex.search("1234567890") #returns first match found
print(mo.group())
regex = re.compile(r"(\d){3,5}?")
mo = regex.search("1234567890") #returns as soon as a match found
print(mo.group())
