import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "guru8296jadhav@",
    database = "student_information",
)
cur = mydb.cursor(buffered=True)

def getbyusn(usn):
    up = ("SELECT * FROM student_information.institution_details WHERE USN=(%s)")
    val = (usn,)
    cur.execute(up, val)
    result = cur.fetchall()
    return result

def getbyname(name):
    up = ("""SELECT * FROM student_information.institution_details WHERE name LIKE %s""")
    proc = name + "%"
    val = (proc,)
    cur.execute(up, val)
    result = cur.fetchall()
    return result
