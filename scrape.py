import requests
from bs4 import BeautifulSoup

url='https://www.grainmart.in/news/covid-19-coronavirus-india-state-and-district-wise-tally/'
page=requests.get(url)
print(page)