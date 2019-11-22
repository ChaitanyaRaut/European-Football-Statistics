"""
This script parses a wikipedia page and gives the  goals scored table as a tag object of beatiful soup
""" 

import requests
from bs4 import BeautifulSoup

response = requests.get('https://en.wikipedia.org/wiki/2019%E2%80%9320_La_Liga')

html = BeautifulSoup(response.content, 'html.parser')

a = html.findAll("span", {"id": "Top_goalscorers"}) #Find the Soup for tag which corrosponds to heading given to the table section
b = a[0].parent
table = b.find_next_siblings("table") #This will give you the table of top scorers as a beatiful soup tag, python list

# Alternative - mydivs = b.findAll("div", {"class": "wikitable"}) or use find with class_ key

t= table[0]
t.attrs # this will print the attributes
tbody = t.find('tbody')

rows = tbody.find_all('tr') # This will give you all children of tag table

"""
The problem now is to parse the row such that you can get the names and goals scored for each player.
But wiki page uses something called as "rowspan" which makes it difficult to parse"""


