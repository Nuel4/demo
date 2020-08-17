import mysql.connector
db = mysql.connector.connect(host ="localhost" ,user ="root" ,password ="admin" )
mydb = db.cursor()
mydb.execute('create database Shoes')
mydb.execute('show databases')
result = mydb.fetchall()
for i in result:
    print(i)
