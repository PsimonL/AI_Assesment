from bs4 import BeautifulSoup
from model import VolkswagenModel
import pandas as pd
import requests

data = []

for page_number in range(1, 563):
    # There is 563 pages. 

    url = f"https://www.otomoto.pl/osobowe/volkswagen?page={page_number}"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    articles = soup.find_all('article', attrs={'class': 'ooa-1g2kumr eayvfn60'})
    if len(articles) == 0: articles = soup.find_all('article', attrs={'class': 'ooa-1rudse5 eayvfn60'})

    for article in articles:
        
        price = article.find_all('span', attrs={'class': 'ooa-1bmnxg7 eayvfn611'})
        rest = article.find_all('li', attrs={'class': 'ooa-1k7nwcr e19ivbs0'})
        if(rest[0].text == 'Niski przebieg'): row = VolkswagenModel(price[0].text, rest[1].text, rest[2].text, rest[3].text)
        else : row = VolkswagenModel(price[0].text, rest[0].text, rest[1].text, rest[2].text)
        row.clean_data()
        data.append(row.return_data())  

df = pd.DataFrame(data)
df.to_csv('./AI_UniClasses_Assesment/data/otomoto.csv')