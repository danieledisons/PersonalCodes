#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 18 21:32:56 2020

@author: danielessien
"""

import bs4
import requests
from bs4 import BeautifulSoup

def parsePrice():
  r = requests.get('https://finance.yahoo.com/quote/FB?p=FB')
  soup=bs4.BeautifulSoup(r.text, 'lxml')
  Price = soup.find("div", {"class":'My(6px) Pos(r) smartphone_Mt(6px)'}).find('span').text
  return Price

while True:
    print("the current price is:"+ str(parsePrice()))
