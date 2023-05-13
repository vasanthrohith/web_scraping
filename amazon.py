# Amazon

from bs4 import BeautifulSoup as bs
import requests

url = "https://www.amazon.in/OnePlus-Nord-Lite-128GB-Storage/product-reviews/B09WQYFLRX/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews"

page = requests.get(url)
page.content
soup = bs(page.content, 'html.parser')
soup.prettify()

names = soup.find_all('span', class_='a-profile-name')
n = []
for i in range(len(names)):
    n.append(names[i].get_text())

# import requests
# from bs4 import BeautifulSoup as bs
# import pandas as pd

# url='https://www.amazon.in/s?k=whey&crid=3UM134BB7932&sprefix=whe%2Caps%2C339&ref=nb_sb_noss_2'


# # this is our agent num we can get it by search-> what is my agent number to authenticate user to website
# HEADERS=({'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36','Accept-Language':'en-US,en:q=0.5',})

# # here we are requesting the website scraping with our agent num
# webpage=requests.get(url, headers=HEADERS) # print webpage if we get 200 good to go or 503 req denied

# webpage.content  # this will give us the bytes we need to convert to html content by bs

# soup=bs(webpage.content,'html.parser')  #raw to readable content

# # procuct a class inspection *the product name/link/class always in a class including product link in href
# links=soup.find_all('a',attrs={'class':'a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal'})

# # the above will have list of product script code return values including script here we are taking only the the linkin href
# link=links[2].get('href')

# # becuase we will fetch into each product page to get more infos.. price..ratings
# product_list="https://www.amazon.in"+link

# # this is our individual product page again we are req the auth req
# new_webpage=requests.get(product_list, headers=HEADERS)

# #raw to readable content
# new_soup=bs(new_webpage.content,'html.parser')

# # from the individual product page we are taking the product tile
# new_soup.find('span',attrs={'id':'productTitle'}).text.strip() #product title

# # from the individual product page we are taking the product price
# new_soup.find('span',attrs={'class':'a-price-whole'}).text #product price


# # from the individual product page we are taking the product ratings
# new_soup.find('span',attrs={'class':'a-icon-alt'}).text #ratings

# # to fetch some other thing always tke the class from span class or id


# --------------------------------
import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

url = 'https://www.amazon.in/s?k=whey&crid=3UM134BB7932&sprefix=whe%2Caps%2C339&ref=nb_sb_noss_2'

# this is our agent num we can get it by search-> what is my agent number to authenticate user to website
HEADERS = ({
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
    'Accept-Language': 'en-US,en:q=0.5', })

# here we are requesting the website scraping with our agent num
webpage = requests.get(url, headers=HEADERS)  # print it if we get 200 it's connected else 503-denied

soup = bs(webpage.content, 'html.parser')  # raw to readable content

# procuct a class inspection *the product name/link/class always in a class including product link in href -> comman page product nage
links = soup.find_all('a', attrs={
    'class': 'a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal'})

# to add cleaned links
product_links = []
# len(product_links)

# this loop will iterate into the links list and get only the href and append it to the product list
for i in links:
    # print(i)
    product_links.append(i.get('href'))


def scrap_pname(link_):  # function to scrap the name of the product
    # print(j)

    try:  # try to retrieve the product

        product_list = "https://www.amazon.in" + link_
        new_webpage = requests.get(product_list, headers=HEADERS)
        new_soup = bs(new_webpage.content, 'html.parser')

        p_name = new_soup.find('span', attrs={'id': 'productTitle'}).text.strip()


    except Exception as e:  # if not return it as nan
        p_name = 'nan'

    return p_name


def scrap_pprice(link_):  # function to scrap the price of the product
    # print(j)

    try:  # try to retrieve the price

        product_list = "https://www.amazon.in" + link_
        new_webpage = requests.get(product_list, headers=HEADERS)
        new_soup = bs(new_webpage.content, 'html.parser')

        p_price = new_soup.find('span', attrs={'class': 'a-price-whole'}).text


    except Exception as e:  # if not return it as nan
        p_price = 'nan'

    return p_price


def scrap_prating(link_):  # fn to scrap product rating
    # print(j)

    try:  # try to retrieve the rating

        product_list = "https://www.amazon.in" + link_
        new_webpage = requests.get(product_list, headers=HEADERS)
        new_soup = bs(new_webpage.content, 'html.parser')

        p_rating = new_soup.find('span', attrs={'class': 'a-icon-alt'}).text


    except Exception as e:  # if not return it as nan
        p_rating = 'nan'

    return p_rating


# the scraped details will be appended in below list

prod_name = []
prod_price = []
prod_rarings = []

# loop to iterate the product_links one by one to scrap
for j in range(0, len(product_links)):
    prod_name.append(scrap_pname(product_links[j]))
    prod_price.append(scrap_pprice(product_links[j]))
    prod_rarings.append(scrap_prating(product_links[j]))

dict_1 = {"Product_name": prod_name, "Price": prod_price, "Ratings": prod_rarings}

df = pd.DataFrame(dict_1)  # dataframe

# saving as csv file
df.to_csv(r"C:\Users\vasanth rohith\OneDrive - Kau Yan College\Desktop\Datasets\whey_scrap_090523.csv")
print("saved successfully .....")

# 09/05/2023------------------------------------------------


# scraping multiple page reviews on amazon

from bs4 import BeautifulSoup
import requests
import pandas as pd

link = 'https://www.amazon.in/OnePlus-Nord-Lite-128GB-Storage/product-reviews/B09WQYFLRX/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&'

list_name = []
prod_rev = []

for i in range(1, 4):
    para = {'pagenumber': str(i)}
    page = requests.get(link, params=para)
    soup = bs(page.content, 'html.parser')
    soup.prettify()
    names = soup.find_all('span', attrs={'class': 'a-profile-name'})  # to scrap the profile name
    names = soup.find_all('a', attrs={'class': 'review-title'})  # to scrap the prod review heading

for j in range(0, len(names)):
    list_name.append(names[j].get_text())
    prod_rev.append(names[j].get_text())

# need to scrap pages from multiple pages **************

# text mining
import re
import nltk

nltk.download('stopwords')
from nltk.corpus import stopwords

reviews_1 = ' '.join(prod_rev)  # joining all the words to single para

reviews_2 = re.sub("[^A-Za-z]", " ", reviews_1.lower())  # removing all the special cases taking only the words

reviews_3 = reviews_2.split(" ")  # splitting the list by it's spaces " " separated by ,

# eliminating the stopwords
reviews_4 = [i for i in reviews_3 if not i in set(stopwords.words('english'))]  # eleminating the stop words

reviews_5 = " ".join(reviews_4)  # after completing the cleaning joining all the words to form a word cloud

# visualization
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS

plt.figure(dpi=300)
wordcloud_ = WordCloud(background_color='green', width=1920, height=1080).generate(reviews_5)
plt.imshow(wordcloud_)
