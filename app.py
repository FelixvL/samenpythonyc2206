import mysql.connector
from dotenv import load_dotenv
from flask import Flask, request
from flask_cors import CORS, cross_origin

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

@app.route("/suzanneeerste")
@cross_origin()
def suzanneeerste():
    return suzanne.methodevansuzanne()

@app.route("/felixeerste")
@cross_origin()
def felixeerste():
    return felix.methodevanfelix()

@app.route("/aanmakenquote/<name>")
def quoteaanmaken(name):
    felix.aanmakenquote(name)
    return "Wij kunnen inderdaad een quote aanmaken"

<<<<<<< HEAD
=======
@app.route("/nelleketweede/<num>")
@cross_origin()
def nelleketweede(num):
    return nelleke.toon_data_rij(num)

@app.route("/nellekederde/")
@cross_origin()
def nellekederde():
    print("De derde doet het wel")
    return nelleke.quotes_tonen_allemaal()

@app.route("/nellekevierde/")
@cross_origin()
def nellekevierde():
    return nelleke.quote_random()

>>>>>>> master
@app.route('/felixposttrial', methods = ['POST'])
def update_text():
    return felix.postprobeersel(request)

@app.route("/maaltijden")
@cross_origin()
def maaltijden():
    return nelleke.toon_data()

@app.route("/maaltijd_rij/<num>")
@cross_origin()
def toon_maaltijd_rij(num):
    return nelleke.toon_data_rij(num)

@app.route("/maaltijd_random/")
@cross_origin()
def maaltijd_random():
    return nelleke.toon_data_random()

@app.route("/quotes/")
@cross_origin()
def quotes():
    print("De derde doet het wel")
    return nelleke.toon_quotes_allemaal()

@app.route("/quote_random/")
@cross_origin()
def toon_random_quote():
    return nelleke.quote_random()

@app.route("/quotes_opslaan_sql/")
@cross_origin()
def quotes_opslaan_sql():
    nelleke.quotes_opslaan_sql()
    return "opslaan van quotes in sql database is gelukt"

@app.route("/quotes_verversen/")
@cross_origin()
def ververs_quotes():
    nelleke.quotes_opslaan_txt()
    return "de quotes zijn ververst"

@app.route("/quote_random/")
@cross_origin()
def random_maaltijd():
    return nelleke.toon_data_random()

<<<<<<< HEAD
# @app.route("/quote_random2/")
# @cross_origin()
# def quote_random2():
#     return nelleke.quote_ranslim()
=======
@app.route("/ververs_quotes/")
@cross_origin()
def ververs_quotes():
    nelleke.quotes_opslaan_txt()
    return "de quotes zijn ververst"
>>>>>>> master
