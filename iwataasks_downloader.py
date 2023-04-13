#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# iwataasks_downloader.py

import requests
from bs4 import BeautifulSoup

path = input("PATH (don't include the file name or a slash at the end): ")
title = "Iwata Asks: " + input('Game/product name (don\'t put "iwata asks: ") ')
URL = input("URL: ")

page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(class_="col-xs-12 instapaper_body")

navigation = soup.find(class_="leftmenu")
pages = [URL[26:]]

for link in navigation.find_all("a"):
    pages.append(link["href"])
count = len(pages)

file = open(path + "/iwataasks_output.txt", "w")
for i in range(0, count):
    URL = "https://www.nintendo.co.uk" + pages[i]
    
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find(class_="col-xs-12 instapaper_body")

    for footnote in results.find_all("span", {"class": "footnote"}): 
        footnote.decompose()
    for superscript in results.find_all("sup"): 
        superscript.decompose()
    for image in results.find_all("div", {"class": "col-xs-12"}): 
        image.decompose()
    for script in results.find_all("noscript"): 
        script.decompose()
        
    print("Loading")
    file.write(results.get_text())

file.close()
    
file = open(path + "/iwataasks_output.txt", "r")
contents = file.read()
file.close()
print("Finding")

for _ in range(9):
    contents = contents.replace("  ", " ")
    contents = contents.replace("\n \n", "\n\n")
    contents = contents.replace("\n\n\n", "\n\n")
print("Replacing")

file = open(path + "/iwataasks_output.txt", "w")
file.write(title)
file.close()

file = open(path + "/iwataasks_output.txt", "a")
file.write(contents)
file.close()
print("Done")
