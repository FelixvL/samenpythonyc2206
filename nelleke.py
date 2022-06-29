import mysql.connector
from flask import jsonify
import pandas as pd

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