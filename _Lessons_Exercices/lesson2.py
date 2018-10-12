# coding: utf-8
import requests
import unittest
from bs4 import BeautifulSoup
import pandas as pd
import json

movie = 'star wars'
url = 'http://www.omdbapi.com?apikey=ca3d2593&s='+movie+'&type=movie'

res = requests.get(url)

response_object = json.loads(res.text)
movies_list = response_object['Search']
df_movies = pd.DataFrame(movies_list)
