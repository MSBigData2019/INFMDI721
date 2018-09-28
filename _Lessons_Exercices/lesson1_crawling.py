# coding: utf-8
import requests
from bs4 import BeautifulSoup


url = "http://www.purepeople.com/rechercher/"

#res = requests.get(url)
res = requests.post(url, data = {'q':'macron'})

if res.status_code == 200:
  html_doc =  res.text
  soup = BeautifulSoup(html_doc,"html.parser")
  specific_class = "c-article-flux__title"
  all_links = map(lambda x : x.attrs['href'] , soup.find_all("a", class_= specific_class))
  print all_links


url_page = "http://www.purepeople.com/article/brigitte-macron-decroche-une-jolie-couv-a-l-etranger_a306389/1"

res = requests.get(url_page)

if res.status_code == 200:
  html_doc =  res.text
  soup = BeautifulSoup(html_doc,"html.parser")
  specific_class = "c-sharebox__stats-number"
  print soup.find("span", class_= specific_class).text


