import requests
from bs4 import BeautifulSoup
from newspaper import Article
from tqdm import tqdm
import pandas as pd


def scrap_year(page_count: int):
    scraped_data = []
    url_list = []
    for i in range(1, page_count + 1):
        main_page_url = 'https://aftabnews.ir/fa/archive' + '?p=' + str(i)
        html = requests.get(main_page_url).text
        soup = BeautifulSoup(html, features='html.parser')
        links_all = soup.find_all('div', {'class': 'linear_news'})
        pure_links = []
        for index, link in enumerate(links_all):
            if index == 20:
                break
            pure_links.append(("https://www.aftabnews.ir" + link.a['href']))


        try:
            for link in pure_links:
                print('----', link)
                article = Article(link)
                article.download()
                article.parse()
                scraped_data.append(article.text)
        except Exception as e:
            pass


    fd = pd.DataFrame(scraped_data)
    fd.to_csv(f'aftabnews_to_{page_count}_page.csv')




scrap_year(1)
