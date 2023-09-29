import mysql.connector
# from tkinter import *
# import tkinter.messagebox as msg

    # root=Tk()
    # root.geometry("500x200")
data=mysql.connector.connect(host='localhost',user="root",password="guru8296jadhav@",database="student_information")
cur=data.cursor()
def delete(usn):
    USN=usn
    s=f" DELETE FROM institution_details WHERE USN='{USN}'"
    cur.execute(s)
    data.commit()
    
    
    # s=f" DELETE FROM  pdfimg WHERE USN='{USN}'"
    # cur.execute(s)
    # data.commit()
    # msg.showinfo("Message", "Information Is Removed Succefully...")
    # exit()
    


# fram=Frame(root,width=550,highlightthickness=3,highlightbackground="red")
# fram.pack(ipadx=50,ipady=50,padx=10,pady=15)
# label=Label(fram,text="ENTER USN TO DELETE DATA",font=("Arial 15 bold"),fg="white",bg="purple")
# label.pack(pady=10,fill=BOTH)
# usn=StringVar()
# usn.set("")
# usnEntery=Entry(fram,textvariable=usn,font=("Arial 15 bold"))
# usnEntery.pack(padx=10,pady=20,ipadx=15,ipady=5)
# button=Button(fram,text="OK",font=("Arial 12 bold"),fg="white",bg="skyblue",command=delete,padx=5)
# button.pack(ipadx=25)
# root.mainloop()

delete("2MM20EC003")


    

