import mysql.connector
db = mysql.connector.connect(host ="localhost" ,user ="root" ,password ="admin",database ='computer' )
mydb = db.cursor()

#sqlform = "insert into company values(10 ,'HP' ,10 ,20000) "
#mydb.execute(sqlform)
mydb.execute("select * from company")
my = mydb.fetchall()
for k in my:
    print(k)
