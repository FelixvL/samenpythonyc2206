import mysql.connector
from flask import jsonify


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

