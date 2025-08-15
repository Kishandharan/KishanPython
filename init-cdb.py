import mysql.connector
connection = mysql.connector.connect(host="localhost", user="root", password="root")
cursor = connection.cursor()
cursor.execute("CREATE DATABASE chat")
cursor.execute("USE chat")
cursor.execute("CREATE TABLE chats (msgs VARCHAR(2000))")
