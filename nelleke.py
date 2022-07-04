import mysql.connector
from flask import jsonify
import pandas as pd
import bs4
import requests
import json
import re

# import data
try:
    df = pd.read_csv("./data/maaltijden.csv")
except Exception as err:
    print(err)
        
# def methodevannelleke():
# 	print("naar de database")
# 	mydb = mysql.connector.connect(
# 		host="localhost",  #port erbij indien mac
# 		user="root",
# 		password="",
# 		database="patat"
# )
# 	mycursor = mydb.cursor()
# 	mycursor.execute("SELECT * FROM quote")
# 	recordset = mycursor.fetchall()
# 	print(recordset)
# 	return jsonify(list(recordset))

# import csv file
def toonDataDeel():     
    print(df.head())
    return "toonDataDeel is gelukt"

def toonDataSpecifiek(num):
    row = int(num)
    toon = df.iloc[row]
    print(toon)
    return toon.to_json()

def toonQuotes():    
    try: # errorhandling
        rg = requests.get("https://medium.com/swlh/21-of-the-worlds-most-powerful-quotes-updated-for-today-and-tomorrow-6b7634358c2") # GET document from medium.com        
    except Exception as err: 
        print("Something went wrong:", err)
        rg = None
        
    html_doc = rg.text # get HMTL content from response object
    soup = bs4.BeautifulSoup(html_doc, 'html.parser') # turn html_doc into BS4 object
    quotes = soup.find_all("h2") # find all quotes  
        
    for q in quotes[:21]:
#        print(f"{q.contents[0].strip()}")
        res = str(q).split("“")
        res2 = res[1][:-6]
        res3 = res2.split("” — ")
        print("quote: ",res3[0], "\nauteur: ", res3[1],"\n\n")

    return "hoi in ToonQuotes"