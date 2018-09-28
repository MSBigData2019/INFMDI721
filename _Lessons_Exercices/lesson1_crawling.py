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


query = 'macron'
page_url = "http://www.purepeople.com/article/brigitte-macron-decroche-une-jolie-couv-a-l-etranger_a306389/1"

url_macron = get_all_links_for_query(query)
share_count_test = get_share_count_for_page(page_url)

class Lesson1Tests(unittest.TestCase):
    def testShareCount(self):
        self.assertEqual(get_share_count_for_page("http://www.purepeople.com/article/brigitte-macron-decroche-une-jolie-couv-a-l-etranger_a306389/1") , 86)



def main():
    unittest.main()
