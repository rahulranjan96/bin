import pymysql.cursors

word = input("Enter the word:")
print("Meaning:")
conn = pymysql.connect(database='entries',user='root',host='localhost')
cursor=conn.cursor()
query = "SELECT `definition` FROM `entries` WHERE `word` = %s"
cursor.execute(query,(word))
meaning=cursor.fetchone()
print(meaning)
cursor.close()
conn.close()
	