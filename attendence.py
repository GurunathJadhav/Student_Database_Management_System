from tkinter import *
def attendence():
    root=Tk()
    root.geometry("1000x600")
    root.maxsize(1000,600)
    root.minsize(1000,600)
    frame1=Frame(root,width=1000,height=600,bg="#E8E8E8")
    frame1.place(x=0,y=0)
    sideframe=Frame(frame1,width=250,height=600,bg="lightgray")
    sideframe.place(x=750,y=0)
    frame_attendence=Frame(frame1,width=720,height=600,bg="#E8E8E8")
    frame_attendence.place(x=0,y=0)
    
    def add():
        print(subject1.get())
        pass

    label=Label(frame1,text="Student Attendence Registration",font="Arial 15 bold",bg="#E8E8E8",fg="red")
    label.place(x=200,y=10)

    subjectslabel=Label(frame_attendence,text="Subjects",font="Arial 15 bold",bg="#E8E8E8")
    subjectslabel.place(x=150,y=50)

    totalclasslabel=Label(frame_attendence,text="Total Classes",font="Arial 15 bold",bg="#E8E8E8")
    totalclasslabel.place(x=370,y=50)

    attendedclasses=Label(frame_attendence,text="Attended Classes",font="Arial 15 bold",bg="#E8E8E8")
    attendedclasses.place(x=550,y=50)

    usn=StringVar()
    usn.set("")
    usnEntry=Entry(sideframe,textvariable=usn,font="Arial 15 bold",width=18)
    usnEntry.place(x=25,y=12)

    subject1=StringVar()
    subject1.set("")
    subject1label=Label(frame_attendence,text="Subject 1",font="Arial 10 bold",bg="#E8E8E8")
    subject1label.place(x=10,y=100)
    subject1Entry=Entry(frame_attendence,textvariable=subject1,width=35,font="Arial 10 bold",highlightbackground="black",highlightthickness=1)
    subject1Entry.place(x=80,y=100)

    subject1total=IntVar()
    subject1total.set("")
    subject1totalEntry=Entry(frame_attendence,textvariable=subject1total,width=15,font="Arial 10 bold",highlightbackground="black",highlightthickness=1)
    subject1totalEntry.place(x=570,y=100)

    subject1attend=IntVar()
    subject1attend.set("")
    subject1attendEntry=Entry(frame_attendence,textvariable=subject1attend,width=15,font="Arial 10 bold",highlightbackground="black",highlightthickness=1)
    subject1attendEntry.place(x=380,y=100)

    subject2=StringVar()
    subject2.set("")
    subject2label=Label(frame_attendence,text="Subject 2",font="Arial 10 bold",bg="#E8E8E8")
    subject2label.place(x=10,y=140)
    subject2Entry=Entry(frame_attendence,textvariable=subject2,width=35,font="Arial 10 bold",highlightbackground="black",highlightthickness=1)
    subject2Entry.place(x=80,y=140)

    subject2total=IntVar()
    subject2total.set("")
    subject2totalEntry=Entry(frame_attendence,textvariable=subject2total,width=15,font="Arial 10 bold",highlightbackground="black",highlightthickness=1)
    subject2totalEntry.place(x=570,y=140)

    subject2attend=IntVar()
    subject2attend.set("")
    subject2attendEntry=Entry(frame_attendence,textvariable=subject2attend,width=15,font="Arial 10 bold",highlightbackground="black",highlightthickness=1)
    subject2attendEntry.place(x=380,y=140)

    subject3=StringVar()
    subject3.set("")
    subject3label=Label(frame_attendence,text="Subject 3",font="Arial 10 bold",bg="#E8E8E8")
    subject3label.place(x=10,y=180)
    subject3Entry=Entry(frame_attendence,textvariable=subject3,width=35,font="Arial 10 bold",highlightbackground="black",highlightthickness=1)
    subject3Entry.place(x=80,y=180)

    subject3total=IntVar()
    subject3total.set("")
    subject3totalEntry=Entry(frame_attendence,textvariable=subject3total,width=15,font="Arial 10 bold",highlightbackground="black",highlightthickness=1)
    subject3totalEntry.place(x=570,y=180)

    subject3attend=IntVar()
    subject3attend.set("")
    subject3attendEntry=Entry(frame_attendence,textvariable=subject3attend,width=15,font="Arial 10 bold",highlightbackground="black",highlightthickness=1)
    subject3attendEntry.place(x=380,y=180)

    subject4=StringVar()
    subject4.set("")
    subject4label=Label(frame_attendence,text="Subject 4",font="Arial 10 bold",bg="#E8E8E8")
    subject4label.place(x=10,y=220)
    subject4Entry=Entry(frame_attendence,textvariable=subject4,width=35,font="Arial 10 bold",highlightbackground="black",highlightthickness=1)
    subject4Entry.place(x=80,y=220)

    subject4total=IntVar()
    subject4total.set("")
    subject4totalEntry=Entry(frame_attendence,textvariable=subject4total,width=15,font="Arial 10 bold",highlightbackground="black",highlightthickness=1)
    subject4totalEntry.place(x=570,y=220)

    subject4attend=IntVar()
    subject4attend.set("")
    subject4attendEntry=Entry(frame_attendence,textvariable=subject4attend,width=15,font="Arial 10 bold",highlightbackground="black",highlightthickness=1)
    subject4attendEntry.place(x=380,y=220)

    subject5=StringVar()
    subject5.set("")
    subject5label=Label(frame_attendence,text="Subject 5",font="Arial 10 bold",bg="#E8E8E8")
    subject5label.place(x=10,y=260)
    subject5Entry=Entry(frame_attendence,textvariable=subject5,width=35,font="Arial 10 bold",highlightbackground="black",highlightthickness=1)
    subject5Entry.place(x=80,y=260)

    subject5total=IntVar()
    subject5total.set("")
    subject5totalEntry=Entry(frame_attendence,textvariable=subject5total,width=15,font="Arial 10 bold",highlightbackground="black",highlightthickness=1)
    subject5totalEntry.place(x=570,y=260)

    subject5attend=IntVar()
    subject5attend.set("")
    subject5attendEntry=Entry(frame_attendence,textvariable=subject5attend,width=15,font="Arial 10 bold",highlightbackground="black",highlightthickness=1)
    subject5attendEntry.place(x=380,y=260)

    subject6=StringVar()
    subject6.set("")
    subject6label=Label(frame_attendence,text="Subject 6",font="Arial 10 bold",bg="#E8E8E8")
    subject6label.place(x=10,y=300)
    subject6Entry=Entry(frame_attendence,textvariable=subject6,width=35,font="Arial 10 bold",highlightbackground="black",highlightthickness=1)
    subject6Entry.place(x=80,y=300)

    subject6total=IntVar()
    subject6total.set("")
    subject6totalEntry=Entry(frame_attendence,textvariable=subject6total,width=15,font="Arial 10 bold",highlightbackground="black",highlightthickness=1)
    subject6totalEntry.place(x=570,y=300)

    subject6attend=IntVar()
    subject6attend.set("")
    subject6attendEntry=Entry(frame_attendence,textvariable=subject6attend,width=15,font="Arial 10 bold",highlightbackground="black",highlightthickness=1)
    subject6attendEntry.place(x=380,y=300)

    subject7=StringVar()
    subject7.set("")
    subject7label=Label(frame_attendence,text="Subject 7",font="Arial 10 bold",bg="#E8E8E8")
    subject7label.place(x=10,y=340)
    subject7Entry=Entry(frame_attendence,textvariable=subject7,width=35,font="Arial 10 bold",highlightbackground="black",highlightthickness=1)
    subject7Entry.place(x=80,y=340)

    subject7total=IntVar()
    subject7total.set("")
    subject7totalEntry=Entry(frame_attendence,textvariable=subject7total,width=15,font="Arial 10 bold",highlightbackground="black",highlightthickness=1)
    subject7totalEntry.place(x=570,y=340)

    subject7attend=IntVar()
    subject7attend.set("")
    subject7attendEntry=Entry(frame_attendence,textvariable=subject7attend,width=15,font="Arial 10 bold",highlightbackground="black",highlightthickness=1)
    subject7attendEntry.place(x=380,y=340)

    subject8=StringVar()
    subject8.set("")
    subject8label=Label(frame_attendence,text="Subject 8",font="Arial 10 bold",bg="#E8E8E8")
    subject8label.place(x=10,y=380)
    subject8Entry=Entry(frame_attendence,textvariable=subject8,width=35,font="Arial 10 bold",highlightbackground="black",highlightthickness=1)
    subject8Entry.place(x=80,y=380)

    subject8total=IntVar()
    subject8total.set("")
    subject8totalEntry=Entry(frame_attendence,textvariable=subject8total,width=15,font="Arial 10 bold",highlightbackground="black",highlightthickness=1)
    subject8totalEntry.place(x=570,y=380)

    subject8attend=IntVar()
    subject8attend.set("")
    subject8attendEntry=Entry(frame_attendence,textvariable=subject8attend,width=15,font="Arial 10 bold",highlightbackground="black",highlightthickness=1)
    subject8attendEntry.place(x=380,y=380)

    lab1=StringVar()
    lab1.set("")
    lab1label=Label(frame_attendence,text="Lab 1",font="Arial 10 bold",bg="#E8E8E8")
    lab1label.place(x=10,y=420)
    lab1Entry=Entry(frame_attendence,textvariable=lab1,width=35,font="Arial 10 bold",highlightbackground="black",highlightthickness=1)
    lab1Entry.place(x=80,y=420)

    lab1total=IntVar()
    lab1total.set("")
    lab1totalEntry=Entry(frame_attendence,textvariable=lab1total,width=15,font="Arial 10 bold",highlightbackground="black",highlightthickness=1)
    lab1totalEntry.place(x=570,y=420)

    lab1attend=IntVar()
    lab1attend.set("")
    lab1attendEntry=Entry(frame_attendence,textvariable=lab1attend,width=15,font="Arial 10 bold",highlightbackground="black",highlightthickness=1)
    lab1attendEntry.place(x=380,y=420)

    lab2=StringVar()
    lab2.set("")
    lab2label=Label(frame_attendence,text="Lab 2",font="Arial 10 bold",bg="#E8E8E8")
    lab2label.place(x=10,y=460)
    lab2Entry=Entry(frame_attendence,textvariable=lab2,width=35,font="Arial 10 bold",highlightbackground="black",highlightthickness=1)
    lab2Entry.place(x=80,y=460)

    lab2total=IntVar()
    lab2total.set("")
    lab2totalEntry=Entry(frame_attendence,textvariable=lab2total,width=15,font="Arial 10 bold",highlightbackground="black",highlightthickness=1)
    lab2totalEntry.place(x=570,y=460)

    lab2attend=IntVar()
    lab2attend.set("")
    lab2attendEntry=Entry(frame_attendence,textvariable=lab2attend,width=15,font="Arial 10 bold",highlightbackground="black",highlightthickness=1)
    lab2attendEntry.place(x=380,y=460)

    lab3=StringVar()
    lab3.set("")
    lab3label=Label(frame_attendence,text="Lab 3",font="Arial 10 bold",bg="#E8E8E8")
    lab3label.place(x=10,y=500)
    lab3Entry=Entry(frame_attendence,textvariable=lab3,width=35,font="Arial 10 bold",highlightbackground="black",highlightthickness=1)
    lab3Entry.place(x=80,y=500)

    lab3total=IntVar()
    lab3total.set("")
    lab3totalEntry=Entry(frame_attendence,textvariable=lab3total,width=15,font="Arial 10 bold",highlightbackground="black",highlightthickness=1)
    lab3totalEntry.place(x=570,y=500)

    lab3attend=IntVar()
    lab3attend.set("")
    lab3attendEntry=Entry(frame_attendence,textvariable=lab3attend,width=15,font="Arial 10 bold",highlightbackground="black",highlightthickness=1)
    lab3attendEntry.place(x=380,y=500)

    addbutton=Button(sideframe,text="Add",font="Arial 10 bold",width=15,height=2,command=add)
    addbutton.place(x=70,y=70)

    updatebutton=Button(sideframe,text="Update",font="Arial 10 bold",width=15,height=2)
    updatebutton.place(x=70,y=120)

    deletebutton=Button(sideframe,text="Delete",font="Arial 10 bold",width=15,height=2)
    deletebutton.place(x=70,y=170)
    root.mainloop()
    
attendence()