import smtplib

conn = smtplib.SMTP("smtp.gmail.com", 587)
print(type(conn))
print(conn)

# start connection
temp = conn.ehlo()
conn.starttls()

# login
conn.login("email@gmail.com", "mypassword")

# send mail - will return a dict of failed recipient
conn.sendmail("from@gmail.com", "to@gmail.com", "Subject: so long...\n\nHi there, \n much text\n\nRegards")

# stop connection
conn.quit()
