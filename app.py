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

# @app.route("/suzanneeerste")
# @cross_origin()
# def suzanneeerste():
#     return suzanne.methodevansuzanne()

# @app.route("/felixeerste")
# @cross_origin()
# def felixeerste():
#     return felix.methodevanfelix()

@app.route("/nieuwe_quote_opslaan/<a>/<t>")
def quote_nieuw(a,t):
    felix.nieuwe_quote_opslaan(a,t)
    return "Wij kunnen inderdaad een quote aanmaken"

@app.route('/felixposttrial2', methods = ['POST'])
def update_text2():
    return felix.postprobeersel(request)

@app.route('/maaltijden_datasave')
def maaltijden_datasave():
    return nelleke.datasave_maaltijden()


@app.route("/maaltijden")
@cross_origin()
def maaltijden():
    return nelleke.toon_maaltijden()

# @app.route("/maaltijd_rij/<num>")
# @cross_origin()
# def maaltijd_rij(num):
#     return nelleke.toon_maaltijd_rij(num)

@app.route("/maaltijd_random/")
@cross_origin()
def maaltijd_random():
    return nelleke.toon_maaltijd_random()

@app.route("/quotes/")
@cross_origin()
def quotes():
    return nelleke.quotes_tonen()

@app.route("/quote_random/")
@cross_origin()
def quote_random():
    print("het is gelukt wouter")
    return nelleke.quote_toon_random()
    
# @app.route("/quote_ranslim/")
# @cross_origin()
# def quote_ranslim():
#     return nelleke.quote_toon_ranslim()

# @app.route("/quotes_opslaan_sql/")
# @cross_origin()
# def quotes_opslaan_sql():
#     nelleke.quotes_opslaan_sql()
#     return "opslaan van quotes in sql database is gelukt"

# @app.route("/quotes_verversen/")
# @cross_origin()
# def ververs_quotes():
#     nelleke.quotes_opslaan_txt()
#     return "de quotes zijn ververst"