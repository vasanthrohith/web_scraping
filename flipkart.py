# Web scrapping using selenium
from selenium import webdriver
from bs4 import BeautifulSoup

import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

url = "https://www.flipkart.com/home-kitchen/home-appliances/washing-machines/fully-automatic-front-load~function/pr?sid=j9e%2Cabm%2C8qx&otracker=nmenu_sub_TVs%20%26%20Appliances_0_Fully%20Automatic%20Front%20Load"

driver.get(url)
content = driver.page_source

soup = BeautifulSoup(content)

products = []
prices = []

for i in soup.findAll('a', href=True, attrs={'class': '_1fQZEK'}):
    name = i.find('div', attrs={'class': '_4rR01T'})
    price = i.find('div', attrs={'class': '_30jeq3 _1_WHN1'})

    # price=i.find('div',attrs={'class':'_30jeq3 _1_WHN1'})
    # print(name,'\n',price)
    products.append(name.text)
    prices.append(price.text)

df = pd.DataFrame({"Products": products, "Price": prices})
