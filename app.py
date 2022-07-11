from flask import Flask
from flask import request
from flask_cors import CORS, cross_origin
import mysql.connector

def getDBVerbinding():
   
    mydb = mysql.connector.connect(
        host="2206-bezorgapp.mysql.database.azure.com",  #port erbij indien mac
        port=3306,
        user="beheerder@2206-bezorgapp",
        password="abcd1234ABCD!@#$",
        database="bezorgappbigdata"
    )
    '''
    mydb = mysql.connector.connect(
        host="localhost",  #port erbij indien mac
        port=3306,
        user="root",
        password="",
        database="patat"
    )
    ''' 
    return mydb

import felix
import nelleke
import suzanne

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route("/")
@cross_origin()
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/felixeerste")
@cross_origin()
def felixeerste():
    return felix.methodevanfelix()

@app.route("/nellekeeerste")
@cross_origin()
def nellekeeerste():
    return nelleke.toonDataDeel()

@app.route("/suzanneeerste")
@cross_origin()
def suzanneeerste():
    return suzanne.methodevansuzanne()

@app.route("/aanmakenquote/<name>")
def quoteaanmaken(name):
    felix.aanmakenquote(name)
    return "hij doet het"

@app.route("/nelleketweede/<num>")
@cross_origin()
def nelleketweede(num):
    return nelleke.toonDataSpecifiek(num)

@app.route("/nellekederde/")
@cross_origin()
def nellekederde():
    return nelleke.toonQuotes()

@app.route("/nellekevierde/")
@cross_origin()
def nellekevierde():
    return nelleke.opslaanQuotes()


@app.route('/felixposttrial', methods = ['POST'])
def update_text():
    return felix.postprobeersel(request)
