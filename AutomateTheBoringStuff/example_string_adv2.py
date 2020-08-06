# Upper/lower case
spam = "Hellow world"
spam2 = "Hellow World"
print(spam.upper())
print(spam.lower())

answer = input("are you fine\n")

print (answer.lower() == "yes")

# checkcase
print(spam.islower())
print(spam.isupper())
print(spam.isalpha()) #letter only
print(spam.isalnum()) #letter and number only
print(spam.isdecimal()) #numbers only
print(spam.isspace()) #space only
print(spam.istitle()) #first letter of each word caps
print(spam2.istitle())

print(spam.startswith("Hello"))
print(spam.endswith("orld"))

#join list with string seperator
print(",".join(["cats","rats","bats"]))

#split
print("my name is john".split())
print("my name is john".split("m"))

#left / right justify, center
print("Hello".rjust(19))
print("Hello".rjust(19,"*"))
print("Helasdasdao".rjust(19,"*")) #its just 19 spaces between left and right
print("Hello".ljust(19))
print("Hello".ljust(19,"*"))
print("Helasdasdao".ljust(19,"*")) #its just 19 spaces between left and right
print("Hello".center(19))
print("Hello".center(19,"*"))
print("Haaaaaaaello".center(19,"*")) #its just 19 spaces between left and right

#remove whitespace or specfic char
print(spam.strip()) #doesnt work for whitespace inbetween string
print("Hello".rjust(19).strip())
print("Hello".rjust(19,"*").strip()) #only works for spaces justified
print("Hello".rjust(19,"*").strip("*"))
print("Hello".center(19,"*").rstrip("*"))
print("Hello".center(19,"*").lstrip("*"))
print("SpamSpamBaconSpamEggsSpamSpam".strip("ampS")) #strip all 'a' 'm' 'p' 'S' characters from leading and trailing
print("Hello there!".replace("e","XYZ"))
