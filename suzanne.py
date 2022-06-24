import mysql.connector
from flask import jsonify

def methodevansuzanne():
	print("naar de database")
	mydb = mysql.connector.connect(
  		host="localhost", 
  		user="root",
  		password="",
  		database="patat"
	)

	mycursor = mydb.cursor()
	mycursor.execute("SELECT * FROM quote")
	recordset = mycursor.fetchall()
	print(recordset)

	return jsonify(list(recordset))

