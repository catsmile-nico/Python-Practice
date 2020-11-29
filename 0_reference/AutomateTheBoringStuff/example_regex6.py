import re

#search if starts with term
beginsWithHelloRegex = re.compile(r"^Hello")
mo = beginsWithHelloRegex.search("Hello there")
print(mo)
mo = beginsWithHelloRegex.search("He said hello")
print(mo == None)

#search if ends with term
endRegex = re.compile(r"world$")
mo = endRegex.search("Hello world")
print(mo)
mo = endRegex.search("Hello world now")
print(mo == None)


allDigitsRegex = re.compile(r"^\d+$")
mo = allDigitsRegex.search("871236")
print(mo)
mo = allDigitsRegex.search("8712x36")
print(mo == None)

#anything followed by term
atRegex = re.compile(r".at")
mo = atRegex.findall("the cat in the hat sat on the flat mat")
print(mo)
atRegex = re.compile(r".{1,2}at")
mo = atRegex.findall("the cat in the hat sat on the flat mat")
print(mo)


#find anything .*
msg = "First name: Test Last Name: Case"
print(msg.find(":"))

#return whatever is inside (.*)
nameRegex = re.compile(r"First name: (.*) Last Name: (.*)")
mo = nameRegex.findall(msg)
print(mo)

#non-greedy .*
nameRegex = re.compile(r"First name: (.*?) Last Name: (.*?)")
mo = nameRegex.findall(msg)
print(mo)

servemsg = "<To serve humans> for dinner.>"
nonGreedyRegex = re.compile(r"<(.*?)>")
mo = nonGreedyRegex.findall(servemsg)
print(mo)

nonGreedyRegex = re.compile(r"<(.*)>")
mo = nonGreedyRegex.findall(servemsg)
print(mo)

prime = "Search the public trust.\nProtect the innocent.\nUphold the law."
dotStar = re.compile(r".*")
mo = dotStar.search(prime)
print(mo)

#configure compile function
dotStar = re.compile(r".*", re.DOTALL) #greedy dotStar match
mo = dotStar.search(prime)
print(mo)

vowelRegex2 = re.compile(r"[aeiou]", re.I) #ignore case
mo = vowelRegex2.findall("Ey, why does your programming book talk about RoboCop so much?")
print(mo)
