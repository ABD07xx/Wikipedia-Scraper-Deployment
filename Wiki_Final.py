import streamlit as st

import pandas as pd
import requests
from bs4 import BeautifulSoup


st.title("Wikipedia Scraper")
inp   = st.text_input("Enter Persons Name")

if inp is not None:
    
    link  = 'https://www.google.com/search?q=' + str(inp) +" "+ "Wikipedia"
    link  = link.replace(' ','+')
    st.caption(link)

    res = requests.get(link)
    soup = BeautifulSoup(res.text,'html.parser')

    for sp in soup.find_all('div'):
        try:
            link = sp.find('a').get('href')
            
            if('en.wikipedia.org' in link):
                break
        except:
            pass
    link = (link[7:]).split('&')[0]
    print(link)

    res = requests.get(link)
    soup = BeautifulSoup(res.text,'html.parser')

    heading = soup.find('h1').text
    print(heading)


    paragraphs = ''

    for p in soup.find_all('p'):
        paragraphs += p.text
        paragraphs += '\n'
         
    paragraphs = paragraphs.strip()

    for i in range(1000):
        paragraphs = paragraphs.replace('[' + str(i) + ']','')
        
        

    if st.checkbox("Show/Hide"):
        st.text(paragraphs)
    
    status2 = st.radio("Do you want to save this text?",("False","True"))
    if status2 =='True':
        fd = open(heading + ".txt" , 'w',encoding='utf-8')
        fd.write(paragraphs)
        fd.close()
        st.text("File Saved")