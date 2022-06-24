import mysql.connector
from flask import jsonify

def methodevanfelix():
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

def aanmakenquote(denaam):
	mydb = mysql.connector.connect(
		host="localhost",  #port erbij indien mac
		user="root",
		password="",
		database="patat"
	)
	mycursor = mydb.cursor()
	sql = "INSERT INTO quote (tekst, auteur) VALUES (%s, %s)"
	val = (denaam, "harry")
	mycursor.execute(sql, val)
	mydb.commit()
	print(mycursor.rowcount, "record inserted.")

