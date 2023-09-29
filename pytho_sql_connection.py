# import mysql.connector
# studentdb = mysql.connector.connect(
#     host='localhost', user='root', password='guru8296jadhav@', database="student_informations2")
# # print(studentdb.connection_id)
# cur = studentdb.cursor()
# # s="CREATE DATABASE {database name}" ----> creating new database
# # s="CREATE TABLE adharDetails(students int(4),adhar_number varchar(20),name varchar(50))"----> creating new table
# # s = "INSERT INTO adhardetails(students,adhar_number,name) VALUES(%s,%s,%s)"

# #inserting multiple values
# # details=[(2,"123456789","Amey Pradhan"),(3,"78945861222","Sushant Patil")]
# # cur.executemany(s,details)
# # studentdb.commit()

# # s="SELECT * from adhardetails"
# # cur.execute(s)
# # result=cur.fetchall()
# # for i in result:
# #     print(i)

# s=f" UPDATE studentsdetails SET PaidFees='45000' WHERE USN='2MM20EC002'"
# cur.execute(s)
# studentdb.commit()
# s=f" UPDATE studentsdetails SET BalanceFees='0' WHERE USN='2MM20EC002'"
# cur.execute(s)
# studentdb.commit()
# # a=int(input("Enter Sl Number to know the details of students"))
# # s=f"SELECT * from adhardetails WHERE students={a}"
# # cur.execute(s)
# # result=cur.fetchall()
# # print(result)
# # for i in result:
# #     for j in i:
# #         print(j)

# # a=200000
# # print(type(a))
# # a=10
# # b=20
# # c=30 
# # t=(a,b,c)
# # print(t)


# from tkinter import *
# import tkinter.messagebox as msg
# root=Tk()
# root.geometry("100x100")
# def show():
#     # msg.showerror("Wrong","Somthing wrong")
#     # msg.showwarning("Wrong","Somthing wrong")
#     # msg.askyesno("Confirmation","You can access ")
#     # msg.Message("hiii")
#     pass

# Button(root,text="Click",command=show).pack()

# print(f"%s,"*34)
# # root.mainloop()
from tkinter import *
from tkinter import ttk 
root=Tk()
root.geometry("200x200")
style=ttk.Style()
style.configure("BW.Tlabel",foreground="black",background="white")
l1=ttk.Label(root,text="Gurunath",style="BW.Tlabel").pack()
l2=ttk.Label(root,text="Jadhav",style="BW.Tlabel").pack()
root.mainloop()