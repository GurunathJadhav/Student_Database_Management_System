import mysql.connector
table=mysql.connector.connect(host='localhost',user="root",password="guru8296jadhav@",database="student_information")
cur=table.cursor(buffered=True)
def Insert_institution_details(USN,name,phone,branch,dob,sem,quota,gender,domicile,physical,medium,schooler,admission_year):
    # s="INSERT INTO  student_information.institution_details(USN,name,phone,branch,dob,sem,quota,gender,domicile,physical,medium,schooler,admission_year) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    # details=(USN,name,phone,branch,dob,sem,quota,gender,domicile,physical,medium,schooler,admission_year)
    # print(details)
    cur.execute("INSERT INTO  student_information.institution_details(USN,name,phone,branch,dob,sem,quota,gender,domicile,physical,medium,schooler,admission_year) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(USN,name,phone,branch,dob,sem,quota,gender,domicile,physical,medium,schooler,admission_year))
    table.commit()
    
def Insert_personal_details(USN,personalName,fatherName,motherName,adharnumbar,parentsphone,occupation,catagory,religion,caste,national,annualincome,village,taluka,state,address,Email):
    # s="INSERT INTO  student_information.personal_details(USN,personal_name,fatherName,motherName,adharnumbar,parentsphone,occupation,catagory,religion,caste,national,annualincome,village,taluka,state,address) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    # details=(USN,personalName,fatherName,motherName,adharnumbar,parentsphone,occupation,catagory,religion,caste,national,annualincome,village,taluka,state,address)
    # print(details)
    cur.execute("INSERT INTO  student_information.personal_details(USN,personal_name,fatherName,motherName,adharnumbar,parentsphone,occupation,catagory,religion,caste,national,annualincome,village,taluka,state,address,Email) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(USN,personalName,fatherName,motherName,adharnumbar,parentsphone,occupation,catagory,religion,caste,national,annualincome,village,taluka,state,address,Email))
    table.commit()
    
def Insert_user_passoword(USN,password):
    # s="INSERT INTO  student_information.userlogin(USN,password) VALUES(%s,%s)"
    # details=(USN,password)
    cur.execute("INSERT INTO  student_information.userlogin(USN,password) VALUES(%s,%s)",(USN,password))
    table.commit()
    
def Insert_student_attendence(USN,sub1,ttclass1,aclass1,sub2,ttclass2,aclass2,sub3,ttclass3,aclass3,sub4,ttclass4,aclass4,sub5,ttclass5,aclass5,sub6,ttclass6,aclass6,sub7,ttclass7,aclass7,sub8,ttclass8,aclass8,lab1,ttlab1,alab1,lab2,ttlab2,alab2,lab3,ttlab3,alab3):
    
    cur.execute("INSERT INTO  student_information.student_attendence(USN,sub1,ttclass1,aclass1,sub2,ttclass2,aclass2,sub3,ttclass3,aclass3,sub4,ttclass4,aclass4,sub5,ttclass5,aclass5,sub6,ttclass6,aclass6,sub7,ttclass7,aclass7,sub8,ttclass8,aclass8,lab1,ttlab1,alab1,lab2,ttlab2,alab2,lab3,ttlab3,alab3) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(USN,sub1,ttclass1,aclass1,sub2,ttclass2,aclass2,sub3,ttclass3,aclass3,sub4,ttclass4,aclass4,sub5,ttclass5,aclass5,sub6,ttclass6,aclass6,sub7,ttclass7,aclass7,sub8,ttclass8,aclass8,lab1,ttlab1,alab1,lab2,ttlab2,alab2,lab3,ttlab3,alab3))
    table.commit()