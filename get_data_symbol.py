from bs4 import BeautifulSoup
import requests
import pandas as pd

#获取当前行情
def get_curr():
    url = "https://coinmarketcap.com/all/views/all/"
    content = requests.get(url).content
    soup = BeautifulSoup(content,'html.parser')
    table = soup.find('table', {'class': 'table'})
    
    
    data = [[td.text.strip() for td in tr.findChildren('td')]
            for tr in table.findChildren('tr')]
    
    df = pd.DataFrame(data)
    df.drop(df.index[0], inplace=True) # first row is empty
    df.drop(df.index[1], inplace=True) # first row is empty
    df.drop(df.columns[0],axis=1,inplace=True)
    df.drop(df.columns[9],axis=1,inplace=True)
    df.columns = ['Name','Symbol','Market Cap','Price','Circulating Supply','Volume(24h)','%1h','%24h','%7d']
    df.sort_index(inplace=True)
    print df
    df.to_csv("all_view.csv",index=False)

