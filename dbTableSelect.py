import mysql.connector
db = mysql.connector.connect(host ="localhost" ,user ="root" ,password ="admin",database ='shoes' )
mydb = db.cursor()

re = mydb.execute('show tables')
re = mydb.fetchall()
for i in re:
    print(i)