from bs4 import BeautifulSoup
import requests
import pandas as pd
import re


def parser():
    url = "https://coinmarketcap.com/all/views/all/"
    content = requests.get(url).content
    return BeautifulSoup(content,'html.parser')
    
def get_date_print():
    soup = parser() 
    for a in soup.find_all('a', {'class': 'currency-name-container link-secondary'}, href=True):
        print "a---:",a.text
        print "Found the URL:", a['href']
        
def get_coin_name():
    pattern = re.compile(r'/+')
    soup = parser()
    return [pattern.split(url.get('href'))[2] for url in soup.find_all("a", attrs={"class": "currency-name-container link-secondary"})] 

