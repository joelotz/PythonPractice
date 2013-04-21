# -*- coding: utf-8 -*-
'''
-------------------------------------------------------------------------------
Filename   : scrabbleAPI.py
Date       : 2013-04-20
Author     : Joe Lotz <joelotz@gmail.com>
Description: 
This is my attempt at building an API from a website. It utilizes web scraping, 
assumes an internet connect and access to http://www.scrabblefinder.com, 
scrabblefinder is authored by David Shimoda @scrabblefinder

Please follow the first rule of web-scraping... Don't be a dick.

This could is not intended to be "production-quality" rather it was built to 
practice and learn building APIs to extend website functionality. 
It was directly inspired and motivated by Asheesh Laroia in his wonderful 
PyCon talks.(http://pyvideo.org/)

SCRABBLE® is a registered trademark...duh
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
    if len(words) > 0:
        d = []
        for word in words:
            if word.endswith(letters): d.append(word)
        return d            
    else: 
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
    if len(words) > 0:
        d = []
        for word in words:
            if word.startswith(letters): d.append(word)
        return d            
    else: 
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
        
def twoletter():
    url = "http://www.scrabblefinder.com/two-letter-scrabble-words"
    return scrape_page(url)

def threeletter():
    url = "http://www.scrabblefinder.com/3-letter-words/"
    return scrape_page(url)
    
def fourletter():
    url = "http://www.scrabblefinder.com/4-letter-words/"
    return scrape_page(url)    
