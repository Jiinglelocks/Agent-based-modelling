# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 18:16:12 2022

@author: alexa
"""
import requests
import bs4


# make a http request inside a response variable 'r'
r = requests.get('http://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part9/data.html')
content = r.text
# make the soup! passing the text from the http request into a BeautifulSoup object
# which represents it as a nested data structure
soup = bs4.BeautifulSoup(content, 'html.parser')
#print(soup.prettify()) # checking out the html in an indented format
td_ys = soup.find_all(attrs={"class" : "y"}) # finds all rows with specified class, stores in a list including tags
td_xs = soup.find_all(attrs={"class" : "x"})
#print(int(td_ys[0].text)) # printing out a value at position [0] to see how it looks

# stripping out the integer values from the td_ys and td_xs lists and appending
# to a blank list, for example, now instead of <td class="y">93</td> the value will be 93
y_values = []
for row in td_ys:
    #print(int(row.text))
    y_values.append(int(row.text))
x_values = []
for row in td_xs:
    x_values.append(int(row.text))
print(y_values) # checking how it looks
print(x_values)

    





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
"""

