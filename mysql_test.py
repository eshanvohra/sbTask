import mysql.connector

connection=mysql.connector.connect(host="localhost",user="root",password="password", database="home_builder")

cursor=connection.cursor()



insert_query = "INSERT INTO labours_table (name, role, wages) VALUES (%s, %s, %s)"
cursor.execute(insert_query, ('New Labour', 'labour', 600))
connection.commit()

connection.close()
cursor.close()
# cursor.execute("select name,wages from labours_table")

# res=cursor.fetchall();

# print(res)