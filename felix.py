from flask import jsonify
from flask import request
import json
import app


def methodevanfelix():
	mydb = app.getDBVerbinding()
	print("naar de database")
	mycursor = mydb.cursor()
	mycursor.execute("SELECT * FROM quote")
	recordset = mycursor.fetchall()
	print(recordset)
	return jsonify(list(recordset))

def aanmakenquote(denaam):
	mydb = app.getDBVerbinding()
	mycursor = mydb.cursor()
	sql = "INSERT INTO quote (tekst, auteur) VALUES (%s, %s)"
	val = (denaam, "harry")
	mycursor.execute(sql, val)
	mydb.commit()
	print(mycursor.rowcount, "record inserted.")

def postprobeersel(verzoek):
	if verzoek.method == 'POST':
		jsonResponse = json.loads(verzoek.data.decode('utf-8'))
		print(jsonResponse["naam"])
		return jsonResponse["naam"]
	return "{\"oo\":\"GEEN POST\"}"