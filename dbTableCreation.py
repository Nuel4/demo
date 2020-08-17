import mysql.connector
db = mysql.connector.connect(host ="localhost" ,user ="root" ,password ="admin",database ='shoes' )
mydb = db.cursor()
mydb.execute('create table footwear (idd int(10) ,name varchar(25) ,size varchar(20) ,price int(20))')
