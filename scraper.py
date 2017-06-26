import requests
from lxml import html

pageContent=requests.get('https://www.w3schools.com/xml/books.xml')
tree = html.fromstring(pageContent.content)

authors=tree.xpath('//*/bookstore/book/title')

print (authors)
