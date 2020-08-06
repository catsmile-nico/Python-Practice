import requests

# get response from website
res = requests.get("https://automatetheboringstuff.com/files/rj.txt")
print(res.status_code) #200 means OK
print(len(res.text))
print(res.text[:500]) 
res.raise_for_status() #nothing happen if success, otherwise throw exception

try:
    badRes = requests.get("https://automatetheboringstuff.com/files/raaajasdolihdashl")
    badRes.raise_for_status()
except:
    print("HTTPError")

# save content
playFile = open("RomeoAndJuliet.txt","wb")
for chunk in res.iter_content(100000):
    print(playFile.write(chunk)) # chunk written
    
playFile.close()
