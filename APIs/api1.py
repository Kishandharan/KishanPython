from flask import Flask
import mysql.connector

app1 = Flask(__name__)
pwd1 = input("Enter your MySQL password: ")
con1 = mysql.connector.connect(
    host="localhost",
    user="root",
    password=pwd1
)
cur1 = con1.cursor()

@app1.route("/createdb/<dbname>")
def route1(dbname):
    cur1.execute("create database "+dbname+";")
    return {"status":"done"}

@app1.route("/deletedb/<dbname>")
def route2(dbname):
    cur1.execute("drop database "+dbname+";")
    return {"status":"done"}

app1.run()
