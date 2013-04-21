# -*- coding: utf-8 -*-
'''
-------------------------------------------------------------------------------
Filename   : scrabbleAPI.py
Date       : 2013-04-20
Author     : Joe Lotz
Description: 
-------------------------------------------------------------------------------
'''
def scrape_page(url):
    from mechanize import Browser
    from bs4 import BeautifulSoup

    mech = Browser()
    page = mech.open(url)
    soup = BeautifulSoup(page.read())

    words = []
    for links in soup.findAll('li', attrs={'class' : 'defLink'}):
        words.append(links.a.text)
    
    return words

def make_dictionary(names):
    from collections import defaultdict
    
    d =  defaultdict(list)
    for name in names:
        key = len(name)
        d[key].append(name)

    return d    
    
def endswith(letters, size=0, words=[]):
    if len(words) == 0:
        url = ''.join(["http://www.scrabblefinder.com/ends-with/",letters,"/"])
        words = scrape_page(url)

    d = make_dictionary(words)
    
    if size > 0:
        if size not in d.keys():
            print ("There are no words with size=%i that ends with \"%s\"" % (size,letters))
        else:
            return d[size]
    else:   
        return d

def startswith(letters, size=0, words=[]):
    if len(words) == 0:
        url = ''.join(["http://www.scrabblefinder.com/starts-with/",letters,"/"])
        words = scrape_page(url)
    d = make_dictionary(words) 
    if size > 0:
        if size not in d.keys():
            print ("There are no words with size=%i that start with \"%s\"" % (size,letters))
        else:
            return d[size]
    else:   
        return d

def 2letter():
    url = "http://www.scrabblefinder.com/two-letter-scrabble-words"
    return scrape_page(url)

def 3letter():
    url = "http://www.scrabblefinder.com/3-letter-words/"
    return scrape_page(url)
    
def 4letter():
    url = "http://www.scrabblefinder.com/4-letter-words/"
    return scrape_page(url)    
    
    
    
    
    
##==============================##

d = endswith(letters="us",size=3)


