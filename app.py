from flask import Flask
from flask_cors import CORS, cross_origin

import felix
#import nelleke
#import suzanne

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
