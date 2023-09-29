from tkinter import *
def Export():
        import csv

        import tkinter.messagebox as msg
       
        root=Tk()
        root.geometry("500x200")
        def add():
                data1=""
                try:
                        from accessing import Access_institution_details
                        data=Access_institution_details(usn.get().upper())
                        data1=data[0]
                except:""
                with open("StudentInformation.csv","a") as f:
                        w=csv.writer(f,dialect='excel')
                        w.writerow(data1) 
                        msg.showinfo("Export","Export Successfully")
                

        # print(data[0])
        # for info in data[0]:
        #     print(info)
        label=Label(root,text="Exporting Data",font="Arial 15 bold")
        label.place(x=200,y=5)
        usn=StringVar()
        usn.set("")
        usnentry=Entry(root,textvariable=usn,width=20,font="Arial 15 bold")
        usnentry.place(x=150,y=50)

        btn=Button(root,text="Export",font="Arial 10 bold",width=8,command=add)
        btn.place(x=230,y=110)
        root.mainloop()
        
if __name__== '__main__':
        Export()