import mysql.connector
data=mysql.connector.connect(host='localhost',user="root",password="guru8296jadhav@",database="student_information")
cur=data.cursor(buffered=True)

def Access_institution_details(usn):
    s=f"SELECT * FROM institution_details WHERE USN='{usn}'"
    cur.execute(s)
    return cur.fetchall()
def Access_institution_details_name(name):
    s=f"SELECT * FROM institution_details WHERE name='{name}'"
    cur.execute(s)
    return cur.fetchall()

def Access_personal_details(usn):
    s=f"SELECT * FROM personal_details WHERE USN='{usn}'"
    cur.execute(s)
    return cur.fetchall()

def Access_user_password(usn):
    s=f"SELECT * FROM userlogin WHERE USN='{usn}'"
    cur.execute(s)
    return cur.fetchall()

def Access_student_attendence(usn):
    s=f"SELECT * FROM student_attendence WHERE USN='{usn}'"
    cur.execute(s)
    return cur.fetchall()
# data=Access_student_attendence("2MM20EC002")
# print(data)
    

    
    
