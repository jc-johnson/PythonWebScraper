from __future__ import unicode_literals
import urllib2
from bs4 import BeautifulSoup
import csv
from datetime import datetime

#!/usr/bin/python
# -*- coding: utf-8 -*-

# specify the url
quote_page = ['https://www.bloomberg.com/quote/SPX:IND',
    'https://www.bloomberg.com/quote/CCMP:IND',
    'https://www.bloomberg.com/quote/SPTSX:IND',
    'https://www.bloomberg.com/quote/GC1:COM',
    'https://www.bloomberg.com/quote/UKX:IND']

# for loop
data = []
for pg in quote_page:
    # query the website and return the html to the variable 'page'
    page = urllib2.urlopen(pg)

    # parse the html using beautiful soap and store in variable 'soup'
    soup = BeautifulSoup(page, 'html.parser')

    # Take out the <div> of name and get its value
    name_box = soup.find('h1', attrs={'class': 'name'})
    name = name_box.text.strip() # strip() is used to remove starting and trailing

    # get the index price
    price_box = soup.find('div', attrs={'class':'price'})
    price = price_box.text

    print name
    print price

    # save the data in tuple
    data.append((name, price))

# open a csv file with append, so old data will not be erased
with open('index.csv', 'a') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(["Name", "Price", "Current Time"])
    for name, price in data:
        writer.writerow([name, price, datetime.now()])
