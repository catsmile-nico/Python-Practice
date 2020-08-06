import re

#multiple groups
phoneRegex = re.compile(r"(\d\d\d)-(\d\d\d-\d\d\d\d)")
msg = "555-523-1234 aiudasgduiassd 123-331-5341"
print ("1 Level: " + str(phoneRegex.findall(msg)))

phoneRegex = re.compile(r"((\d\d\d)-(\d\d\d-\d\d\d\d))")
msg = "555-523-1234 aiudasgduiassd 123-331-5341"
print ("2 Level: " + str(phoneRegex.findall(msg)))


#piping
digitRegex = re.compile(r"(0|1|2|3|4|5|6|7|8|9)")
digitRegex = re.compile(r"(\d)")

#character classes
digitRegex = re.compile(r"(\d)")
notDigitRegex = re.compile(r"(\D)")
wordRegex = re.compile(r"(\w)") #any letter, numeric, underscore
notWordRegex = re.compile(r"(\W)")
whitespaceRegex = re.compile(r"(\s)")
notWhitespaceRegex = re.compile(r"(\S)")

import pprint
#combinations
lyrics = "12 Drummers Drumming, 11 Pipers Piping, 10 Lords a Leaping, 9 Ladies Dancing, 8 Maids a Milking, 7 Swans a Swimming, 6 Geese a Laying, 5 Golden Rings, 4 Calling Birds, 3 French Hens, 2 Turtle Doves, and 1 Partridge in a Pear Tree"
xmasRegex = re.compile(r"\d+\s\w+")
mo = xmasRegex.findall(lyrics)
pprint.pprint (mo)
xmasRegex = re.compile(r"(\d+(\s\w+)+)")
mo = xmasRegex.findall(lyrics)
pprint.pprint (mo)

#customized character class
regexObj = re.compile(r"[a-zA-Z]") 
vowelRegex = re.compile(r"[aeiouAEIOU]") #same as r"(a|e|i|o|u)"
mo = vowelRegex.findall("Robocop Eats Baby Food.")
print(mo)

doubleVowelRegex = re.compile(r"[aeiouAEIOU]{2}")
mo = doubleVowelRegex.findall("Robocop Eats Baby Food.")
print(mo)

notVowelRegex = re.compile(r"[^aeiouAEIOU]")
mo = notVowelRegex.findall("Robocop Eats Baby Food.")
print(mo)
