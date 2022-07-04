from flask import jsonify
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

