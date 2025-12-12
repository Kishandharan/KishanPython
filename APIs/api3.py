from flask import Flask
import mysql.connector

app1 = Flask(__name__)
junk = input("Enter Your ****: ")
con1 = mysql.connector.connect(
    host="localhost",
    user="root",
    password=junk,
    database="jokes"
)
cur1 = con1.cursor()

cur1.execute("select * from jokes");
out1 = cur1.fetchall()
print(out1)
