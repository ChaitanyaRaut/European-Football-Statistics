# -*- coding: utf-8 -*-
"""
Created on Tue Mar 20 16:02:27 2018

@author: Chaitanya Raut     
"""

import requests

response = requests.get('https://www.fotmob.com/leagues/87/stats')

#print(response.text)

response.json()

"""
index = page.find('"rank">1') #Start of the table at the webpage
index1 = page.find('"rank">4',index) #End of the data which we are interested
player_data = page[index:index1-23]
player_data = ' '.join(player_data.split())


print(player_data)
URL2 = urllib2.urlopen('http://www.espnfc.us/english-premier-league/23/statistics/scorers')
page1 = URL2.read()  #Reads the url
page1.strip()       #Removes white spaces
index = page1.find('"rank">1') #Start of the table at the webpage
index1 = page1.find('"rank">4',index) #End of the data which we are interested
player_data1 = page1[index:index1-23]
player_data1 = ' '.join(player_data1.split())

print player_data1
"""