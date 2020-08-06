import bs4, requests

res = requests.get("http://automatetheboringstuff.com/")
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, "html.parser")
# right click element > inspect
# right click highlighted code > copy > copy selector
elems = soup.select("body > div.main > div:nth-child(1) > h2:nth-child(19)")
print(elems[0].text)
