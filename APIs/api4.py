from flask import Flask
from flask_cors import CORS
import mysql.connector
from random import choice

app1 = Flask(__name__)
CORS(app1)
junk = input("Enter Your ****: ")
con1 = mysql.connector.connect(
    host="172.105.253.146",
    user="root",
    password=junk,
    database="jokes"
)
cur1 = con1.cursor()

cur1.execute("select * from jokes");
out1 = cur1.fetchall() # [ ( "Joke" , ), ( "Joke" , ),]

@app1.route("/joke")
def route1():
    randomJoke1 = choice(out1)
    randomJoke2 = randomJoke1[0]
    return {"joke": randomJoke2}

app1.run()

