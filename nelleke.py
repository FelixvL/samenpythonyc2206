import mysql.connector
from flask import jsonify, Response
import pandas as pd
import bs4
import requests
import json
import re
import random
from pathlib import Path

CWD = Path(__file__).parent
DATAPATH = CWD / "data"

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

def toon_maaltijden():     
    print(df.head())
    return "toon maaltijden is gelukt"

def toon_maaltijd_rij(num):
    row = int(num)
    toon = df.iloc[row]
    print(toon)
    return toon.to_json()

def toon_maaltijd_random():
    return df.sample().to_json(orient="records")

def get_quotes():    
    try: # errorhandling
        rg = requests.get("https://medium.com/swlh/21-of-the-worlds-most-powerful-quotes-updated-for-today-and-tomorrow-6b7634358c2") # GET document from medium.com        
    except Exception as err: 
        print("Something went wrong:", err)
        rg = None
        
    html_doc = rg.text # get HMTL content from response object
    soup = bs4.BeautifulSoup(html_doc, 'html.parser') # turn html_doc into BS4 object
    quotes = soup.find_all("h2") # find all quotes  
    
    quotes_lijst = []
    
    for q in quotes[:21]:
        res = str(q).split("“")
        res2 = res[1][:-5]
        res3 = res2.split("” — ")
        
        tekst_en_auteur = (f"{res3[0]} - {res3[1]}")
        quotes_lijst.append(tekst_en_auteur)
    
    return quotes_lijst

def quotes_opslaan_txt():
    quotes = get_quotes()

    # maak datapath aan en als deze bestaat, geef dan geen error
    DATAPATH.mkdir(exist_ok=True)

    with open(DATAPATH / "quotes.txt", "w") as f:
        for q in quotes:
            f.write(q + "\n")
    
    return quotes.txt

def quotes_lezen_txt():
    quotes_bestand = DATAPATH / "quotes.txt"
    if not quotes_bestand.exists():
        quotes_opslaan_txt()
    else:
        pass

    new_quotes = []
    with open(quotes_bestand, "r") as f:
        for line in f:
            new_quotes.append(line.strip())
    return new_quotes

def quotes_tonen():
    return jsonify(quotes_lezen_txt())

def quote_toon_random():
    nummer = random.randint(0, 20)
    quotes = quotes_lezen_txt()
    print(type(quotes))
    resultaat = {"quote":quotes[nummer]} 
    return jsonify(resultaat)

def quote_toon_ranslim():
    quotes = quotes_lezen_txt()
    return random.choice(quotes)

def quotes_opslaan_sql():    
    quotes = quotes_lezen_txt()

    mycursor = mydb.cursor()
    # leeg tabel
    mycursor.execute("DELETE FROM quote")
    
    # reset index
    mycursor.execute("ALTER TABLE quote AUTO_INCREMENT = 1")

    for quote in quotes[:21]:        
        tekst, auteur = quote.split(" - ")
    
        sql = "INSERT INTO quote (tekst, auteur) VALUES (%s, %s)"
        val = (tekst, auteur)
        mycursor.execute(sql, val)
        print(mycursor.rowcount, "record inserted.")
    
    mydb.commit()