import mysql.connector
db = mysql.connector.connect(host ="localhost" ,user ="root" ,password ="admin",database ='computer' )
mydb = db.cursor()

mydb.execute("select brand from company")
my = mydb.fetchone()
for k in my:
    print(k)