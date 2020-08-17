import mysql.connector
db = mysql.connector.connect(host ="localhost" ,user ="root" ,password ="admin",database ='student' )
mydb = db.cursor()


sql = "delete  from studentdetails where fname ='rita'"
mydb.execute(sql)
db.commit()