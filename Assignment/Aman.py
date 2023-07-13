# Importing required libraries

# pip install selenium

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Setting up the webdriver
driver = webdriver.Chrome()

# Navigating to the Amazon.ca homepage
driver.get("https://www.amazon.ca")
time.sleep(5)

# Finding the search bar and entering text
# search_bar = driver.find_element_by_id("id","twotabsearchtextbox") old syntax
search_bar = driver.find_element("id","twotabsearchtextbox")
search_bar.send_keys("career books")

# Submitting the search query
search_bar.send_keys(Keys.RETURN)

# Waiting for the search results page to load
time.sleep(5)



# Selecting a picture 
free_shipping_link = driver.find_element("xpath","/html/body/div[1]/div[2]/div[1]/div[2]/div/div[3]/span/div[1]/div/div/div[1]/ul/span/li/span/a/span")
# free_shipping_link = driver.find_element("By.CSS_SELECTOR","span[data-component-type='s-product-image'] a")
free_shipping_link.click()
time.sleep(4)



# Selecting a picture 
Book_link = driver.find_element("xpath","/html/body/div[1]/div[2]/div[1]/div[1]/div/span[1]/div[1]/div[3]/div/div/div/div/div/div/div[1]/span/a/div")
#Book_link = driver.find_element("By.CSS_SELECTOR","span[data-component-type='s-product-image'] a")
Book_link.click()
time.sleep(4)


# Selecting a picture 
#Button_link = driver.find_element("xpath","/html/body/div[2]/div[2]/div[3]/div[1]/div[4]/div[4]/div/div[1]/div/div/div/form/div/div/div/div/div[3]/div/div[23]/div/div/span[2]/span/input")
#Button_link = driver.find_element("By.CSS_SELECTOR","span[data-component-type='s-product-image'] a")
#Button_link.click()
#time.sleep(4)

#Buy_now_button = driver.find_element("id","Buy-now-button").click()
#driver.find_element("xpath","//html/body/div[2]/div[2]/div[3]/div[1]/div[4]/div[4]/div/div[1]/div/div/div/form/div/div/div/div/div[3]/div/div[23]/div/div/span[2]/span/input")


New_york_link = driver.find_element("xpath","/html/body/div[2]/header/div/div[6]/div/a[8]/span")
#Book_link = driver.find_element("By.CSS_SELECTOR","span[data-component-type='s-product-image'] a")
New_york_link.click()
time.sleep(4)







driver.close()





