from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

binary = FirefoxBinary(r"C:\Program Files\Mozilla Firefox\firefox.exe")
fp = webdriver.FirefoxProfile()
driver = webdriver.Firefox(firefox_binary=binary, firefox_profile=fp, executable_path='geckodriver.exe')

driver.get("http://automatetheboringstuff.com/")

# get element using css selector
elem = driver.find_element_by_css_selector(".main > div:nth-child(1) > ul:nth-child(20) > li:nth-child(1) > a:nth-child(1)")
print (elem)
elem.click()

# browser navigation
driver.back()
driver.forward()


# get all paragraph elements
elems = driver.find_elements_by_css_selector("p") 
print (len(elems))


 
searchElem = driver.find_element_by_css_selector(".search-field")
searchElem.send_keys("zophie")
searchElem.submit()


# browser interaction
driver.refresh()
driver.quit()
