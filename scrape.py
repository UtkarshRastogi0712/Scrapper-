import requests
from bs4 import BeautifulSoup

url='https://www.flipkart.com/gaming/gaming-consoles/pr?sid=4rr,x1m&otracker=categorytree'
page=requests.get(url)
print(page)
soup = BeautifulSoup(page.content,'html.parser')
data=soup.find('a',class_='s1Q9rs')
print(data.text)