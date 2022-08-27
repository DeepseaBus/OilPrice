import requests
import urllib
import re
import csv
import codecs
import random
import time
import os
from bs4 import BeautifulSoup

result = requests.get("https://www2.moeaboe.gov.tw/oil102/oil2017/newmain.asp")
c = result.content
soup = BeautifulSoup(c, 'html.parser')
soup.prettify()

domestic = soup.find('div', {"id": "tbuse"})
d = domestic.find('div', {"id": "1Tab"})
rawText = "".join(d.text.replace("\n", ",").split())
oilInfo = rawText.split(",")
insertInfo = []
for info in oilInfo:
    if info != "" and not re.match(r'[0-9]+[.][0-9]+', info) and not re.search(r'[0-9]+[/][0-9]+[/][0-9]+', info):
        info = info.split('：')
        tmp = info.pop()
        r = (re.search(r'[0-9]+[.][0-9]+', tmp)).span()
        type = info[0]
        price = tmp[r[0]:r[1]]
        unit = tmp[r[1]:]
        entity = [type,price,unit]
        insertInfo.append(entity)
print(insertInfo)

international = soup.find('section', {"class": "boxheight_05"})
rawText = "".join(international.text.replace("\n", ",").split())
oilInfo = rawText.split(",")
for i in range(0,len(oilInfo)):
    if re.search(r'[0-9]+[.][0-9]+', oilInfo[i]):
        a = oilInfo[i]
        r = (re.search(r'[0-9]+[.][0-9]+', oilInfo[i])).span()
        type = oilInfo[i][:r[0]]
        price = oilInfo[i][r[0]:r[1]]
        unit = oilInfo[i+1]
        entity = [type,price,unit]
        insertInfo.append(entity)
print(insertInfo)
