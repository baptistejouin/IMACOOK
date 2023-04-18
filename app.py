import mysql.connector as MC

try:
	conn = MC.connect(host = 'localhost', database = 'imacook', user = 'root', password = "")
except MC.Error as err:
	print(err)
finally:
	if(conn.is_connected()):
		conn.cursor.close()
		conn.close()
		conn.execute("SELECT * FROM cookers")
		cookers = conn.fetchall()
		conn.commit()
		print(cookers)
