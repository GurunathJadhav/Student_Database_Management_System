import mysql.connector
DB=mysql.connector.connect(host='localhost',user="root",password="guru8296jadhav@")
s="CREATE DATABASE student_information"
cur=DB.cursor()
cur.execute(s)
print("Database Created")