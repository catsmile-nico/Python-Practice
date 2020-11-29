import re

namesRegex = re.compile(r"Agent \w+")
mo = namesRegex.findall("Agent Alice gave the secret documents to Agent Bob.")
print (mo)

# replace occurances with a word
mo = namesRegex.sub("REDACTED","Agent Alice gave the secret documents to Agent Bob.")
print (mo)

# replace after group
namesRegex = re.compile(r"A(gent) (\w)\w*")
mo = namesRegex.findall("Agent Alice gave the secret documents to Agent Bob.")
print (mo)

# replace occurances with censor
# \1 \2 is the group no. to replace from
mo = namesRegex.sub(r"A\1****","Agent Alice gave the secret documents to Agent Bob.")
print (mo)

mo = namesRegex.sub(r"Agent \2****","Agent Alice gave the secret documents to Agent Bob.")
print (mo)
