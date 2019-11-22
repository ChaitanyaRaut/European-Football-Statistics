import requests
from bs4 import BeautifulSoup

response = requests.get('https://www.bbc.com/sport/football/spanish-la-liga/top-scorers')


soup = BeautifulSoup(response.content, 'html.parser')
table_tag = soup.find('ol')   

with open('sample_tag.html', 'w') as f:
    f.write(table_tag.prettify())

