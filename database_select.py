# first install mysql-connector-python
import mysql.connector
db = mysql.connector.connect(host ="localhost" ,user ="root" ,password ="admin" , database = 'house')
mydb = db.cursor()
mydb.execute('select * from tenants')


for i in mydb:
    print(i)