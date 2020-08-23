# https://www.crummy.com/software/BeautifulSoup/bs4/doc/
# https://realpython.com/python-requests/
# https://realpython.com/beautiful-soup-web-scraper-python/

import requests
from bs4 import BeautifulSoup

def printJobs (jobList):
    for jobElememt in jobList:
        title = jobElememt.find('h2', class_='title')
        company = jobElememt.find('div', class_='company')
        location = jobElememt.find('div', class_='location')
        posted = jobElememt.find('time')

        if None in (title, company, location, posted):
            continue

        print("Title: " + title.text.strip())
        print("Company: " + company.text.strip())
        print("Location: " + location.text.strip())
        print("Date Posted: " + posted.text.strip())
        print()

# region Request
URL = "https://www.monster.com/jobs/search/?q=Software-Developer&where=tokyo"
page = requests.get(URL)

if page.status_code == 200:
    print('requests.get: Success!')
elif page.status_code == 404:
    print('requests.get: Not Found.')

print()
# endregion

soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id='ResultsScrollable')

# FIND 
jobElements = results.find_all('section', class_='card-content')
printJobs(jobElements)

jobEngineers = results.find_all('h2', string=lambda text: 'engineer' in text.lower())
print ("Engineer jobs: " + str(len(jobEngineers)))

if len(jobEngineers) >= 1:
    for jobElement in jobEngineers:
        link = jobElement.find('a')['href']
        print(jobElement.text.strip())
        print(f"Apply here: {link}\n")






# google my user agent
# headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36"}

# def checkPrice():
#     page = requests.get(URL, headers=headers)

#     soup = BeautifulSoup(page.content, "html.parser")
#     title = soup.find(id="productTitle")
#     price = soup.find(id="priceblock_ourprice")

#       print (title.strip())    
#       print (price)

# checkPrice()