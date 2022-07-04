import mysql.connector
from flask import jsonify
import app

def methodevansuzanne():
	print("naar de database")
	mydb = app.getDBVerbinding()
	mycursor = mydb.cursor()
	mycursor.execute("SELECT * FROM quote")
	recordset = mycursor.fetchall()
	print(recordset)

	return jsonify(list(recordset))

