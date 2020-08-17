import mysql.connector
db = mysql.connector.connect(host ="localhost" ,user ="root" ,password ="admin",database ='student' )
mydb = db.cursor()


mydb.execute("select  *from studentdetails where fname ='chukwudi'")
my = mydb.fetchone()
for k in my:
    print(k)