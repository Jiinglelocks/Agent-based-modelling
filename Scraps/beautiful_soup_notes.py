# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 18:31:30 2022

@author: alexa
"""

html_doc = """<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

from bs4 import BeautifulSoup

soup = BeautifulSoup(html_doc, 'html.parser')

"""
# could also pass it into BS constructor with an open filehandle:
with open("index.html") as fp:
    soup = BeautifulSoup(fp, 'html.parser')
"""

# print the html source in an indented tree style
print(soup.prettify())

# print the title class
print(soup.title)

# extract all URLs within the <a> tags
for link in soup.find_all('a'):
    print(link.get('href'))
    
# extract all the text from a page
print(soup.get_text())

# A tag object corresponds to an XML or HTML tag in source
soup = BeautifulSoup('<b class="boldest">Extremely bold</b>', 'html.parser')
tag = soup.b
print(type(tag))

# each tag has a name
print(tag.name)

# changing a tag's name will reflect in any HTML markup generated by BS
tag.name = "blockquote"
print(tag)


