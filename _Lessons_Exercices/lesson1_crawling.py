# coding: utf-8
import requests
from bs4 import BeautifulSoup



def get_all_links_for_query(query):

  url = "http://www.purepeople.com/rechercher/"
  res = requests.post(url, data = {'q': query })

  if res.status_code == 200:
    html_doc =  res.text
    soup = BeautifulSoup(html_doc,"html.parser")
    specific_class = "c-article-flux__title"
    all_links = map(lambda x : x.attrs['href'] , soup.find_all("a", class_= specific_class))

  return all_links

page_url = "http://www.purepeople.com/article/brigitte-macron-decroche-une-jolie-couv-a-l-etranger_a306389/1"
def get_share_count_for_page(page_url):

  res = requests.get(page_url)

  if res.status_code == 200:
    html_doc =  res.text
    soup = BeautifulSoup(html_doc,"html.parser")
    specific_class = "c-sharebox__stats-number"
    return soup.find("span", class_= specific_class).text


