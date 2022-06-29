import mysql.connector
from flask import jsonify
import pandas as pd

def methodevannelleke():
	print("naar de database")
	mydb = mysql.connector.connect(
		host="localhost",  #port erbij indien mac
		user="root",
		password="",
		database="patat"
)
	mycursor = mydb.cursor()
	mycursor.execute("SELECT * FROM quote")
	recordset = mycursor.fetchall()
	print(recordset)
	return jsonify(list(recordset))

# import csv file
try:
    df = pd.read_csv("C:/Users/Nelleke/Documents/YC/Traineeship/samenpythonyc2206/data/maaltijden.csv")
except Exception as err:
    print(err)
    
print(df)