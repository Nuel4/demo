import mysql.connector
db = mysql.connector.connect(host ="localhost" ,user ="root" ,password ="admin",database ='computer' )
mydb = db.cursor()


sqlform = "insert into company(id,brand ,quantity, price) values(15 ,'SAMSUNG' ,5 ,30000)"
mydb.execute(sqlform)
db.commit()  # used to save changes