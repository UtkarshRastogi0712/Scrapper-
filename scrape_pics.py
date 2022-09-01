import requests
from bs4 import BeautifulSoup
from os.path import basename

url='https://www.flipkart.com/gaming/gaming-consoles/pr?sid=4rr,x1m&otracker=categorytree'
page=requests.get(url)
print(page)
soup = BeautifulSoup(page.content,'html.parser')
count,limit=0,10
for img in soup.find_all('img',class_='_396cs4 _3exPp9'):
    if 'http' in img['src']:
        link = img['src']
        name='img_'+str(count)+'.jpg'
        with open(name,'wb') as handler:
            handler.write(requests.get(link).content)
            count+=1
        if count==limit:
            break
        