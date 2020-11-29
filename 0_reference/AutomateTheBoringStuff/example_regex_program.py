#! python3

import re, pyperclip

# Create a regex for phone numbers
phoneRegex = re.compile(r"""
# 415-555-5555, 555-00000, (514) 555-0000, 555-5555 ext 12345, ext. 12345, x12345
(
((\d\d\d)|(\(\d\d\d\)))?      # area code (optional)
(\s|-)              # first seperator
\d\d\d              # first 3 digits
-                   # second seperator
\d\d\d\d            # last 4 digits
(((ext(\.)?\s)|x)   # extension word (optional)
 (\d{2,5}))?           # extension num (optional)
)
""", re.VERBOSE)


# Create a regex for email addresses
emailRegex = re.compile(r"""
# some.+_thing@something.com

[a-zA-Z0-9_.+]+      # name 
@                    # @ symbol
[a-zA-Z0-9_.+]+      # domain name


""", re.VERBOSE)

# Get the text off the clipboard
text = pyperclip.paste()


# TODO: Extract the email/phone from this text
extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)

allPhoneNumbers = []
for phoneNumbers in extractedPhone:
    allPhoneNumbers.append(phoneNumbers[0])

print(allPhoneNumbers)
print(extractedEmail)

# TODO: Copy extracted email/phone to the clipboard
results = "\n".join(allPhoneNumbers) + "\n" + "\n".join(extractedEmail)
pyperclip.copy(results)

# Arrowood, Tanya A	608-758-6075	Tanya.Arrowood@wisconsin.gov	CORRECTIONS DEPT OF
# Atwood, Jeffrey J	608-261-6780	Jeff.Atwood@SWIB.STATE.WI.US	INVESTMENT BOARD
# Blackwood, Allison A	414-750-1882	Allison.Blackwood@dot.wi.gov	TRANSPORTATION DEPT OF
