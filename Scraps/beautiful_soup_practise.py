# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 18:16:12 2022

@author: alexa
"""
import requests
import bs4
"""
# make a http request inside a response variable 'r'
r = requests.get('http://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part9/data.html')
content = r.text
soup = bs4.BeautifulSoup(content, 'html.parser')
#print(soup.prettify())
td_ys = soup.find_all(attrs={"class" : "y"})
td_xs = soup.find_all(attrs={"class" : "x"})
print(td_ys)
print(td_xs)
"""

r2 = requests.get('https://naturenet.net/law/sched9.html')
content2 = r2.text

soup = bs4.BeautifulSoup(content2, 'html.parser')
soup.td.decompose()
print(str(soup))
test = soup.find_all(attrs={"class" : "natnet"})
testlist = []

for row in soup.find_all('td'):
    testlist.append(row)
    print(row)
    

