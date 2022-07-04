import mysql.connector
from flask import jsonify

mydb = mysql.connector.connect(
	host="2206-bezorgapp.mysql.database.azure.com",  #port erbij indien mac
	port=3306,
	user="beheerder@2206-bezorgapp",
	password="abcd1234ABCD!@#$",
	database="bezorgappyc2206"
)
def methodevanfelix():
	print("naar de database")
	mycursor = mydb.cursor()
	mycursor.execute("SELECT * FROM maaltijd")
	recordset = mycursor.fetchall()
	print(recordset)
	return jsonify(list(recordset))

def aanmakenquote(denaam):
	mycursor = mydb.cursor()
	sql = "INSERT INTO quote (tekst, auteur) VALUES (%s, %s)"
	val = (denaam, "harry")
	mycursor.execute(sql, val)
	mydb.commit()
	print(mycursor.rowcount, "record inserted.")

