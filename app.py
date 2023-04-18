import mysql.connector

mydb = mysql.connector.connect(
	host="localhost",
    user="admin",
    password="imabiencooke",
    database="imacook",
)

cursor = mydb.cursor()

cursor.execute("SELECT * FROM cookers")
cursor.commit()

cookers = cursor.fetchall()

print(cookers)

cursor.close()