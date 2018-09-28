# coding: utf-8
import requests
import unittest
from bs4 import BeautifulSoup

website_prefix = "http://www.purepeople.com"
def _handle_request_result_and_build_soup(request_result):

  if request_result.status_code == 200:
    html_doc =  request_result.text
    soup = BeautifulSoup(html_doc,"html.parser")
    return soup

def get_all_links_for_query(query):

  url = website_prefix + "/rechercher/"
  res = requests.post(url, data = {'q': query })
  soup = _handle_request_result_and_build_soup(res)
  specific_class = "c-article-flux__title"
  all_links = map(lambda x : x.attrs['href'] , soup.find_all("a", class_= specific_class))

  return all_links

def get_share_count_for_page(page_url):
  res = requests.get(page_url)
  soup = _handle_request_result_and_build_soup(res)
  specific_class = "c-sharebox__stats-number"
  share_count_text = soup.find("span", class_= specific_class).text
  return  int(share_count_text.strip())


query = 'macron'
page_url = "http://www.purepeople.com/article/brigitte-macron-decroche-une-jolie-couv-a-l-etranger_a306389/1"

url_macron = get_all_links_for_query(query)
results_macron = []
for url in url_macron:
    results_macron.append(get_share_count_for_page(website_prefix + url))

class Lesson1Tests(unittest.TestCase):
    def testShareCount(self):
        self.assertEqual(get_share_count_for_page("http://www.purepeople.com/article/brigitte-macron-decroche-une-jolie-couv-a-l-etranger_a306389/1") , 86)


def main():
    unittest.main()

#if __name__ == '__main__':
    #main()
