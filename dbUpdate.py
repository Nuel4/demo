import mysql.connector
db = mysql.connector.connect(host ="localhost" ,user ="root" ,password ="admin",database ='computer' )
mydb = db.cursor()


sql = "update company set price =35000 where brand = 'hp' "
mydb.execute(sql)
db.commit()