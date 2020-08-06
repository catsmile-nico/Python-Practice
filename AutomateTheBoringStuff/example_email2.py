import imapclient

# create imap obj
conn = imapclient.IMAPClient("imap.gmail.com", ssl=True)

# login
conn.login("user@gmail.com", "mypassword")

# list folders
conn.list_folders()

# sel folder
conn.select_folder("INBOX", readonly=True) #set false to modify inbox folder

# search - returns UIDs for emails
UIDs = conn.search(["SINCE 20-Aug-2015"])
print(UIDs)

# delete mail using UID
conn.delete_messages([47474])

# get mail content using UID
rawMessage = conn.fetch([47474],["BODY[]", "FLAGS"])

# format message
import pyzmail
message = pyzmail.PyzMessage.factory(rawMessage[47474][b'BODY[]'])
print(message.get_subject())
print(message.get_addresses("from")) # to, bcc
print(message.text_part)
print(message.html_part)

# get body text
print(message.text_part.get_payload().decode("UTF-8"))

# get body text charset
print(message.text_part.charset)
