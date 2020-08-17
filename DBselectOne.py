import mysql.connector
db = mysql.connector.connect(host ="localhost" ,user ="root" ,password ="admin" , database = 'house')
mydb = db.cursor()
mydb.execute('select * from tenants')
result = mydb.fetchone()
for i in result:
    print(i)