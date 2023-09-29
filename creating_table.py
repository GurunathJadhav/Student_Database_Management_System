import mysql.connector
table=mysql.connector.connect(host='localhost',user="root",password="guru8296jadhav@",database="student_information")
cur=table.cursor()
# s="CREATE TABLE institution_details(USN varchar(50),name varchar(70),phone varchar(15),email varchar(30),sem integer(2),admissionmode varchar(20) ,admissionyear varchar(10))"
s="CREATE TABLE institution_details(USN varchar(20),name varchar(50),phone varchar(15),branch varchar(50),dob varchar(10),sem int(2),quota varchar(50),gender varchar(10),domicile varchar(50),physical varchar(10),medium varchar(30),schooler varchar(30),admission_year int(10),Photo MEDIUMBLOB)"
# s="CREATE TABLE personal_details(USN varchar(50),personal_name varchar(70),fathername varchar(70),mothername varchar(70),adharnumbar varchar(20),parentsphone varchar(15),occupation varchar(20),catagory varchar(20),religion varchar(20),caste varchar(20),national varchar(20),annualincome int(10),village varchar(10),taluka varchar(20),state varchar(20),address varchar(100),Email varchar(50))"
# s="CREATE TABLE userlogin(USN varchar(20),password varchar(10))"
# s="CREATE TABLE student_attendence(USN varchar(50),sub1 varchar(50),ttclass1 int(10),aclass1 int(10),sub2 varchar(50),ttclass2 int(10),aclass2 int(10),sub3 varchar(50),ttclass3 int(10),aclass3 int(10),sub4 varchar(50),ttclass4 int(10),aclass4 int(10),sub5 varchar(50),ttclass5 int(10),aclass5 int(10),sub6 varchar(50),ttclass6 int(10),aclass6 int(10),sub7 varchar(50),ttclass7 int(10),aclass7 int(10),sub8 varchar(50),ttclass8 int(10),aclass8 int(10),lab1 varchar(50),ttlab1 int(10),alab1 int(10),lab2 varchar(50),ttlab2 int(10),alab2 int(10),lab3 varchar(50),ttlab3 int(10),alab3 int(10))"
# cur.execute(s)

cur.execute("CREATE TABLE pdfimg(usn varchar(20),Photo MEDIUMBLOB)")
# s=f"DROP TABLE pdfimg "
# cur.execute(s)
print("Table created ")