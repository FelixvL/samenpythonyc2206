import mysql.connector
from flask import jsonify
import pandas as pd
import bs4
import requests
import json
import re
import random

# import data
try:
    df = pd.read_csv("./data/maaltijden.csv")
except Exception as err:
    print(err)
        
mydb = mysql.connector.connect(
	host="2206-bezorgapp.mysql.database.azure.com",  #port erbij indien mac
	port=3306,
	user="beheerder@2206-bezorgapp",
	password="abcd1234ABCD!@#$",
	database="bezorgappbigdata"
)

def toonDataDeel():     
    print(df.head())
    return "toonDataDeel is gelukt"

def toonDataSpecifiek(num):
    row = int(num)
    toon = df.iloc[row]
    print(toon)
    return toon.to_json()

def toonQuotesAllemaal():    
    try: # errorhandling
        rg = requests.get("https://medium.com/swlh/21-of-the-worlds-most-powerful-quotes-updated-for-today-and-tomorrow-6b7634358c2") # GET document from medium.com        
    except Exception as err: 
        print("Something went wrong:", err)
        rg = None
        
    html_doc = rg.text # get HMTL content from response object
    soup = bs4.BeautifulSoup(html_doc, 'html.parser') # turn html_doc into BS4 object
    quotes = soup.find_all("h2") # find all quotes  
    
    counter = 0
    quotes_lijst = []
    
    for q in quotes[:21]:
        res = str(q).split("“")
        res2 = res[1][:-5]
        res3 = res2.split("” — ")
        q = res3[0]
        a = res3[1]
        
        counter +=1
        tekst_en_auteur = (f"{q} - {a}")
        quotes_lijst.append(tekst_en_auteur)
        
    return quotes_lijst, q, a

def randomQuote():
    nummer = random.randint(0, 21)
    quotes = toonQuotesAllemaal()
    print("----------")
    print(quotes)
    return quotes[0][nummer]


def opslaanQuotes():    
    try: # errorhandling
        rg = requests.get("https://medium.com/swlh/21-of-the-worlds-most-powerful-quotes-updated-for-today-and-tomorrow-6b7634358c2") # GET document from medium.com        
    except Exception as err: 
        print("Something went wrong:", err)
        rg = None
        
    html_doc = rg.text # get HMTL content from response object
    soup = bs4.BeautifulSoup(html_doc, 'html.parser') # turn html_doc into BS4 object
    quotes = soup.find_all("h2") # find all quotes  
        
    for quote in quotes[:21]:
        res = str(quote).split("“")
        res2 = res[1][:-5]
        res3 = res2.split("” — ")
    
        q = res3[0]
        a = res3[1]
    
        mycursor = mydb.cursor()
        sql = "INSERT INTO quote (tekst, auteur) VALUES (%s, %s)"
        val = (q, a)
        mycursor.execute(sql, val)
        mydb.commit()
        print(mycursor.rowcount, "record inserted.")
    
    return "opslaan van quotes is gelukt!!!"