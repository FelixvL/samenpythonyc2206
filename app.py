from flask import Flask
from flask import request
from flask_cors import CORS, cross_origin
import mysql.connector
from dotenv import load_dotenv
load_dotenv()

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
    return nelleke.toon_data_deel()

@app.route("/suzanneeerste")
@cross_origin()
def suzanneeerste():
    return suzanne.methodevansuzanne()

@app.route("/aanmakenquote/<name>")
def quoteaanmaken(name):
    felix.aanmakenquote(name)
    return "Wij kunnen inderdaad een quote aanmaken"

@app.route("/nelleketweede/<num>")
@cross_origin()
def nelleketweede(num):
    return nelleke.toon_data_specifiek(num)

@app.route("/nellekederde/")
@cross_origin()
def nellekederde():
    print("De derde doet het wel")
    return nelleke.toon_quotes_allemaal()

@app.route("/nellekevierde/")
@cross_origin()
def nellekevierde():
    return nelleke.random_quote()

@app.route('/felixposttrial', methods = ['POST'])
def update_text():
    return felix.postprobeersel(request)

@app.route("/nellekevijfde/")
@cross_origin()
def nellekevijfde():
    return nelleke.opslaan_quotes()

@app.route("/random_maaltijd/")
@cross_origin()
def random_maaltijd():
    return nelleke.toon_data_random()
    
    
