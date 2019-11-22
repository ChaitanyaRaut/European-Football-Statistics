import requests
from bs4 import BeautifulSoup

response = requests.get('https://www.bbc.com/sport/football/italian-serie-a/top-scorers')


soup = BeautifulSoup(response.content, 'html.parser')

############### Parsing for BBC sports page #################

#a = html.find_all('h1', class_="page-title")
# b = a[0].find_next_sibling("div", {"id": "top-scorers"})

table_tag = soup.find('ol')   
#This will directly give you the table tag. Key Observation = "<ol" tag appears only once in the page and is used for the table


rows = table_tag.find_all('li')

for row in rows:
    player_name = row.find('h2', class_="top-player-stats__name")
    goals_scored = row.find('span', class_="top-player-stats__goals-scored-number")
    assists = row.find('span', class_="top-player-stats__assists-number")
    print("Name = {}".format(player_name.string))
    print("Goals = {}".format(goals_scored.string))
    print("Assists = {}".format(assists.string))

#TODO - Convert the goals and assists in ints
    




