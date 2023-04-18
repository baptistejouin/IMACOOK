import mysql.connector

mydb = mysql.connector.connect(
	host="http://193.168.146.209/",
    user="admin",
    password="imabiencooke",
    database="imacook",
)

cursor = mydb.cursor()

cursor.execute("SELECT * FROM cookers")
cursor.commit()

cookers = cursor.fetchall()

print(cookers)