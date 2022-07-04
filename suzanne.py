import mysql.connector
from flask import jsonify

mydb = mysql.connector.connect(
	host="2206-bezorgapp.mysql.database.azure.com",  #port erbij indien mac
	port=3306,
	user="beheerder@2206-bezorgapp",
	password="abcd1234ABCD!@#$",
	database="bezorgappyc2206"
)

def methodevansuzanne():
	print("naar de database")

	mycursor = mydb.cursor()
	mycursor.execute("SELECT * FROM maaltijd")
	recordset = mycursor.fetchall()
	print(recordset)

	return jsonify(list(recordset))

