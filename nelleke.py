import mysql.connector
from flask import jsonify, Response
import pandas as pd
import bs4
import requests
import json
import re
import random
from pathlib import Path
from sqlalchemy import create_engine
import MySQLdb
import collections

CWD = Path(__file__).parent
DATAPATH = CWD / "data"

mydb = mysql.connector.connect(
	host="2206-bezorgapp.mysql.database.azure.com",  #port erbij indien mac
	port=3306,
	user="beheerder@2206-bezorgapp",
	password="abcd1234ABCD!@#$",
	database="bezorgappbigdata"
)
# import data
try:
    df = pd.read_csv("./data/maaltijden.csv")
except Exception as err:
    print(err)
        
def toon_maaltijden():     
    print(df.head())
    return "toon maaltijden is gelukt"

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
    
    mycursor = mydb.cursor()
    for q in quotes[:21]:
        res = str(q).split("“")
        res2 = res[1][:-5]
        res3 = res2.split("” — ")

        # check if quote in db
        sql = "SELECT COUNT(*) from quote WHERE tekst = %s"
        val = (res3[0],)
        mycursor.execute(sql, val)
        aantal = mycursor.fetchone()

        # als niet in db, dan toevoegen
        if aantal[0] == 0:
            sql = "INSERT INTO quote (tekst, auteur) VALUES (%s, %s)"
            val = (res3[0], res3[1])
            mycursor.execute(sql, val)
            print(mycursor.rowcount, "record inserted.")

    mydb.commit()

def quotes_tonen():
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM quote")

    quotes_in_sql = mycursor.fetchall()
    quotes = []
    for q in quotes_in_sql:
        d = collections.OrderedDict()
        d["ID"] = q[0]
        d["tekst"] = q[1]
        d["auteur"] = q[2]
 
        quotes.append(d)
    
    return jsonify(quotes)


def quote_toon_random():
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM quote order by RAND() limit 1")

    quotes_in_sql = mycursor.fetchall()
    quotes = []
    for q in quotes_in_sql:
        d = collections.OrderedDict()
        d["ID"] = q[0]
        d["tekst"] = q[1]
        d["auteur"] = q[2]
 
        quotes.append(d)
    
    return jsonify(quotes)