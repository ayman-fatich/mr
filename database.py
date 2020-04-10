import mysql.connector

mydb = mysql.connector.connect(
	host = "localhost",
	user = "root",
	passwd = "AYfaof26..@",
	database = "moulay_rachid",
)

crsr = mydb.cursor()

crsr.execute("CREATE TABLE posts (title VARCHAR(50), author VARCHAR(50), file VARCHAR(150), date DATETIME, subject VARCHAR(100), field VARCHAR(50), post_id INTEGER AUTO_INCREMENT PRIMARY KEY)")
mydb.commit()

