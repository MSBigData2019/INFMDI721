# coding: utf-8
import requests
from bs4 import BeautifulSoup


def _handle_request_result_and_build_soup(request_result):

  if request_result.status_code == 200:
    html_doc =  request_result.text
    soup = BeautifulSoup(html_doc,"html.parser")
    return soup

def get_all_links_for_query(query):

  url = "http://www.purepeople.com/rechercher/"
  res = requests.post(url, data = {'q': query })
  soup = _handle_request_result_and_build_soup(res)
  specific_class = "c-article-flux__title"
  all_links = map(lambda x : x.attrs['href'] , soup.find_all("a", class_= specific_class))

  return all_links

def get_share_count_for_page(page_url):
  res = requests.get(page_url)
  soup = _handle_request_result_and_build_soup(res)
  specific_class = "c-sharebox__stats-number"
  return soup.find("span", class_= specific_class).text


