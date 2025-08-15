import mysql.connector
connection = mysql.connector.connect(
    host="localhost", 
    user="root", 
    password="root",
    database="chat"    
)
cursor = connection.cursor()
inp1 = input(">>")#message
tup1 = (inp1, )
#s1 = "INSERT INTO chats (msgs) VALUES ("+"'"+inp1+"'"+")"
s1 = "INSERT INTO chats (msgs) VALUES (%s)"
cursor.execute(s1, tup1)
connection.commit()
