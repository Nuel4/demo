import mysql.connector
db = mysql.connector.connect(host ="localhost" ,user ="root" ,password ="admin",database ='computer' )
mydb = db.cursor()

sqlform = "insert into company(id,brand ,quantity, price) values(%s ,%s,%s ,%s)"
prod =[(10 ,'HP' ,10 ,20000),(11,'Dell' ,20 ,25000),(12 ,"Apple",15 ,35000),(13 ,'LENOVO' ,13 ,15000),(14 ,'TOSHIBA',23 ,17000) ]
mydb.executemany(sqlform,prod)
db.commit()

print(a)