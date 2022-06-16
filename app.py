from flask import Flask
import felix
import nelleke
import suzanne

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/felixeerste")
def felixeerste():
    return felix.methodevanfelix()

@app.route("/nellekeeerste")
def nellekeeerste():
    return nelleke.methodevannelleke()

@app.route("/suzanneeerste")
def suzanneeerste():
    return suzanne.methodevansuzanne()