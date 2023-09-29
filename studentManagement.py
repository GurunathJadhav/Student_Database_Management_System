from tkinter import *
from tkinter import ttk, filedialog
from PIL import ImageTk, Image
import tkinter.messagebox as msg
import mysql.connector
import datetime
import fitz
import os
import pandas as pd
def Restart():
    window=Tk()
    window.geometry("1366x750")
    # window.minsize(1366,750)
    # window.maxsize(1366,750)
    window.state("zoomed")
    window.title("Student Management System")
    icon = PhotoImage(
        file=r"C:\Users\User\Desktop\Student_Management\students_Logo.png")
    window.iconphoto(False, icon)
    
    def studentDetails(): 
        def access(username,password):
            global state0,state1,state2,state3
            if username=="mmec" and password=="mmec*":
                state0="active"
                state1="active"
                state2="active"
                state3="active"
                msg.showinfo("Login","Login Successfull For Staff")
            else:
                state0="active"
                state1="active"
                state2="disabled"
                state3="disabled"
                
            frame1=Frame(frame2,width=1366,height=768,bg="#E8E8E8")
            frame1.place(x=0,y=0)
            frame_internal=Frame(frame1,width=1220,height=630,bg="#E8E8E8")
            frame_internal.place(x=150,y=0)
            institutionLabel = Label(frame_internal, text="Institution Details       ", font=(
                "Times New Roman", 18, "bold"), bg="purple", fg="white",padx=110)
            institutionLabel.place(x=0, y=5)
            sideframe=Frame(frame1,width=250,height=768,bg="lightgray")
            sideframe.place(x=0,y=0)
            def getdata():
                from accessing import Access_student_attendence
                try:
                        data=Access_student_attendence(studentsusn.get().upper())
                        subject1.set(data[0][1])
                        subject1Entry.update()
                        subject1total.set(data[0][2])
                        subject1totalEntry.update()
                        subject1attend.set(data[0][3])
                        subject1attendEntry.update()
                        
                        subject2.set(data[0][4])
                        subject2Entry.update()
                        subject2total.set(data[0][5])
                        subject2totalEntry.update()
                        subject2attend.set(data[0][6])
                        subject2attendEntry.update()
                        
                        subject3.set(data[0][7])
                        subject3Entry.update()
                        subject3total.set(data[0][8])
                        subject3totalEntry.update()
                        subject3attend.set(data[0][9])
                        subject3attendEntry.update()
                        
                        subject4.set(data[0][10])
                        subject4Entry.update()
                        subject4total.set(data[0][11])
                        subject4totalEntry.update()
                        subject4attend.set(data[0][12])
                        subject4attendEntry.update()
                        
                        subject5.set(data[0][13])
                        subject5Entry.update()
                        subject5total.set(data[0][14])
                        subject5totalEntry.update()
                        subject5attend.set(data[0][15])
                        subject5attendEntry.update()
                        
                        subject6.set(data[0][16])
                        subject6Entry.update()
                        subject6total.set(data[0][17])
                        subject6totalEntry.update()
                        subject6attend.set(data[0][18])
                        subject6attendEntry.update()
                        
                        subject7.set(data[0][19])
                        subject7Entry.update()
                        subject7total.set(data[0][20])
                        subject7totalEntry.update()
                        subject7attend.set(data[0][21])
                        subject7attendEntry.update()
                        
                        subject8.set(data[0][22])
                        subject8Entry.update()
                        subject8total.set(data[0][23])
                        subject8totalEntry.update()
                        subject8attend.set(data[0][24])
                        subject8attendEntry.update()
                        
                        lab1.set(data[0][25])
                        lab1Entry.update()
                        lab1total.set(data[0][26])
                        lab1totalEntry.update()
                        lab1attend.set(data[0][27])
                        lab1attendEntry.upper()    
                except:""   
                try:
                    attenddata=Access_student_attendence(studentsusn.get().upper())
                    lab2.set(attenddata[0][28])
                    lab2Entry.update()
                    lab2total.set(attenddata[0][29])
                    lab2totalEntry.update()
                    lab2attend.set(attenddata[0][30])
                    lab2attendEntry.upper()
                    
                except:""
                try:
                    attenddata=Access_student_attendence(studentsusn.get().upper())
                    lab3.set(attenddata[0][31])
                    lab3Entry.update()
                    lab3total.set(attenddata[0][32])
                    lab3totalEntry.update()
                    lab3attend.set(attenddata[0][33])
                    lab3attendEntry.upper()
                    
                except:""
            def Attendence():
                try:
                    def previous():
                        frame_attendence.destroy()
                    global subject1,subject1Entry,subject1total,subject1totalEntry,subject1attend,subject1attendEntry ,subject2,subject2Entry,subject2total,subject2totalEntry,subject2attend,subject2attendEntry ,subject3,subject3Entry,subject3total,subject3totalEntry,subject3attend,subject3attendEntry ,subject4,subject4Entry,subject4total,subject4totalEntry,subject4attend,subject4attendEntry,subject5,subject5Entry,subject5total,subject5totalEntry,subject5attend,subject5attendEntry,subject6,subject6Entry,subject6total,subject6totalEntry,subject6attend,subject6attendEntry,subject7,subject7Entry,subject7total,subject7totalEntry,subject7attend,subject7attendEntry,subject8,subject8Entry,subject8total,subject8totalEntry,subject8attend,subject8attendEntry,lab1,lab1Entry,lab1total,lab1totalEntry,lab1attend,lab1attendEntry,lab2,lab2Entry,lab2total,lab2totalEntry,lab2attend,lab2attendEntry,lab3,lab3Entry,lab3total,lab3totalEntry,lab3attend,lab3attendEntry
                    
                    frame_attendence=Frame(frame1,width=1200,height=630,bg="#E8E8E8")
                    frame_attendence.place(x=250,y=0)
                    subjectslabel=Label(frame_attendence,text="Subjects",font="Arial 15 bold",bg="#E8E8E8")
                    subjectslabel.place(x=270,y=50)
                    totalclasslabel=Label(frame_attendence,text="Total Classes",font="Arial 15 bold",bg="#E8E8E8")
                    totalclasslabel.place(x=550,y=50)
                    attendedclasses=Label(frame_attendence,text="Attended Classes",font="Arial 15 bold",bg="#E8E8E8")
                    attendedclasses.place(x=750,y=50)
                    
                    subject1=StringVar()
                    subject1.set("")
                    subject1label=Label(frame_attendence,text="Subject 1",font="Arial 10 bold",bg="#E8E8E8")
                    subject1label.place(x=120,y=100)
                    subject1Entry=Entry(frame_attendence,textvariable=subject1,width=35,font="Arial 10 bold",highlightbackground="black",highlightthickness=1)
                    subject1Entry.place(x=200,y=100)
                    
                    subject1total=IntVar()
                    subject1total.set("")
                    subject1totalEntry=Entry(frame_attendence,textvariable=subject1total,width=15,font="Arial 10 bold",highlightbackground="black",highlightthickness=1)
                    subject1totalEntry.place(x=570,y=100)
                    
                    subject1attend=IntVar()
                    subject1attend.set("")
                    subject1attendEntry=Entry(frame_attendence,textvariable=subject1attend,width=15,font="Arial 10 bold",highlightbackground="black",highlightthickness=1)
                    subject1attendEntry.place(x=780,y=100)
                    
                    subject2=StringVar()
                    subject2.set("")
                    subject2label=Label(frame_attendence,text="Subject 2",font="Arial 10 bold",bg="#E8E8E8")
                    subject2label.place(x=120,y=140)
                    subject2Entry=Entry(frame_attendence,textvariable=subject2,width=35,font="Arial 10 bold",highlightbackground="black",highlightthickness=1)
                    subject2Entry.place(x=200,y=140)
                    
                    subject2total=IntVar()
                    subject2total.set("")
                    subject2totalEntry=Entry(frame_attendence,textvariable=subject2total,width=15,font="Arial 10 bold",highlightbackground="black",highlightthickness=1)
                    subject2totalEntry.place(x=570,y=140)
                    
                    subject2attend=IntVar()
                    subject2attend.set("")
                    subject2attendEntry=Entry(frame_attendence,textvariable=subject2attend,width=15,font="Arial 10 bold",highlightbackground="black",highlightthickness=1)
                    subject2attendEntry.place(x=780,y=140)
                    
                    subject3=StringVar()
                    subject3.set("")
                    subject3label=Label(frame_attendence,text="Subject 3",font="Arial 10 bold",bg="#E8E8E8")
                    subject3label.place(x=120,y=180)
                    subject3Entry=Entry(frame_attendence,textvariable=subject3,width=35,font="Arial 10 bold",highlightbackground="black",highlightthickness=1)
                    subject3Entry.place(x=200,y=180)
                    
                    subject3total=IntVar()
                    subject3total.set("")
                    subject3totalEntry=Entry(frame_attendence,textvariable=subject3total,width=15,font="Arial 10 bold",highlightbackground="black",highlightthickness=1)
                    subject3totalEntry.place(x=570,y=180)
                    
                    subject3attend=IntVar()
                    subject3attend.set("")
                    subject3attendEntry=Entry(frame_attendence,textvariable=subject3attend,width=15,font="Arial 10 bold",highlightbackground="black",highlightthickness=1)
                    subject3attendEntry.place(x=780,y=180)
                    
                    subject4=StringVar()
                    subject4.set("")
                    subject4label=Label(frame_attendence,text="Subject 4",font="Arial 10 bold",bg="#E8E8E8")
                    subject4label.place(x=120,y=220)
                    subject4Entry=Entry(frame_attendence,textvariable=subject4,width=35,font="Arial 10 bold",highlightbackground="black",highlightthickness=1)
                    subject4Entry.place(x=200,y=220)
                    
                    subject4total=IntVar()
                    subject4total.set("")
                    subject4totalEntry=Entry(frame_attendence,textvariable=subject4total,width=15,font="Arial 10 bold",highlightbackground="black",highlightthickness=1)
                    subject4totalEntry.place(x=570,y=220)
                    
                    subject4attend=IntVar()
                    subject4attend.set("")
                    subject4attendEntry=Entry(frame_attendence,textvariable=subject4attend,width=15,font="Arial 10 bold",highlightbackground="black",highlightthickness=1)
                    subject4attendEntry.place(x=780,y=220)
                    
                    subject5=StringVar()
                    subject5.set("")
                    subject5label=Label(frame_attendence,text="Subject 5",font="Arial 10 bold",bg="#E8E8E8")
                    subject5label.place(x=120,y=260)
                    subject5Entry=Entry(frame_attendence,textvariable=subject5,width=35,font="Arial 10 bold",highlightbackground="black",highlightthickness=1)
                    subject5Entry.place(x=200,y=260)
                    
                    subject5total=IntVar()
                    subject5total.set("")
                    subject5totalEntry=Entry(frame_attendence,textvariable=subject5total,width=15,font="Arial 10 bold",highlightbackground="black",highlightthickness=1)
                    subject5totalEntry.place(x=570,y=260)
                    
                    subject5attend=IntVar()
                    subject5attend.set("")
                    subject5attendEntry=Entry(frame_attendence,textvariable=subject5attend,width=15,font="Arial 10 bold",highlightbackground="black",highlightthickness=1)
                    subject5attendEntry.place(x=780,y=260)
                    
                    subject6=StringVar()
                    subject6.set("")
                    subject6label=Label(frame_attendence,text="Subject 6",font="Arial 10 bold",bg="#E8E8E8")
                    subject6label.place(x=120,y=300)
                    subject6Entry=Entry(frame_attendence,textvariable=subject6,width=35,font="Arial 10 bold",highlightbackground="black",highlightthickness=1)
                    subject6Entry.place(x=200,y=300)
                    
                    subject6total=IntVar()
                    subject6total.set("")
                    subject6totalEntry=Entry(frame_attendence,textvariable=subject6total,width=15,font="Arial 10 bold",highlightbackground="black",highlightthickness=1)
                    subject6totalEntry.place(x=570,y=300)
                    
                    subject6attend=IntVar()
                    subject6attend.set("")
                    subject6attendEntry=Entry(frame_attendence,textvariable=subject6attend,width=15,font="Arial 10 bold",highlightbackground="black",highlightthickness=1)
                    subject6attendEntry.place(x=780,y=300)
                    
                    subject7=StringVar()
                    subject7.set("")
                    subject7label=Label(frame_attendence,text="Subject 7",font="Arial 10 bold",bg="#E8E8E8")
                    subject7label.place(x=120,y=340)
                    subject7Entry=Entry(frame_attendence,textvariable=subject7,width=35,font="Arial 10 bold",highlightbackground="black",highlightthickness=1)
                    subject7Entry.place(x=200,y=340)
                    
                    subject7total=IntVar()
                    subject7total.set("")
                    subject7totalEntry=Entry(frame_attendence,textvariable=subject7total,width=15,font="Arial 10 bold",highlightbackground="black",highlightthickness=1)
                    subject7totalEntry.place(x=570,y=340)
                    
                    subject7attend=IntVar()
                    subject7attend.set("")
                    subject7attendEntry=Entry(frame_attendence,textvariable=subject7attend,width=15,font="Arial 10 bold",highlightbackground="black",highlightthickness=1)
                    subject7attendEntry.place(x=780,y=340)
                    
                    subject8=StringVar()
                    subject8.set("")
                    subject8label=Label(frame_attendence,text="Subject 8",font="Arial 10 bold",bg="#E8E8E8")
                    subject8label.place(x=120,y=380)
                    subject8Entry=Entry(frame_attendence,textvariable=subject8,width=35,font="Arial 10 bold",highlightbackground="black",highlightthickness=1)
                    subject8Entry.place(x=200,y=380)
                    
                    subject8total=IntVar()
                    subject8total.set("")
                    subject8totalEntry=Entry(frame_attendence,textvariable=subject8total,width=15,font="Arial 10 bold",highlightbackground="black",highlightthickness=1)
                    subject8totalEntry.place(x=570,y=380)
                    
                    subject8attend=IntVar()
                    subject8attend.set("")
                    subject8attendEntry=Entry(frame_attendence,textvariable=subject8attend,width=15,font="Arial 10 bold",highlightbackground="black",highlightthickness=1)
                    subject8attendEntry.place(x=780,y=380)
                    
                    lab1=StringVar()
                    lab1.set("")
                    lab1label=Label(frame_attendence,text="Lab 1",font="Arial 10 bold",bg="#E8E8E8")
                    lab1label.place(x=120,y=420)
                    lab1Entry=Entry(frame_attendence,textvariable=lab1,width=35,font="Arial 10 bold",highlightbackground="black",highlightthickness=1)
                    lab1Entry.place(x=200,y=420)
                    
                    lab1total=IntVar()
                    lab1total.set("")
                    lab1totalEntry=Entry(frame_attendence,textvariable=lab1total,width=15,font="Arial 10 bold",highlightbackground="black",highlightthickness=1)
                    lab1totalEntry.place(x=570,y=420)
                    
                    lab1attend=IntVar()
                    lab1attend.set("")
                    lab1attendEntry=Entry(frame_attendence,textvariable=lab1attend,width=15,font="Arial 10 bold",highlightbackground="black",highlightthickness=1)
                    lab1attendEntry.place(x=780,y=420)
                    
                    lab2=StringVar()
                    lab2.set("")
                    lab2label=Label(frame_attendence,text="Lab 2",font="Arial 10 bold",bg="#E8E8E8")
                    lab2label.place(x=120,y=460)
                    lab2Entry=Entry(frame_attendence,textvariable=lab2,width=35,font="Arial 10 bold",highlightbackground="black",highlightthickness=1)
                    lab2Entry.place(x=200,y=460)
                    
                    lab2total=IntVar()
                    lab2total.set("")
                    lab2totalEntry=Entry(frame_attendence,textvariable=lab2total,width=15,font="Arial 10 bold",highlightbackground="black",highlightthickness=1)
                    lab2totalEntry.place(x=570,y=460)
                    
                    lab2attend=IntVar()
                    lab2attend.set("")
                    lab2attendEntry=Entry(frame_attendence,textvariable=lab2attend,width=15,font="Arial 10 bold",highlightbackground="black",highlightthickness=1)
                    lab2attendEntry.place(x=780,y=460)
                    
                    lab3=StringVar()
                    lab3.set("")
                    lab3label=Label(frame_attendence,text="Lab 3",font="Arial 10 bold",bg="#E8E8E8")
                    lab3label.place(x=120,y=500)
                    lab3Entry=Entry(frame_attendence,textvariable=lab3,width=35,font="Arial 10 bold",highlightbackground="black",highlightthickness=1)
                    lab3Entry.place(x=200,y=500)
                    
                    lab3total=IntVar()
                    lab3total.set("")
                    lab3totalEntry=Entry(frame_attendence,textvariable=lab3total,width=15,font="Arial 10 bold",highlightbackground="black",highlightthickness=1)
                    lab3totalEntry.place(x=570,y=500)
                    
                    lab3attend=IntVar()
                    lab3attend.set("")
                    lab3attendEntry=Entry(frame_attendence,textvariable=lab3attend,width=15,font="Arial 10 bold",highlightbackground="black",highlightthickness=1)
                    lab3attendEntry.place(x=780,y=500)
                    
                    attendenceLabel=Label(frame_attendence,text="  Student Attendence                      ", font=(
                    "Times New Roman", 18, "bold"), bg="purple", fg="white")
                    attendenceLabel.place(x=0,y=5)
                    
                    previousButton=Button(frame_attendence,text="<---Previous--->",font="Arial 10 bold",relief=FLAT,bg="#E8E8E8",fg="blue",command=previous)
                    window.bind("<Left>",lambda event:previous())
                    previousButton.place(x=980,y=600)        
                except:
                    ""
            def getData():
                if len(studentsusn.get().upper())==10:
                    if username.upper()==studentsusn.get().upper():
                        try:
                            if username.upper()==studentsusn.get().upper():
                                studentsUsnEntry.config(state="disabled")
                                from images import get, convertbinarytopdf
                                usn1 = studentsusn.get().upper()
                                show = 'img.jpg'
                                if usn1 == "":
                                    msg.showinfo("Message", "Enter USN please")
                                else:
                                    data = get(studentsusn.get().upper())
                                    if (data[1] is not None):
                                        val = data[1]
                                        convertbinarytopdf(val, show)
                                        showimg(show)
                                    else:
                                        msg.showinfo("Message", "No Data available Please add photo")
                                from accessing import Access_institution_details,Access_personal_details,Access_student_attendence 
                                data = Access_institution_details(studentsusn.get().upper())
                                prsdata=Access_personal_details(studentsusn.get().upper())
                                Usn.set(data[0][0])
                                UsnEntry.update()
                                name.set(data[0][1])
                                nameEntry.update()
                                phone.set(data[0][2])
                                phoneEntry.update()
                                Branch.set(data[0][3])
                                BranchEntry.update()
                                DOB.set(data[0][4])
                                DOBEntry.update()
                                Sem.set(data[0][5])
                                SemEntry.update()
                                Quota.set(data[0][6])
                                QuotaEntry.update()
                                Gender.set(data[0][7])
                                GenderEntry.update()
                                Domicile.set(data[0][8])
                                DomicileEntry.update()
                                Physical1.set(data[0][9])
                                PhysicalEntry.update()
                                Medium1.set(data[0][10])
                                MediumEntry.update()
                                Schooler1.set(data[0][11])
                                SchoolerEntry.update()
                                AdmissionYear1.set(data[0][12])
                                AdmissionYearEntry.update()
                                
                                personalName.set(prsdata[0][1])
                                persNameEntry.update()
                                fatherName.set(prsdata[0][2])
                                FatherNamEntry.update() 
                                motherName.set(prsdata[0][3])
                                MotherNameEntry.update()
                                adharnumbar.set(prsdata[0][4])
                                AdharNumberEntry.update() 
                                Parentsphone.set(prsdata[0][5])
                                ParentphoneEntry.update()
                                Occupation.set(prsdata[0][6])
                                OccupationEntry.update()
                                category.set(prsdata[0][7])
                                CatagoryEntry.update()
                                Religion.set(prsdata[0][8])
                                ReligionEntry.update()
                                Caste1.set(prsdata[0][9])
                                CasteEntry.update()
                                Nationality1.set(prsdata[0][10])
                                NationalityEntry.update()
                                Annual_Income1.set(prsdata[0][11])
                                Annual_IncomeEntry.update()
                                village1.set(prsdata[0][12])
                                villageEntry.update()
                                Taluka1.set(prsdata[0][13])
                                TalukaEntry.update()
                                State1.set(prsdata[0][14])
                                StateEntry.update()
                                Address1.set(prsdata[0][15])
                                AddressEntry.update()
                                Email.set(prsdata[0][16])
                                EmailEntry.update()
                                getdata()
                            else:
                                msg.showwarning(
                            "Warning", "You Can Not Access Others Information !")
                        except:
                            ""
                    elif username=="mmec":
                        from images import get, convertbinarytopdf
                        usn1 = studentsusn.get().upper()
                        show = 'img.jpj'
                        if usn1 == "":
                            msg.showinfo("Message", "Enter USN please")
                        else:
                            data = get(studentsusn.get().upper())
                            # print(data)
                            if (data[1] is not None):
                                val = data[1]
                                convertbinarytopdf(val, show)
                                showimg(show)
                            else:
                                msg.showinfo("Message", "No Data available Please add photo")
                        getdata()
                        try:
                            from accessing import Access_institution_details,Access_personal_details
                            data = Access_institution_details(studentsusn.get().upper())
                            prsdata=Access_personal_details(studentsusn.get().upper())
                            if data[0][0]==studentsusn.get().upper():
                                studentsUsnEntry.config(state="normal")
                            Usn.set(data[0][0])
                            UsnEntry.update()
                            name.set(data[0][1])
                            nameEntry.update()
                            phone.set(data[0][2])
                            phoneEntry.update()
                            Branch.set(data[0][3])
                            BranchEntry.update()
                            DOB.set(data[0][4])
                            DOBEntry.update()
                            Sem.set(data[0][5])
                            SemEntry.update()
                            Quota.set(data[0][6])
                            QuotaEntry.update()
                            Gender.set(data[0][7])
                            GenderEntry.update()
                            Domicile.set(data[0][8])
                            DomicileEntry.update()
                            Physical1.set(data[0][9])
                            PhysicalEntry.update()
                            Medium1.set(data[0][10])
                            MediumEntry.update()
                            Schooler1.set(data[0][11])
                            SchoolerEntry.update()
                            AdmissionYear1.set(data[0][12])
                            AdmissionYearEntry.update()
                            
                            personalName.set(prsdata[0][1])
                            persNameEntry.update()
                            fatherName.set(prsdata[0][2])
                            FatherNamEntry.update() 
                            motherName.set(prsdata[0][3])
                            MotherNameEntry.update()
                            adharnumbar.set(prsdata[0][4])
                            AdharNumberEntry.update() 
                            Parentsphone.set(prsdata[0][5])
                            ParentphoneEntry.update()
                            Occupation.set(prsdata[0][6])
                            OccupationEntry.update()
                            category.set(prsdata[0][7])
                            CatagoryEntry.update()
                            Religion.set(prsdata[0][8])
                            ReligionEntry.update()
                            Caste1.set(prsdata[0][9])
                            CasteEntry.update()
                            Nationality1.set(prsdata[0][10])
                            NationalityEntry.update()
                            Annual_Income1.set(prsdata[0][11])
                            Annual_IncomeEntry.update()
                            village1.set(prsdata[0][12])
                            villageEntry.update()
                            Taluka1.set(prsdata[0][13])
                            TalukaEntry.update()
                            State1.set(prsdata[0][14])
                            StateEntry.update()
                            Address1.set(prsdata[0][15])
                            AddressEntry.update()
                            Email.set(prsdata[0][16])
                            EmailEntry.update()
                        except:
                            msg.showwarning(
                                "Warning", "Your Infomation Is Not Added Yet,Please add your details.If Information Is Alrady Added Please Restart The Application To Access It")
                else:
                    msg.showerror("Error","Enter Correct USN Number")
            def clear():
                studentsusn.set("")
                studentsUsnEntry.update()
                Usn.set("")
                UsnEntry.update()
                name.set("")
                nameEntry.update()
                phone.set("")
                phoneEntry.update()
                Branch.set("")
                BranchEntry.update()
                DOB.set("")
                DOBEntry.update()
                Sem.set("")
                SemEntry.update()
                Quota.set("")
                QuotaEntry.update()
                Gender.set("")
                GenderEntry.update()
                Domicile.set("")
                DomicileEntry.update()
                Physical1.set("")
                PhysicalEntry.update()
                Medium1.set("")
                MediumEntry.update()
                Schooler1.set("")
                SchoolerEntry.update()
                AdmissionYear1.set("")
                AdmissionYearEntry.update()
                
                personalName.set("")
                persNameEntry.update()
                fatherName.set("")
                FatherNamEntry.update()
                motherName.set("")
                MotherNameEntry.update()
                adharnumbar.set("")
                AdharNumberEntry.update()
                Parentsphone.set("")
                ParentphoneEntry.update()
                Occupation.set("")
                OccupationEntry.update()
                category.set("")
                CatagoryEntry.update()
                Religion.set("")
                ReligionEntry.update()
                Caste1.set("")
                CasteEntry.update()
                Nationality1.set("")
                NationalityEntry.update()
                Annual_Income1.set("")
                Annual_IncomeEntry.update()
                village1.set("")
                villageEntry.update()
                Taluka1.set("")
                TalukaEntry.update()
                State1.set("")
                StateEntry.update()
                Address1.set("")
                AddressEntry.update()
                Email.set("")
                EmailEntry.update()
                studentsUsnEntry.config(state="normal")
            def addData():
                global USN1 ,sem
                USN1="0"
                sem=0
                try:
                    from accessing import Access_institution_details,Access_personal_details
                    data = Access_institution_details(studentsusn.get().upper())
                    USN1=data[0][0]
                    sem=data[0][5]
                except:
                    ""
                if studentsusn.get().upper()==USN1 and Sem.get()==sem:
                    msg.showinfo("Information","Your Information Is Already Exist..")
                else:
                    if phone.get().isnumeric():
                        if len(phone.get()) ==10 :
                            if Parentsphone.get().isnumeric():
                                if len(Parentsphone.get()) ==10 :
                                    if adharnumbar.get().isnumeric():
                                        if len(adharnumbar.get()) ==12:
                                            if studentsusn.get().upper()!="      Student USN":
                                                from inserting_values import Insert_institution_details
                                                Insert_institution_details(studentsusn.get().upper(), name.get().upper(
                                                ), phone.get(), Branch.get(), DOB.get(), Sem.get(), Quota.get(),Gender.get().upper(),Domicile.get(),Physical1.get(),Medium1.get(),Schooler1.get(),AdmissionYear1.get())
                                                from inserting_values import Insert_personal_details
                                                Insert_personal_details(studentsusn.get().upper(),personalName.get().upper(),fatherName.get().upper(),motherName.get().upper(),adharnumbar.get(),Parentsphone.get(),Occupation.get().upper(),category.get(),Religion.get(),Caste1.get(),Nationality1.get(),Annual_Income1.get(),village1.get(),Taluka1.get(),State1.get(),Address1.get(),Email.get())
                                                msg.showinfo("Message", "Your Infomation Is Saved Successfully...")
                                                clear()
                                            else:
                                                msg.showwarning("Warning","Fill All The Details")
                                        else:
                                            msg.showwarning("Warning","Enter 12 digit Adhar number")
                                            adharnumbar.set("")
                                            AdharNumberEntry.update()
                                    else:
                                        msg.showwarning("Warning","Enter Valid Adhar number")
                                        adharnumbar.set("")
                                        AdharNumberEntry.update()
                                else:
                                    msg.showwarning("Warning","Enter 10 digit Parent's number")
                                    Parentsphone.set("")
                                    ParentphoneEntry.update()
                            else:
                                msg.showwarning("Warning","Enter correct  Parent's number")
                                Parentsphone.set("")
                                ParentphoneEntry.update()
                        else:
                            msg.showwarning("Warning","Enter 10 digit phone number")
                            phone.set("")
                            phoneEntry.update()
                    else:
                        msg.showwarning("Warning","Enter correct phone number")
                        phone.set("")
                        phoneEntry.update()
            # window.bind(",",lambda e:clear())
            def Update():
                studentdb = mysql.connector.connect( host='localhost', user='root', password='guru8296jadhav@', database="student_information")
                cur = studentdb.cursor(buffered=True)
                s=f" UPDATE `student_information`.`institution_details` SET sem='{Sem.get()}' WHERE USN='{studentsusn.get().upper()}'"
                cur.execute(s)
                studentdb.commit()
                
                s=f" UPDATE `student_information`.`institution_details` SET phone='{phone.get()}' WHERE USN='{studentsusn.get().upper()}'"
                cur.execute(s)
                studentdb.commit()
                
                s=f" UPDATE `student_information`.`institution_details` SET dob='{DOB.get()}' WHERE USN='{studentsusn.get().upper()}'"
                cur.execute(s)
                studentdb.commit()
                
                s=f" UPDATE `student_information`.`institution_details` SET admission_year='{AdmissionYear1.get()}' WHERE USN='{studentsusn.get().upper()}'"
                cur.execute(s)
                studentdb.commit()
                
                s=f" UPDATE `student_information`.`institution_details` SET medium='{Medium1.get()}' WHERE USN='{studentsusn.get().upper()}'"
                cur.execute(s)
                studentdb.commit()
                
                s=f" UPDATE `student_information`.`personal_details` SET parentsphone='{Parentsphone.get()}' WHERE USN='{studentsusn.get().upper()}'"
                cur.execute(s)
                studentdb.commit()
            
                cur.execute(f" UPDATE `student_information`.`personal_details` SET annualincome='{Annual_Income1.get()}' WHERE USN='{studentsusn.get().upper()}'")
                studentdb.commit()
                
                s=f" UPDATE `student_information`.`personal_details` SET address='{Address1.get()}' WHERE USN='{studentsusn.get().upper()}'"
                cur.execute(s)
                studentdb.commit()
                
                s=f" UPDATE `student_information`.`personal_details` SET Email='{Email.get()}' WHERE USN='{studentsusn.get().upper()}'"
                cur.execute(s)
                studentdb.commit()
                msg.showinfo("Updation","Information Is Updated Successfully")
            def Delete():
                data=mysql.connector.connect(host='localhost',user="root",password="guru8296jadhav@",database="student_information")
                cur=data.cursor(buffered=True)
                s=f" DELETE FROM student_information.institution_details WHERE USN='{studentsusn.get().upper()}'"
                cur.execute(s)
                data.commit()
            
                s=f" DELETE FROM  student_information.personal_details WHERE USN='{studentsusn.get().upper()}'"
                cur.execute(s)
                data.commit()
                msg.showinfo("Delete","Information Removed Successfully")
            try:
                if username=="mmec":
                    greet=Label(frame_internal,text=f"Welcom ,Respected Staff",bg="#E8E8E8",font="Arial 10 bold",fg="blue")
                    greet.place(x=900,y=3) 
                else:
                    from accessing import Access_institution_details
                    data1=Access_institution_details(username)
                    greet=Label(frame_internal,text=f"Welcom ,{data1[0][1]}",bg="#E8E8E8",font="Arial 10 bold",fg="blue")
                    greet.place(x=870,y=3)  
            except:""
            def enter(e):
                studentsUsnEntry.delete(0, "end")
            def leave(e):
                if studentsUsnEntry.get() == "":
                    studentsUsnEntry.insert(0, "       Student USN")
            def enterfordob(e):
                DOBEntry.delete(0, "end")
            def leavefordob(e):
                if DOBEntry.get() == "":
                    DOBEntry.insert(0, "      DD/MM/YYYY")
            def addimg():
                usn=studentsusn.get().upper()
                from images import insertimg, get, updateimg
                filename = filedialog.askopenfilename(initialdir="/Desktop", title="Select a File",
                                                    filetypes=(("JPG Files", "*.jpg"),
                                                                ("JPEG Files", "*.jpeg"), ("ALL Files", "*.*")))
                data = get(usn)
                if data is None:
                    insertimg(filename, usn)
                    msg.showinfo("Message", "Uploaded successfully")
                elif data is not None:
                    if data[0] == studentsusn.get().upper():
                        updateimg(filename, usn)
                        msg.showinfo("Message", "Updated successfully")
                    else:
                        insertimg(filename, usn)
                        msg.showinfo("Message", "Uploaded successfully")
                else:
                    pass
            def showimg(filename):
                img = Image.open(filename)
                global new_image
                try:
                    resized_image = img.resize((180, 200), Image.LANCZOS)
                except:""
                new_image = ImageTk.PhotoImage(resized_image)
                canvas.create_image(0, 0, anchor=NW, image=new_image) 
            studentsusn = StringVar()
            studentsusn.set("")
            studentsUsnEntry = Entry(sideframe, textvariable=studentsusn, font=(
                "Arial 15 bold"), highlightbackground="black", highlightthickness=1)
            studentsUsnEntry.insert(0, "      Student USN")
            studentsUsnEntry.bind("<FocusIn>", enter)
            studentsUsnEntry.bind("<FocusOut>", leave)
            studentsUsnEntry.place(x=10, y=25)
            
            name = StringVar()
            name.set("")
            namevar = Label(frame_internal, text="Student Name",
                            font=("Arial 11 bold"),bg="#E8E8E8")
            namevar.place(x=120, y=70)
            nameEntry = Entry(frame_internal, width=30, textvariable=name, font=(
                "Arial 10 bold"), highlightbackground="black", highlightthickness=1)
            nameEntry.place(x=235, y=70)
            
            Usn = StringVar()
            Usn.set("")
            Usnvar = Label(frame_internal,text="Student USN",
                            font=("Arial 11 bold"), bg="#E8E8E8")
            Usnvar.place(x=460, y=70)
            UsnEntry = Entry(frame_internal, width=30, textvariable=Usn, font=(
                "Arial 10 bold"), highlightbackground="black", highlightthickness=1)
            UsnEntry.place(x=580, y=70)

            phone = StringVar()
            phone.set("")
            phonevar = Label(frame_internal, text="Phone Number",
                                font=("Arial 11 bold"), bg="#E8E8E8")
            phonevar.place(x=810, y=70)
            phoneEntry = Entry(frame_internal, width=30, textvariable=phone, font=(
                "Arial 10 bold"), highlightbackground="black", highlightthickness=1)
            phoneEntry.place(x=940, y=70)
            
            Branch = StringVar()
            Branch.set("")
            Branchvar = Label(frame_internal, text="Branch",
                            font=("Arial 11 bold"), bg="#E8E8E8")
            Branchvar.place(x=140, y=110)
            Branches=["Computer Science","Electronics and Communication","Robotics","Mechanical"]
            BranchEntry =ttk.Combobox(frame_internal,values=Branches,textvariable=Branch,width=28,font=("Arial 10 bold"))
            BranchEntry.place(x=235, y=110)
            
            DOB = StringVar()
            DOB.set("")
            DOBvar = Label(frame_internal, text="Date Of Birth",
                            font=("Arial 11 bold"), bg="#E8E8E8")
            DOBvar.place(x=460, y=110)
            DOBEntry = Entry(frame_internal, width=29, textvariable=DOB, font=(
                "Arial 10 bold"), highlightbackground="black", highlightthickness=1)
            DOBEntry.insert(0, "              DD/MM/YYYY")
            DOBEntry.bind("<FocusIn>", enterfordob)
            DOBEntry.bind("<FocusOut>", leavefordob)
            DOBEntry.place(x=580, y=110)
            
            Sem = IntVar()
            Sem.set(0)
            Semvar = Label(frame_internal, text="Semester",
                        font=("Arial 11 bold"), bg="#E8E8E8")
            Semvar.place(x=830, y=110)
            sem=[1,2,3,4,5,6,7,8]
            SemEntry = ttk.Combobox(frame_internal, width=28, values=sem,textvariable=Sem, font=(
                "Arial 10 bold"))
            SemEntry.place(x=940, y=110)
            
            Quota = StringVar()
            Quota.set("")
            Quotavar = Label(frame_internal, text="Admission Quota",
                        font=("Arial 11 bold"), bg="#E8E8E8")
            quota=["Management","CET","SNQ"]
            Quotavar.place(x=105, y=150)
            QuotaEntry = ttk.Combobox(frame_internal, width=28,values=quota ,textvariable=Quota, font=(
                "Arial 10 bold"))
            QuotaEntry.place(x=235, y=150)
            
            Gender = StringVar()
            Gender.set("")
            Gendervar = Label(frame_internal, text="Gender",
                        font=("Arial 11 bold"), bg="#E8E8E8")
            gender=["MALE","FEMALE","OTHER"]
            Gendervar.place(x=480, y=150)
            GenderEntry = ttk.Combobox(frame_internal, width=28,values=gender ,textvariable=Gender, font=(
                "Arial 10 bold"))
            GenderEntry.place(x=580, y=150)
            
            Domicile = StringVar()
            Domicile.set("")
            Domicilevar = Label(frame_internal, text="Domicile",
                        font=("Arial 11 bold"), bg="#E8E8E8")
            State=["Karnataka","Non Karnataka"]
            Domicilevar.place(x=830, y=150)
            DomicileEntry = ttk.Combobox(frame_internal, width=28,values=State ,textvariable=Domicile, font=(
                "Arial 10 bold"))
            DomicileEntry.place(x=940, y=150)
            
            Physical1 = StringVar()
            Physical1.set("")
            Physical = Label(frame_internal, text='''  Whether Physically
            Handicapped''',
                            font=("Arial 11 bold"), bg="#E8E8E8")
            Physical.place(x=105, y=192)
            value=["Yes","No"]
            PhysicalEntry = ttk.Combobox(frame_internal, width=10, values=value,textvariable=Physical1, font=(
                "Arial 10 bold"))
            PhysicalEntry.place(x=265, y=192)
            
            Medium1 = StringVar()
            Medium1.set("")
            Medium = Label(frame_internal, text='''       Medium of 
            Education''',
                            font=("Arial 11 bold"), bg="#E8E8E8")
            Medium.place(x=400, y=192)
            value=["Hindi","Marathi","English","Kannada"]
            MediumEntry = ttk.Combobox(frame_internal, width=10, values=value,textvariable=Medium1, font=(
                "Arial 10 bold "))
            MediumEntry.place(x=520, y=192)
            
            Schooler1 = StringVar()
            Schooler1.set("")
            Schooler = Label(frame_internal, text='''   Hosteller/
            Dayschooler''',
                            font=("Arial 11 bold"), bg="#E8E8E8")
            Schooler.place(x=620, y=192)
            value=["Hosteller","Dayschooler"]
            SchoolerEntry = ttk.Combobox(frame_internal, width=12, values=value,textvariable=Schooler1, font=(
                "Arial 10 bold"))
            SchoolerEntry.place(x=750, y=192)
            
            AdmissionYear1 = IntVar()
            AdmissionYear1.set("")
            AdmissionYear = Label(frame_internal, text='''   Year of 
            Admission''',
                            font=("Arial 11 bold"), bg="#E8E8E8")
            AdmissionYear.place(x=860, y=192)
            value=[2029,2028,2027,2026,2025,2024,2023,2022,2021,2020,2019,2018,2017,2016,2015,2014,2013,2012,2011,2010]
            AdmissionYearEntry = ttk.Combobox(frame_internal, width=10, values=value,textvariable=AdmissionYear1, font=(
                "Arial 10 bold"))
            AdmissionYearEntry.place(x=970, y=192)
            
            personalLabel = Label(frame_internal, text="Personal Details          ", font=(
                "Times New Roman", 18, "bold"), bg="purple", fg="white",padx=100)
            personalLabel.place(x=15, y=250)
            
            personalName = StringVar()
            personalName.set("")
            persName = Label(frame_internal, text="Personal Name",
                            font=("Arial 11 bold"), bg="#E8E8E8")
            persName.place(x=110, y=300)
            persNameEntry = Entry(frame_internal, width=28, textvariable=personalName, font=(
                "Arial 10 bold"), highlightbackground="black", highlightthickness=1)
            persNameEntry.place(x=240, y=300)
            
            fatherName = StringVar()
            fatherName.set("")
            FatherName = Label(frame_internal, text="Father Name",
                            font=("Arial 11 bold"), bg="#E8E8E8")
            FatherName.place(x=460, y=300)
            FatherNamEntry = Entry(frame_internal, width=28, textvariable=fatherName, font=(
                "Arial 10 bold"), highlightbackground="black", highlightthickness=1)
            FatherNamEntry.place(x=580, y=300)
            
            motherName = StringVar()
            motherName.set("")
            MotherName = Label(frame_internal, text="Mother Name",
                            font=("Arial 11 bold"), bg="#E8E8E8")
            MotherName.place(x=810, y=300)
            MotherNameEntry = Entry(frame_internal, width=30, textvariable=motherName, font=(
                "Arial 10 bold"), highlightbackground="black", highlightthickness=1)
            MotherNameEntry.place(x=940, y=300)
            
            adharnumbar = StringVar()
            adharnumbar.set("")
            AdharNumber = Label(frame_internal, text="Addhar Number",
                                font=("Arial 11 bold"), bg="#E8E8E8")
            AdharNumber.place(x=110, y=340)
            AdharNumberEntry = Entry(frame_internal, width=28, textvariable=adharnumbar, font=(
                "Arial 10 bold"), highlightbackground="black", highlightthickness=1)
            AdharNumberEntry.place(x=240, y=340)
            
            Parentsphone = StringVar()
            Parentsphone.set("")
            Parentphonevar = Label(frame_internal, text="Parent's Phone",
                                font=("Arial 11 bold"), bg="#E8E8E8")
            Parentphonevar.place(x=460, y=340)
            ParentphoneEntry = Entry(frame_internal, width=28, textvariable=Parentsphone, font=(
                "Arial 10 bold"), highlightbackground="black", highlightthickness=1)
            ParentphoneEntry.place(x=580, y=340)
            
            Occupation = StringVar()
            Occupation.set("")
            Occupationvar = Label(frame_internal, text='''   Occupation of 
            Father/Mother''',
                                font=("Arial 11 bold"), bg="#E8E8E8")
            Occupationvar.place(x=800, y=330)
            OccupationEntry = Entry(frame_internal, width=28, textvariable=Occupation, font=(
                "Arial 10 bold"), highlightbackground="black", highlightthickness=1)
            OccupationEntry.place(x=960, y=340)
            
            category = StringVar()
            category.set("")
            Catagory = Label(frame_internal, text="Category",
                            font=("Arial 11 bold"), bg="#E8E8E8")
            Catagory.place(x=150, y=380)
            cate=["GM","SC","ST","Cat-I","2A","2B","3A","3B"]
            CatagoryEntry = ttk.Combobox(frame_internal, width=10,values=cate, textvariable=category, font=(
                "Arial 10 bold"))
            CatagoryEntry.place(x=240, y=380)
            
            Religion = StringVar()
            Religion.set("")
            Religionl = Label(frame_internal, text="Religion",
                            font=("Arial 11 bold"), bg="#E8E8E8")
            Religionl.place(x=350, y=380)
            reli=["Hindu","Jain"]
            ReligionEntry = ttk.Combobox(frame_internal, width=10,values=reli, textvariable=Religion, font=(
                "Arial 10 bold"))
            ReligionEntry.place(x=430, y=380)
            
            Caste1 = StringVar()
            Caste1.set("")
            Caste = Label(frame_internal, text="Caste",
                            font=("Arial 11 bold"), bg="#E8E8E8")
            Caste.place(x=530, y=380)
            caste=["Maratha"]
            CasteEntry = ttk.Combobox(frame_internal, width=10,values=caste, textvariable=Caste1, font=(
                "Arial 10 bold"))
            CasteEntry.place(x=600, y=380)
            
            Nationality1= StringVar()
            Nationality1.set("")
            Nationality = Label(frame_internal, text="Nationality",
                            font=("Arial 11 bold"), bg="#E8E8E8")
            Nationality.place(x=710, y=380)
            nations=["Indian","NRI"]
            NationalityEntry = ttk.Combobox(frame_internal, width=10,values=nations, textvariable=Nationality1, font=(
                "Arial 10 bold"))
            NationalityEntry.place(x=810, y=380)
            
            Annual_Income1 = IntVar()
            Annual_Income1.set("")
            Annual_Income = Label(frame_internal, text="Annual Income",
                            font=("Arial 11 bold"), bg="#E8E8E8")
            Annual_Income.place(x=920, y=380)
            income=[100000,200000,500000,1000000]
            Annual_IncomeEntry = ttk.Combobox(frame_internal, width=10,values=income
                                            , textvariable=Annual_Income1, font=(
                "Arial 10 bold"))
            Annual_IncomeEntry.place(x=1050, y=380)
            
            village1 = StringVar()
            village1.set("")
            village = Label(frame_internal, text="Village/Town",
                            font=("Arial 11 bold"), bg="#E8E8E8")
            village.place(x=110, y=420)
            villageEntry = Entry(frame_internal, width=28, textvariable=village1, font=(
                "Arial 10 bold"), highlightbackground="black", highlightthickness=1)
            villageEntry.place(x=240, y=420)
            
            Taluka1 = StringVar()
            Taluka1.set("")
            Taluka = Label(frame_internal, text="Taluka",
                            font=("Arial 11 bold"), bg="#E8E8E8")
            Taluka.place(x=490, y=420)
            TalukaEntry = Entry(frame_internal, width=28, textvariable=Taluka1, font=(
                "Arial 10 bold"), highlightbackground="black", highlightthickness=1)
            TalukaEntry.place(x=580, y=420)
            
            State1 = StringVar()
            State1.set("")
            State = Label(frame_internal, text="State",
                            font=("Arial 11 bold"), bg="#E8E8E8")
            State.place(x=860, y=420)
            StateEntry = Entry(frame_internal, width=28, textvariable=State1, font=(
                "Arial 10 bold"), highlightbackground="black", highlightthickness=1)
            StateEntry.place(x=940, y=420)
            
            Address1 = StringVar()
            Address1.set("")
            Address = Label(frame_internal, text="Address",
                            font=("Arial 11 bold"), bg="#E8E8E8")
            Address.place(x=130, y=460)
            AddressEntry = Entry(frame_internal, width=70, textvariable=Address1, font=(
                "Arial 10 bold"), highlightbackground="black", highlightthickness=1)
            AddressEntry.place(x=240, y=460)
            
            Email = StringVar()
            Email.set("")
            Emaillabel = Label(frame_internal, text="Email",
                            font=("Arial 11 bold"), bg="#E8E8E8")
            Emaillabel.place(x=750, y=460)
            EmailEntry = Entry(frame_internal, width=30, textvariable=Email, font=(
                "Arial 12 "), highlightbackground="black", highlightthickness=1)
            EmailEntry.place(x=800, y=460)
            global addbutton,updatebutton,deletebutton,k,getbutton
            k=0
            def Down(e):
                global k
                k+=1
                if k==1:
                    getData1.focus_set()
                    window.bind("<Return>",lambda event:getData())
                elif k==2:
                    AddData.focus_set()
                    window.bind("<Return>",lambda event:addData())
                elif k==3:
                    Updatedata.focus_set()
                    window.bind("<Return>",lambda event:Update())
                elif k==4:
                    deletedata.focus_set()
                    window.bind("<Return>",lambda event:Delete())
                    k-=4
            window.bind("<Down>",Down)
            getData1=Button(sideframe,text="Get Data",command=getData,padx=15,pady=5,width=15,relief=RAISED,font=("Arial 10 bold"))
            getData1.config(state=state0)
            getData1.place(x=48,y=270)
            AddData=Button(sideframe,text="Add Data",command=addData,padx=15,pady=5,width=15,relief=RAISED,font=("Arial 10 bold"))
            AddData.config(state=state1)
            AddData.place(x=48,y=310)
            
            Updatedata=Button(sideframe,text="Update",command=Update,padx=15,pady=5,width=15,relief=RAISED,font=("Arial 10 bold"))
            Updatedata.config(state=state2)
            Updatedata.place(x=48,y=350)
            
            deletedata=Button(sideframe,text="Delete",command=Delete,padx=15,pady=5,width=15,relief=RAISED,font=("Arial 10 bold"))
            deletedata.config(state=state3)
            deletedata.place(x=48,y=390)
            
            Next=Button(frame_internal,text="<---Next--->",font="Arial 10 bold",relief=FLAT,command=Attendence,bg="#E8E8E8",fg="blue")
            window.bind("<Right>",lambda event:Attendence())
            Next.place(x=1080,y=600)
            canvas = Canvas(sideframe, width=170, height=180, bg="lightgray")
            canvas.place(x=40, y=70)
            Addimg = Button(sideframe, text="Add Photo", command=addimg, padx=15, pady=5, width=15, relief=RAISED,
                            font=("Arial 10 bold"))
            Addimg.config(state="active")
            Addimg.place(x=48, y=430)
            date=datetime.date.today()
            datestr=str(date)
            Datestr=datestr.split("-")
            dates=Datestr[: : -1]
            d="-".join(dates)
# ===========================================Staff/Student Login/Registration==========================================================================================
            bottomframe = Frame(frame1,width=1380,height=25,bg="lightgray")
            bottomframe.place(x=0, y=630)
            bottomLabel = Label(frame1, text="Note: User Can Either Add or Fetch The Data ", font=(
                "Times New Roman", 8, "bold"), fg="black",bg="lightgray")
            bottomLabel.place(x=5,y=630)
            day=datetime.datetime.now().strftime("%A")
            dayLabel=Label(bottomframe,text=f'{day},',font=(
                "Times New Roman", 10, "bold"),bg="lightgray")
            dayLabel.place(x=1180,y=0)
            dateLabel=Label(bottomframe,text=d,font=(
                "Times New Roman", 10, "bold"),bg="lightgray")
            dateLabel.place(x=1250,y=0)
        frame=Frame(frame2,width=800,height=350,bg="#E8E8E8",highlightbackground="skyblue",highlightthickness=3)
        frame.place(x=250,y=230)
        label=Label(frame,text=" Staff Login",font=("Arial 17 bold"),bg="cyan",padx=100,relief=RAISED)
        label.place(x=35,y=50)
        bottomlabel=Label(frame,text="Staff/Student Can Login By Using Their Username And Password",font=("Arial 8 bold"),bg="#E8E8E8",fg="red")
        bottomlabel.place(x=0,y=325)
        def login():
            try:
                if username.get()=="mmec" and password.get()=="mmec*":
                    access(username.get(),password.get())
                    frame.destroy()
                else:
                    msg.showwarning("Warning","You Have Not Register Yet..")
            except:""
        def studentlogin():
            from accessing import Access_user_password
            userdetails=Access_user_password(studentusername.get().upper())
            try:
                if studentusername.get().upper()==userdetails[0][0] and studentpassword.get()==userdetails[0][1]:
                    msg.showinfo("Login","Login Successfull For Student")
                    access(studentusername.get(),studentpassword.get())
                    frame.destroy()
                else:
                    msg.showwarning("Warning","You Have Not Register Yet..")
                
            except:""
        def add():
            def Registerdetails():
                global username1
                username1=""
                try:
                    from accessing import Access_user_password
                    userdetails=Access_user_password(user.get().upper())
                    username1=userdetails[0][0]
                except:
                    ""
                if user.get()=="      Username" and userpass.get()=="      Password":
                    msg.showwarning("Warning","Please Fill Details")
                elif user.get().upper()==username1:
                    msg.showinfo("Registration","Already Registered")
                else:
                    from inserting_values import Insert_user_passoword
                    Insert_user_passoword(user.get().upper(),userpass.get())
                    msg.showinfo("Registration","Registration Successfully")
                    frame_login.destroy()
            def enter(e):
                userEntry.delete(0, "end")
            def leave(e):
                if userEntry.get() == "":
                    userEntry.insert(0, "       Username")
            frame_login=Frame(frame2,width=400,height=300,bg="#E8E8E8",highlightbackground="skyblue",highlightthickness=2)
            frame_login.place(x=500,y=230)
            label=Label(frame_login,text="New Student Registration",font=("Arial 15 bold"),bg="#E8E8E8")
            label.place(x=80,y=25)
            user=StringVar()
            user.set("")
            userEntry=Entry(frame_login,textvariable=user,width=30,font=("Arial 12 bold"),highlightbackground="skyblue",highlightthickness=2)
            userEntry.insert(0, "      Username")
            userEntry.bind("<FocusIn>", enter)
            userEntry.bind("<FocusOut>", leave)
            userEntry.place(x=70,y=100)
            def Cancle():
                frame_login.destroy()
            def enter(e):
                userpassEntry.delete(0, "end")
            def leave(e):
                if userpassEntry.get() == "":
                    userpassEntry.insert(0, "       Password")
            userpass=StringVar()
            userpass.set("")
            userpassEntry=Entry(frame_login,textvariable=userpass,width=30,font=("Arial 12 bold"),highlightbackground="skyblue",highlightthickness=2)
            userpassEntry.insert(0, "      Password")
            userpassEntry.bind("<FocusIn>", enter)
            userpassEntry.bind("<FocusOut>", leave)
            userpassEntry.place(x=70,y=150)
            
            register_button=Button(frame_login,text="Register",font=("Arial 10 bold"),command=Registerdetails,padx=25)
            window.bind("<Return>",lambda event:Registerdetails())
            register_button.place(x=155,y=200)
            cancleButton1=Button(frame_login,text="X",bg="red",fg="white",padx=10,command=Cancle)
            cancleButton1.place(x=360,y=0)
            frame.destroy()
        def enter1(e):
                usernameEntry.delete(0, "end")
        def leave1(e):
                if usernameEntry.get() == "":
                    usernameEntry.insert(0, "       Username")
        username=StringVar()
        username.set("")
        usernameEntry=Entry(frame,textvariable=username,width=20,font=("Arial 15 bold"),highlightbackground="skyblue",highlightthickness=2)
        usernameEntry.insert(0, "      Username")
        usernameEntry.bind("<FocusIn>", enter1)
        usernameEntry.bind("<FocusOut>", leave1)
        usernameEntry.place(x=80,y=100)
        def enter2(e):
                passwordEntry.delete(0, "end")
        def leave2(e):
                if passwordEntry.get() == "":
                    passwordEntry.insert(0, "       Password")
        def cancle():
            frame.destroy()
        password=StringVar()
        password.set("")
        passwordEntry=Entry(frame,textvariable=password,width=20,font=("Arial 15 bold"),highlightbackground="skyblue",highlightthickness=2)
        passwordEntry.insert(0, "      Password")
        passwordEntry.bind("<FocusIn>", enter2)
        passwordEntry.bind("<FocusOut>", leave2)
        passwordEntry.place(x=80,y=150)
        
        loginButton=Button(frame,text="Login",font=("Arial 12 bold"),padx=30,pady=10,bg="cyan",command=login)
        window.bind("<Return>",lambda event:login())
        loginButton.place(x=138,y=200)
        
        cancleButton=Button(frame,text="X",bg="red",fg="white",padx=10,command=cancle)
        cancleButton.place(x=760,y=0)
        
        label=Label(frame,text=" Student Login",font=("Arial 17 bold"),bg="pink",padx=85,relief=RAISED)
        label.place(x=445,y=50)
        def enter(e):
                SusernameEntry.delete(0, "end")
        def leave(e):
                if SusernameEntry.get() == "":
                    SusernameEntry.insert(0, "       Username")
        studentusername=StringVar()
        studentusername.set("")
        SusernameEntry=Entry(frame,textvariable=studentusername,width=20,font=("Arial 15 bold"),highlightbackground="pink",highlightthickness=2)
        SusernameEntry.insert(0, "      Username")
        SusernameEntry.bind("<FocusIn>", enter)
        SusernameEntry.bind("<FocusOut>", leave)
        SusernameEntry.place(x=500,y=100)
        def enter(e):
                
                SpasswordEntry.delete(0, "end")
        def leave(e):
                if SpasswordEntry.get() == "":
                    SpasswordEntry.insert(0, "       Password")
        def cancle():
            frame.destroy()
        studentpassword=StringVar()
        studentpassword.set("")
        SpasswordEntry=Entry(frame,textvariable=studentpassword,width=20,font=("Arial 15 bold"),highlightbackground="pink",highlightthickness=2)
        SpasswordEntry.insert(0, "      Password")
        SpasswordEntry.bind("<FocusIn>", enter)
        SpasswordEntry.bind("<FocusOut>", leave)
        SpasswordEntry.place(x=500,y=150)
        
        loginButton1=Button(frame,text="Login",font=("Arial 12 bold"),padx=30,pady=10,bg="pink",command=studentlogin)
        window.bind("<Return>",lambda event:studentlogin())
        loginButton1.place(x=550,y=200)
        
        register=Button(frame,text="Resister Here",font="Arial 10 bold",command=add,bg="#E8E8E8",fg="blue",relief=FLAT)
        register.place(x=565,y=260)
        window.mainloop()
# =====================================**********Examination********================
    def Examination():
        global frame4,frame3,frame5
        frame4.destroy()
        frame3.destroy()
        frame5.destroy()
        def getpdf():
            global val
            from addpdf import get,convertbinarytopdf
            usn1 = usn.get().upper()
            outputpdf = 'show.pdf'
            if usn1 == "":
                msg.showinfo("Message", "Enter USN please")
            elif pdfsem.get() == "":
                msg.showinfo("Message", "Enter Semester please")
            else:
                data = get(usn1)
                if (pdfsem.get() == "First") and (data[2] is not None):
                    val = data[2]
                    convertbinarytopdf(val,outputpdf)
                    show(outputpdf)
                elif (pdfsem.get() == "Second") and (data[3] is not None):
                    val = data[3]
                    convertbinarytopdf(val, outputpdf)
                    show(outputpdf)
                elif (pdfsem.get() == "Third") and (data[4] is not None):
                    val = data[4]
                    convertbinarytopdf(val, outputpdf)
                    show(outputpdf)
                elif (pdfsem.get() == "Fourth") and (data[5] is not None):
                    val = data[5]
                    convertbinarytopdf(val, outputpdf)
                    show(outputpdf)
                elif (pdfsem.get() == "Fifth") and (data[6] is not None):
                    val = data[6]
                    convertbinarytopdf(val, outputpdf)
                    show(outputpdf)
                elif (pdfsem.get() == "Sixth") and (data[7] is not None):
                    val = data[7]
                    convertbinarytopdf(val, outputpdf)
                    show(outputpdf)
                elif (pdfsem.get() == "Seventh") and (data[8] is not None):
                    val = data[8]
                    convertbinarytopdf(val, outputpdf)
                    show(outputpdf)
                elif (pdfsem.get() == "Eighth") and (data[9] is not None):
                    val = data[9]
                    convertbinarytopdf(val, outputpdf)
                    show(outputpdf)
                else:
                    msg.showinfo("Message", "No Data available")
        def insertpdf():
            try:
                from addpdf import insert, get,update
                def file():
                    filename = filedialog.askopenfilename(initialdir="/Downloads", title="Select a File",
                                                        filetypes=(("PDF Files", "*.pdf"), ("ALL Files", "*.*")))
                    data = get(usn.get().upper())
                    if data is None:
                        insert(filename, pdfsem.get(), usn.get().upper())
                        msg.showinfo("Message", "Uploaded successfully")
                    elif data is not None:
                        if data[1] == usn.get().upper():
                            update(filename, pdfsem.get(), usn.get().upper())
                            msg.showinfo("Message", "Updated successfully")
                        else:
                            insert(filename, pdfsem.get(), usn.get().upper())
                            msg.showinfo("Message", "Uploaded successfully")
                    else:
                        pass
                if pdfsem.get() == "":
                    msg.showinfo("Message", "Enter Semester please")
                elif usn.get().upper() == "":
                    msg.showinfo("Message", "Enter USN please")
                else:
                    file()
            except:""
        def updatepdf():
            try:
                from addpdf import update
                def file1():
                    filename = filedialog.askopenfilename(initialdir="/Downloads", title="Select a File",
                                                        filetypes=(("PDF Files", "*.pdf"), ("ALL Files", "*.*")))
                    update(filename, pdfsem.get(), usn.get().upper())
                    msg.showinfo("Message", "Updated successfully")
                if pdfsem.get() == "":
                    msg.showinfo("Message", "Enter Semester please")
                elif usn.get().upper() == "":
                    msg.showinfo("Message", "Enter USN please")
                else:
                    file1()   
            except:""
        frame1=Frame(frame2,width=1366,height=670,bg="#E8E8E8")
        frame1.place(x=0,y=0)
        global frame_internal
        frame_internal=Frame(frame1,width=1110,height=620,bg="#E8E8E8",borderwidth=3,relief=SUNKEN,highlightbackground="black",highlightthickness=3)
        frame_internal.place(x=250,y=0)
        
        bottom=Frame(frame2,width=1366,height=27,bg="lightgray")
        bottom.place(x=0,y=625)
        
        date=datetime.date.today()
        datestr=str(date)
        Datestr=datestr.split("-")
        dates=Datestr[: : -1]
        d="-".join(dates)
        
        day=datetime.datetime.now().strftime("%A")
        dayLabel=Label(bottom,text=f'{day},',font=(
            "Times New Roman", 11, "bold"),bg="lightgray")
        dayLabel.place(x=1165,y=0)
        dateLabel=Label(bottom,text=d,font=(
            "Times New Roman", 11, "bold"),bg="lightgray")
        dateLabel.place(x=1250,y=0)
        global sideframe
        sideframe=Frame(frame1,width=250,height=650,bg="lightgray")
        sideframe.place(x=0,y=0)

        global pdfsem
        semlabel=Label(sideframe,text="Select Sem",bg="lightgray",font="Arial 10 bold ",fg="red")
        semlabel.place(x=80,y=50)
        pdfsem = StringVar()
        pdfsem.set("")
        sem = ["First", "Second", "Third", "Fourth", "Fifth", "Sixth", "Seventh", "Eighth"]
        sementry = ttk.Combobox(sideframe, width=10, values=sem, textvariable=pdfsem, font=("Arial 11 bold"))
        sementry.place(x=70, y=70)

        filein = Button(sideframe, width=32, text="Add Result", font=("Arial 10 bold"), bg="lightgray", fg="blue", bd=0
                        ,command=insertpdf)
        filein.place(x=0, y=170)
        fileget = Button(sideframe, width=32, text="Get Result", font=("Arial 10 bold"), bg="lightgray", fg="blue", bd=0
                        ,command=getpdf )
        fileget.place(x=0, y=120)
        fileup = Button(sideframe, width=32, text="Update Result", font=("Arial 10 bold"), bg="lightgray", fg="blue", bd=0
                    ,command=updatepdf )
        fileup.place(x=0, y=220)
        global usn
        usn = StringVar()
        usn.set("")
        usnentry = Entry(sideframe, textvariable=usn, font=("Arial 12 bold"), highlightbackground="black", highlightthickness=2)
        usnentry.place(x=20, y=10)
        
    def show(pdffile):
        for widgets in frame_internal.winfo_children():
            widgets.destroy()
        f = pdffile
        doc = fitz.open(f)
        global num_pages
        num_pages = 0
        for p in doc:
            num_pages += 1
        scrollbar = Scrollbar(frame_internal)
        scrollbar.pack(side=RIGHT, fill=Y)
        canvas = Canvas(frame_internal,width=980,height=600, yscrollcommand=scrollbar.set)
        canvas.pack(side=RIGHT, fill=BOTH,ipadx=48)
        mat = fitz.Matrix(1.8, 1.6)
        def pdf_to_img(page_num):
            page = doc.load_page(page_num)
            pix = page.get_pixmap(matrix=mat)
            return Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
        global page_num
        page_num = 0
        def show_image(page_num):
            try:
                assert page_num >= 0 and page_num < num_pages
                im = pdf_to_img(page_num)
                img_tk = ImageTk.PhotoImage(im)
                frame = Frame(canvas,width=1220,height=630)
                frame.place(x=150,y=0)
                panel = Label(frame, image=img_tk)
                panel.pack(side="bottom", fill="both", expand="yes")
                frame.image = img_tk
                canvas.create_window(0, 0, anchor='nw', window=frame)
                frame.update_idletasks()
                canvas.config(scrollregion=canvas.bbox("all"))
            except:
                pass
        show_image(0)
        scrollbar.config(command=canvas.yview)
        def next():
            global ps
            ps = page_num + 1
            show_image(ps)
        def prev():
            sh = ps - 1
            show_image(sh)
        nx = Button(sideframe, text="Next Page >>>>>", font=("Times New Roman", 11, "bold"), width=28, pady=10, bd=0, fg="blue",
                    command=next,bg="lightgray")
        nx.place(x=0, y=550)
        pre = Button(sideframe, text="<<<<< Previous Page ", font=("Times New Roman", 11, "bold"), width=28, pady=10, bd=0,
                    fg="blue",bg="lightgray",
                    command=prev)
        pre.place(x=0, y=590)   
    def exam():
        head = Frame(window)
        head.place(x=0,y=0)
        label1= Label(head, text="                   Examination    ", font=(
        "Times New Roman", 20, "bold"), bg="skyblue", fg="black")
        label1.pack(ipadx=510, ipady=2)
        frame4.destroy()
        frame3.destroy()
        frame5.destroy()
        frame6.destroy()
        Examination()
    head = Frame(window)
    head.place(x=0,y=0)
    label = Label(head, text="Student Management System", font=(
        "Times New Roman", 20, "bold"), bg="skyblue", fg="black")
    label.pack(ipadx=510, ipady=2)

# ================================Student Details=============================
    def Student_details():
        head = Frame(window)
        head.place(x=0,y=0)
        label1= Label(head, text="                   Student Information", font=(
        "Times New Roman", 20, "bold"), bg="skyblue", fg="black")
        label1.pack(ipadx=510, ipady=2)
        frame4.destroy()
        frame3.destroy()
        frame5.destroy()
        frame6.destroy()
        studentDetails()
    # ===============================*********Registration**********=================================    
    def register():
        def info():
            infoframe=Frame(window,width=700,height=600,bg="gray")
            infoframe.place(x=150,y=80)
            info = Frame(infoframe, width=700, height=600, bg="#E8E8E8", highlightbackground="black", highlightthickness=2)
            info.place(x=0, y=0)


            title = Label(info, text="Enter Your Details",
                        font="Arial 20 bold", bg="#E8E8E8", fg="#003153")
            title.place(x=215, y=5)
            Frame(info, width=700, height=1, bg="black").place(x=0, y=50)

            name = StringVar()
            namevar = Label(info, text="Name",
                            font="Arial 15 bold", bg="#E8E8E8", fg="#003153")
            namevar.place(x=50, y=60)
            nameEntry = Entry(info, width=20, textvariable=name, font="Arial 15 bold", bd=1,
                            bg="#E8E8E8", highlightcolor="#0f5289", highlightbackground="black", highlightthickness=1,
                            relief=FLAT)
            nameEntry.place(x=60, y=95)
            # 0f5289  003153
            fathername = StringVar()
            fname = Label(info, text="Father Name",
                        font="Arial 15 bold", bg="#E8E8E8", fg="#003153")
            fname.place(x=380, y=60)
            fnameEntry = Entry(info, width=20, textvariable=fathername, font="Arial 15 bold", bd=1,
                            bg="#E8E8E8", highlightcolor="#0f5289", highlightbackground="black", highlightthickness=1,
                            relief=FLAT)
            fnameEntry.place(x=392, y=92)

            usn = StringVar()
            usnlabel = Label(info, text="USN",
                            font="Arial 15 bold", bg="#E8E8E8", fg="#003153")
            usnlabel.place(x=50, y=130)
            usnEntry = Entry(info, width=20, textvariable=usn, font="Arial 15 bold", bd=1,
                            bg="#E8E8E8", highlightcolor="#0f5289", highlightbackground="black", highlightthickness=1, relief=FLAT)
            usnEntry.place(x=60, y=157)

            Branch = StringVar()
            branchlabel = Label(info, text="Branch",
                                font="Arial 15 bold", bg="#E8E8E8", fg="#003153")
            branchlabel.place(x=380, y=130)
            BranchEntry = Entry(info, textvariable=Branch, width=20, font="Arial 15 bold", bd=1,
                                bg="#E8E8E8", highlightcolor="#0f5289", highlightbackground="black", highlightthickness=1,
                                relief=FLAT)
            BranchEntry.place(x=392, y=157)

            phone = StringVar()
            phonelabel = Label(info, text="Mobile No.",
                            font="Arial 15 bold", bg="#E8E8E8", fg="#003153")
            phonelabel.place(x=50, y=200)
            phoneEntry = Entry(info, width=20, textvariable=phone, font="Arial 15 bold", bd=1,
                            bg="#E8E8E8", highlightcolor="#0f5289", highlightbackground="black", highlightthickness=1,
                            relief=FLAT)
            phoneEntry.place(x=60, y=227)

            fphone = StringVar()
            fphonelabel = Label(info, text="Father's Mobile No.",
                                font=("Arial 15 bold"), bg="#E8E8E8", fg="#003153")
            fphonelabel.place(x=380, y=200)
            fphoneEntry = Entry(info, width=20, textvariable=fphone, font="Arial 15 bold", bd=1,
                                bg="#E8E8E8", highlightcolor="#0f5289", highlightbackground="black", highlightthickness=1,
                                relief=FLAT)
            fphoneEntry.place(x=392, y=227)

            sem = StringVar()
            semlabel = Label(info, text="Semester",
                            font="Arial 15 bold", bg="#E8E8E8", fg="#003153")
            semlabel.place(x=50, y=270)
            semEntry = Entry(info, width=20, textvariable=sem, font="Arial 15 bold", bd=1,
                            bg="#E8E8E8", highlightcolor="#0f5289", highlightbackground="black", highlightthickness=1, relief=FLAT)
            semEntry.place(x=60, y=300)

            gender = StringVar()
            genderlabel = Label(info, text="Gender",
                                font="Arial 15 bold", bg="#E8E8E8", fg="#003153")
            genderlabel.place(x=380, y=270)
            genderEntry = Entry(info, width=20, textvariable=gender, font="Arial 15 bold", bd=1,
                                bg="#E8E8E8", highlightcolor="#0f5289", highlightbackground="black", highlightthickness=1,
                                relief=FLAT)
            genderEntry.place(x=392, y=300)

            email = StringVar()
            emailabel = Label(info, text="Email Address",
                            font=("Arial 15 bold"), bg="#E8E8E8", fg="#003153")
            emailabel.place(x=50, y=340)
            emailEntry = Entry(info, width=35, textvariable=email, font="Arial 15 bold", bd=1,
                            bg="#E8E8E8", highlightcolor="#0f5289", highlightbackground="black", highlightthickness=1,
                            relief=FLAT)
            emailEntry.place(x=60, y=370)

            addr = StringVar()
            addrlabel = Label(info, text="Address",
                            font=("Arial 15 bold"), bg="#E8E8E8", fg="#003153")
            addrlabel.place(x=50, y=410)
            addrEntry = Entry(info, width=40, textvariable=addr, font="Arial 15 bold", bd=1,
                            bg="#E8E8E8", highlightcolor="#0f5289", highlightbackground="black", highlightthickness=1,
                            relief=FLAT)
            addrEntry.place(x=60, y=440)

            def Cancle():
               infoframe.destroy() 
            def add():
                infoframe.destroy()

            button = Button(info, width=27, text="SUBMIT", bg="#E8E8E8", fg="#003153", bd=0, font="Arial 15 bold",
                            command=add, highlightcolor="#003153", highlightthickness=1)
            button.place(x=180, y=480)
            canclebutton=Button(info,text="X",bg="red",fg="white",width=5,command=Cancle)
            canclebutton.place(x=650,y=0)
      
        def Registerdetails():
                global username1
                username1=""
                try:
                    from accessing import Access_user_password
                    userdetails=Access_user_password(user.get().upper())
                    username1=userdetails[0][0]
                except:""
                if user.get()=="      Username" and userpass.get()=="      Password":
                    msg.showwarning("Warning","Please Fill Details")
                elif user.get().upper()==username1:
                    msg.showinfo("Registration","Already Registered")
                    frame_login.destroy()
                else:
                    from inserting_values import Insert_user_passoword
                    Insert_user_passoword(user.get().upper(),userpass.get())
                    msg.showinfo("Registration","Registration Successfully")
                    frame_login.destroy()
                    info()
        def Cancle():
                frame_login.destroy()
        def enter(e):
            userEntry.delete(0, "end")
        def leave(e):
            if userEntry.get() == "":
                userEntry.insert(0, "       Username")
        frame_login=Frame(window,width=400,height=300,bg="#E8E8E8",highlightbackground="skyblue",highlightthickness=2)
        frame_login.place(x=500,y=230)
        label=Label(frame_login,text="New Student Registration",font=("Arial 15 bold"),bg="#E8E8E8")
        label.place(x=80,y=25)
        
        user=StringVar()
        user.set("")
        userEntry=Entry(frame_login,textvariable=user,width=30,font=("Arial 12 bold"),highlightbackground="skyblue",highlightthickness=2)
        userEntry.insert(0, "      Username")
        userEntry.bind("<FocusIn>", enter)
        userEntry.bind("<FocusOut>", leave)
        userEntry.place(x=70,y=100)
        def enter(e):
                userpassEntry.delete(0, "end")
        def leave(e):
                if userpassEntry.get() == "":
                    userpassEntry.insert(0, "       Password")
        userpass=StringVar()
        userpass.set("")
        userpassEntry=Entry(frame_login,textvariable=userpass,width=30,font=("Arial 12 bold"),highlightbackground="skyblue",highlightthickness=2)
        userpassEntry.insert(0, "      Password")
        userpassEntry.bind("<FocusIn>", enter)
        userpassEntry.bind("<FocusOut>", leave)
        userpassEntry.place(x=70,y=150)
        
        register_button=Button(frame_login,text="Register",font=("Arial 10 bold"),padx=25,command=Registerdetails)
        window.bind("<Return>",lambda event:Registerdetails())
        register_button.place(x=155,y=200)
        cancleButton1=Button(frame_login,text="X",bg="red",fg="white",padx=10,command=Cancle)
        cancleButton1.place(x=360,y=0)  
    # ------------------------------------main Frame---------------------------------------------------------   
    global frame2
    frame2 = Frame(window, width=1366, height=768,bg="white")
    frame2.place(x=0, y=41)
    # -------------------------------------------------------------------------------------------------------------
    # ====================================***********Attendence***********====================
    def attend():
        frame1=Frame(frame2,width=1000,height=600,bg="#E8E8E8",highlightbackground="skyblue",highlightthickness=3)
        frame1.place(x=10,y=20)
        sideframe=Frame(frame1,width=245,height=590,bg="lightgray")
        sideframe.place(x=750,y=0)
        frame_attendence=Frame(frame1,width=720,height=590,bg="#E8E8E8")
        frame_attendence.place(x=0,y=0)
        def Get():
            if len(usn.get().upper())==10:
                usnEntry.config(state="disabled")
                from accessing import Access_student_attendence
                try:
                        data=Access_student_attendence(usn.get().upper())
                        subject1.set(data[0][1])
                        subject1Entry.update()
                        subject1total.set(data[0][3])
                        subject1totalEntry.update()
                        subject1attend.set(data[0][2])
                        subject1attendEntry.update()
                        
                        subject2.set(data[0][4])
                        subject2Entry.update()
                        subject2total.set(data[0][6])
                        subject2totalEntry.update()
                        subject2attend.set(data[0][5])
                        subject2attendEntry.update()
                        
                        subject3.set(data[0][7])
                        subject3Entry.update()
                        subject3total.set(data[0][9])
                        subject3totalEntry.update()
                        subject3attend.set(data[0][8])
                        subject3attendEntry.update()
                        
                        subject4.set(data[0][10])
                        subject4Entry.update()
                        subject4total.set(data[0][12])
                        subject4totalEntry.update()
                        subject4attend.set(data[0][11])
                        subject4attendEntry.update()
                        
                        subject5.set(data[0][13])
                        subject5Entry.update()
                        subject5total.set(data[0][15])
                        subject5totalEntry.update()
                        subject5attend.set(data[0][14])
                        subject5attendEntry.update()
                        
                        subject6.set(data[0][16])
                        subject6Entry.update()
                        subject6total.set(data[0][18])
                        subject6totalEntry.update()
                        subject6attend.set(data[0][17])
                        subject6attendEntry.update()
                        
                        subject7.set(data[0][19])
                        subject7Entry.update()
                        subject7total.set(data[0][21])
                        subject7totalEntry.update()
                        subject7attend.set(data[0][20])
                        subject7attendEntry.update()
                        
                        subject8.set(data[0][22])
                        subject8Entry.update()
                        subject8total.set(data[0][24])
                        subject8totalEntry.update()
                        subject8attend.set(data[0][23])
                        subject8attendEntry.update()
                        
                        lab1.set(data[0][25])
                        lab1Entry.update()
                        lab1total.set(data[0][27])
                        lab1totalEntry.update()
                        lab1attend.set(data[0][26])
                        lab1attendEntry.update()
                except: "" 
                try:
                    attenddata=Access_student_attendence(usn.get().upper())
                    lab2.set(attenddata[0][28])
                    lab2Entry.update()
                    lab2total.set(attenddata[0][30])
                    lab2totalEntry.update()
                    lab2attend.set(attenddata[0][29])
                    lab2attendEntry.update()
                except:""
                try:
                    attenddata=Access_student_attendence(usn.get().upper())
                    lab3.set(attenddata[0][31])
                    lab3Entry.update()
                    lab3total.set(attenddata[0][33])
                    lab3totalEntry.update()
                    lab3attend.set(attenddata[0][32])
                    lab3attendEntry.update()
                except:""
            else:
                msg.showwarning("Warning","Please Enter Correct USN Number")   
        def add():
            if usn.get().upper()=="      Student USN":
                msg.showinfo("Attendence","Please Enter USN Number")
            elif len(usn.get().upper())!=10:
                msg.showwarning("Warning","Please Enter Correct USN Number")
            else:
                from inserting_values import Insert_student_attendence
                Insert_student_attendence(usn.get().upper(),subject1.get().upper(),subject1attend.get(),subject1total.get(),subject2.get().upper(),subject2attend.get(),subject2total.get(),subject3.get().upper(),subject3attend.get(),subject3total.get(),subject4.get().upper(),subject4attend.get(),subject4total.get(),subject5.get().upper(),subject5attend.get(),subject5total.get(),subject6.get().upper(),subject6attend.get(),subject6total.get(),subject7.get().upper(),subject7attend.get(),subject7total.get(),subject8.get().upper(),subject8attend.get(),subject8total.get(),lab1.get().upper(),lab1attend.get(),lab1total.get(),lab2.get().upper(),lab2attend.get(),lab2total.get(),lab3.get().upper(),lab3attend.get(),lab3total.get())
                msg.showinfo("Attendence","Attendence Is Saved Successfully")
            pass
        def cancle():
            frame1.destroy()
        def Update():
            studentdb = mysql.connector.connect( host='localhost', user='root', password='guru8296jadhav@', database="student_information")
            cur = studentdb.cursor(buffered=True)
            
            s=f" UPDATE `student_information`.`student_attendence` SET aclass1='{subject1total.get()}' WHERE USN='{usn.get().upper()}'"
            cur.execute(s)
            studentdb.commit()
            
            s=f" UPDATE `student_information`.`student_attendence` SET ttclass1='{subject1attend.get()}' WHERE USN='{usn.get().upper()}'"
            cur.execute(s)
            studentdb.commit()
            
            s=f" UPDATE `student_information`.`student_attendence` SET aclass2='{subject2total.get()}' WHERE USN='{usn.get().upper()}'"
            cur.execute(s)
            studentdb.commit()
            
            s=f" UPDATE `student_information`.`student_attendence` SET ttclass2='{subject2attend.get()}' WHERE USN='{usn.get().upper()}'"
            cur.execute(s)
            studentdb.commit()
            s=f" UPDATE `student_information`.`student_attendence` SET aclass3='{subject3total.get()}' WHERE USN='{usn.get().upper()}'"
            cur.execute(s)
            studentdb.commit()
            
            s=f" UPDATE `student_information`.`student_attendence` SET ttclass3='{subject3attend.get()}' WHERE USN='{usn.get().upper()}'"
            cur.execute(s)
            studentdb.commit()
            s=f" UPDATE `student_information`.`student_attendence` SET aclass4='{subject4total.get()}' WHERE USN='{usn.get().upper()}'"
            cur.execute(s)
            studentdb.commit()
            
            s=f" UPDATE `student_information`.`student_attendence` SET ttclass4='{subject4attend.get()}' WHERE USN='{usn.get().upper()}'"
            cur.execute(s)
            studentdb.commit()
            s=f" UPDATE `student_information`.`student_attendence` SET aclass5='{subject5total.get()}' WHERE USN='{usn.get().upper()}'"
            cur.execute(s)
            studentdb.commit()
            
            s=f" UPDATE `student_information`.`student_attendence` SET ttclass5='{subject5attend.get()}' WHERE USN='{usn.get().upper()}'"
            cur.execute(s)
            studentdb.commit()
            s=f" UPDATE `student_information`.`student_attendence` SET aclass6='{subject6total.get()}' WHERE USN='{usn.get().upper()}'"
            cur.execute(s)
            studentdb.commit()
            
            s=f" UPDATE `student_information`.`student_attendence` SET ttclass6='{subject6attend.get()}' WHERE USN='{usn.get().upper()}'"
            cur.execute(s)
            studentdb.commit()
            s=f" UPDATE `student_information`.`student_attendence` SET aclass7='{subject7total.get()}' WHERE USN='{usn.get().upper()}'"
            cur.execute(s)
            studentdb.commit()
            
            s=f" UPDATE `student_information`.`student_attendence` SET ttclass7='{subject7attend.get()}' WHERE USN='{usn.get().upper()}'"
            cur.execute(s)
            studentdb.commit()
            
            s=f" UPDATE `student_information`.`student_attendence` SET aclass8='{subject8total.get()}' WHERE USN='{usn.get().upper()}'"
            cur.execute(s)
            studentdb.commit()
            
            s=f" UPDATE `student_information`.`student_attendence` SET ttclass8='{subject8attend.get()}' WHERE USN='{usn.get().upper()}'"
            cur.execute(s)
            studentdb.commit()
            
            s=f" UPDATE `student_information`.`student_attendence` SET alab1='{lab1total.get()}' WHERE USN='{usn.get().upper()}'"
            cur.execute(s)
            studentdb.commit()
            
            s=f" UPDATE `student_information`.`student_attendence` SET ttlab1='{lab1attend.get()}' WHERE USN='{usn.get().upper()}'"
            cur.execute(s)
            studentdb.commit()
            
            s=f" UPDATE `student_information`.`student_attendence` SET alab2='{lab2total.get()}' WHERE USN='{usn.get().upper()}'"
            cur.execute(s)
            studentdb.commit()
            
            s=f" UPDATE `student_information`.`student_attendence` SET ttlab2='{lab2attend.get()}' WHERE USN='{usn.get().upper()}'"
            cur.execute(s)
            studentdb.commit()
            s=f" UPDATE `student_information`.`student_attendence` SET alab3='{lab3total.get()}' WHERE USN='{usn.get().upper()}'"
            cur.execute(s)
            studentdb.commit()
            
            s=f" UPDATE `student_information`.`student_attendence` SET ttlab3='{lab3attend.get()}' WHERE USN='{usn.get().upper()}'"
            cur.execute(s)
            studentdb.commit()
            
            msg.showinfo("message","Update")
        def Delete():
            msg.showinfo("message","Delete")
            pass
        label=Label(frame1,text="Student Attendence Registration",font="Arial 15 bold",bg="#E8E8E8",fg="red")
        label.place(x=200,y=10)

        subjectslabel=Label(frame_attendence,text="Subjects",font="Arial 15 bold",bg="#E8E8E8")
        subjectslabel.place(x=150,y=50)

        totalclasslabel=Label(frame_attendence,text="Total Classes",font="Arial 15 bold",bg="#E8E8E8")
        totalclasslabel.place(x=370,y=50)

        attendedclasses=Label(frame_attendence,text="Attended Classes",font="Arial 15 bold",bg="#E8E8E8")
        attendedclasses.place(x=550,y=50)
        global i
        i=0
        def Down1(e):
            global i
            i+=1
            if i==1:
                subject1totalEntry.focus_set()
                subject1attendEntry.focus_set()
                subject1Entry.focus_set()
            elif i==2:
                subject2totalEntry.focus_set()
                subject2attendEntry.focus_set()
                subject2Entry.focus_set()
            elif i==3:
                subject3totalEntry.focus_set()
                subject3attendEntry.focus_set()
                subject3Entry.focus_set()
            elif i==4:
                subject4totalEntry.focus_set()
                subject4attendEntry.focus_set()
                subject4Entry.focus_set()
            elif i==5:
                subject5totalEntry.focus_set()
                subject5attendEntry.focus_set()
                subject5Entry.focus_set()
            elif i==6:
                subject6totalEntry.focus_set()
                subject6attendEntry.focus_set()
                subject6Entry.focus_set()
            elif i==7:
                subject7totalEntry.focus_set()
                subject7attendEntry.focus_set()
                subject7Entry.focus_set()
            elif i==8:
                subject8totalEntry.focus_set()
                subject8attendEntry.focus_set()
                subject8Entry.focus_set()
                
            elif i==9:
                lab1totalEntry.focus_set()
                lab1attendEntry.focus_set()
                lab1Entry.focus_set()
            elif i==10:
                lab2totalEntry.focus_set()
                lab2attendEntry.focus_set()
                lab2Entry.focus_set()
            elif i==11:
                lab3totalEntry.focus_set()
                lab3attendEntry.focus_set()
                lab3Entry.focus_set()
                i-=11
       
        window.bind("<Right>",Down1)
        
        def enter(e):
                usnEntry.delete(0, "end")
        def leave(e):
                if usnEntry.get() == "":
                    usnEntry.insert(0, "       Student USN")
        usn=StringVar()
        usn.set("")
        usnEntry=Entry(sideframe,textvariable=usn,font="Arial 15 bold",width=18,highlightbackground="skyblue",highlightthickness=1,relief=SUNKEN)
        usnEntry.insert(0, "      Student USN")
        usnEntry.bind("<FocusIn>", enter)
        usnEntry.bind("<FocusOut>", leave)
        usnEntry.place(x=25,y=30)

        subject1=StringVar()
        subject1.set("")
        subject1label=Label(frame_attendence,text="Subject 1",font="Arial 10 bold",bg="#E8E8E8")
        subject1label.place(x=10,y=100)
        subject1Entry=Entry(frame_attendence,textvariable=subject1,width=35,font="Arial 10 bold",highlightbackground="skyblue",highlightthickness=1)
        subject1Entry.bind("<FocusIn>",lambda e:subject1Entry.config(highlightbackground="skyblue",highlightthickness=2))
        subject1Entry.bind("<FocusOut>",lambda e:subject1Entry.config(highlightbackground="black",highlightthickness=1))
        subject1Entry.focus_set()
        subject1Entry.place(x=80,y=100)

        subject1total=IntVar()
        subject1total.set("")
        subject1totalEntry=Entry(frame_attendence,textvariable=subject1total,width=15,font="Arial 10 bold",highlightbackground="skyblue",highlightthickness=1)
        subject1totalEntry.bind("<FocusIn>",lambda e:subject1totalEntry.config(highlightbackground="skyblue",highlightthickness=2))
        subject1totalEntry.bind("<FocusOut>",lambda e:subject1totalEntry.config(highlightbackground="black",highlightthickness=1))
        subject1totalEntry.focus_set()
        subject1totalEntry.place(x=570,y=100)

        subject1attend=IntVar()
        subject1attend.set("")
        subject1attendEntry=Entry(frame_attendence,textvariable=subject1attend,width=15,font="Arial 10 bold",highlightbackground="skyblue",highlightthickness=1)
        subject1attendEntry.bind("<FocusIn>",lambda e:subject1attendEntry.config(highlightbackground="skyblue",highlightthickness=2))
        subject1attendEntry.bind("<FocusOut>",lambda e:subject1attendEntry.config(highlightbackground="black",highlightthickness=1))
        subject1attendEntry.focus_set()
        subject1attendEntry.place(x=380,y=100)

        subject2=StringVar()
        subject2.set("")
        subject2label=Label(frame_attendence,text="Subject 2",font="Arial 10 bold",bg="#E8E8E8")
        subject2label.place(x=10,y=140)
        subject2Entry=Entry(frame_attendence,textvariable=subject2,width=35,font="Arial 10 bold",highlightbackground="skyblue",highlightthickness=1)
        subject2Entry.bind("<FocusIn>",lambda e:subject2Entry.config(highlightbackground="skyblue",highlightthickness=2))
        subject2Entry.bind("<FocusOut>",lambda e:subject2Entry.config(highlightbackground="black",highlightthickness=1))
        subject2Entry.place(x=80,y=140)

        subject2total=IntVar()
        subject2total.set("")
        subject2totalEntry=Entry(frame_attendence,textvariable=subject2total,width=15,font="Arial 10 bold",highlightbackground="skyblue",highlightthickness=1)
        subject2totalEntry.bind("<FocusIn>",lambda e:subject2totalEntry.config(highlightbackground="skyblue",highlightthickness=2))
        subject2totalEntry.bind("<FocusOut>",lambda e:subject2totalEntry.config(highlightbackground="black",highlightthickness=1))
        subject2totalEntry.place(x=570,y=140)

        subject2attend=IntVar()
        subject2attend.set("")
        subject2attendEntry=Entry(frame_attendence,textvariable=subject2attend,width=15,font="Arial 10 bold",highlightbackground="skyblue",highlightthickness=1)
        subject2attendEntry.bind("<FocusIn>",lambda e:subject2attendEntry.config(highlightbackground="skyblue",highlightthickness=2))
        subject2attendEntry.bind("<FocusOut>",lambda e:subject2attendEntry.config(highlightbackground="black",highlightthickness=1))
        subject2attendEntry.place(x=380,y=140)

        subject3=StringVar()
        subject3.set("")
        subject3label=Label(frame_attendence,text="Subject 3",font="Arial 10 bold",bg="#E8E8E8")
        subject3label.place(x=10,y=180)
        subject3Entry=Entry(frame_attendence,textvariable=subject3,width=35,font="Arial 10 bold",highlightbackground="skyblue",highlightthickness=1)
        subject3Entry.bind("<FocusIn>",lambda e:subject3Entry.config(highlightbackground="skyblue",highlightthickness=2))
        subject3Entry.bind("<FocusOut>",lambda e:subject3Entry.config(highlightbackground="black",highlightthickness=1))
        subject3Entry.place(x=80,y=180)

        subject3total=IntVar()
        subject3total.set("")
        subject3totalEntry=Entry(frame_attendence,textvariable=subject3total,width=15,font="Arial 10 bold",highlightbackground="skyblue",highlightthickness=1)
        subject3totalEntry.bind("<FocusIn>",lambda e:subject3totalEntry.config(highlightbackground="skyblue",highlightthickness=2))
        subject3totalEntry.bind("<FocusOut>",lambda e:subject3totalEntry.config(highlightbackground="black",highlightthickness=1))
        subject3totalEntry.place(x=570,y=180)

        subject3attend=IntVar()
        subject3attend.set("")
        subject3attendEntry=Entry(frame_attendence,textvariable=subject3attend,width=15,font="Arial 10 bold",highlightbackground="skyblue",highlightthickness=1)
        subject3attendEntry.bind("<FocusIn>",lambda e:subject3attendEntry.config(highlightbackground="skyblue",highlightthickness=2))
        subject3attendEntry.bind("<FocusOut>",lambda e:subject3attendEntry.config(highlightbackground="black",highlightthickness=1))
        subject3attendEntry.place(x=380,y=180)

        subject4=StringVar()
        subject4.set("")
        subject4label=Label(frame_attendence,text="Subject 4",font="Arial 10 bold",bg="#E8E8E8")
        subject4label.place(x=10,y=220)
        subject4Entry=Entry(frame_attendence,textvariable=subject4,width=35,font="Arial 10 bold",highlightbackground="skyblue",highlightthickness=1)
        subject4Entry.bind("<FocusIn>",lambda e:subject4Entry.config(highlightbackground="skyblue",highlightthickness=2))
        subject4Entry.bind("<FocusOut>",lambda e:subject4Entry.config(highlightbackground="black",highlightthickness=1))
        subject4Entry.place(x=80,y=220)

        subject4total=IntVar()
        subject4total.set("")
        subject4totalEntry=Entry(frame_attendence,textvariable=subject4total,width=15,font="Arial 10 bold",highlightbackground="skyblue",highlightthickness=1)
        subject4totalEntry.bind("<FocusIn>",lambda e:subject4totalEntry.config(highlightbackground="skyblue",highlightthickness=2))
        subject4totalEntry.bind("<FocusOut>",lambda e:subject4totalEntry.config(highlightbackground="black",highlightthickness=1))
        subject4totalEntry.place(x=570,y=220)

        subject4attend=IntVar()
        subject4attend.set("")
        subject4attendEntry=Entry(frame_attendence,textvariable=subject4attend,width=15,font="Arial 10 bold",highlightbackground="skyblue",highlightthickness=1)
        subject4attendEntry.bind("<FocusIn>",lambda e:subject4attendEntry.config(highlightbackground="skyblue",highlightthickness=2))
        subject4attendEntry.bind("<FocusOut>",lambda e:subject4attendEntry.config(highlightbackground="black",highlightthickness=1))
        subject4attendEntry.place(x=380,y=220)

        subject5=StringVar()
        subject5.set("")
        subject5label=Label(frame_attendence,text="Subject 5",font="Arial 10 bold",bg="#E8E8E8")
        subject5label.place(x=10,y=260)
        subject5Entry=Entry(frame_attendence,textvariable=subject5,width=35,font="Arial 10 bold",highlightbackground="skyblue",highlightthickness=1)
        subject5Entry.bind("<FocusIn>",lambda e:subject5Entry.config(highlightbackground="skyblue",highlightthickness=2))
        subject5Entry.bind("<FocusOut>",lambda e:subject5Entry.config(highlightbackground="black",highlightthickness=1))
        subject5Entry.place(x=80,y=260)

        subject5total=IntVar()
        subject5total.set("")
        subject5totalEntry=Entry(frame_attendence,textvariable=subject5total,width=15,font="Arial 10 bold",highlightbackground="skyblue",highlightthickness=1)
        subject5totalEntry.bind("<FocusIn>",lambda e:subject5totalEntry.config(highlightbackground="skyblue",highlightthickness=2))
        subject5totalEntry.bind("<FocusOut>",lambda e:subject5totalEntry.config(highlightbackground="black",highlightthickness=1))
        subject5totalEntry.place(x=570,y=260)

        subject5attend=IntVar()
        subject5attend.set("")
        subject5attendEntry=Entry(frame_attendence,textvariable=subject5attend,width=15,font="Arial 10 bold",highlightbackground="skyblue",highlightthickness=1)
        subject5attendEntry.bind("<FocusIn>",lambda e:subject5attendEntry.config(highlightbackground="skyblue",highlightthickness=2))
        subject5attendEntry.bind("<FocusOut>",lambda e:subject5attendEntry.config(highlightbackground="black",highlightthickness=1))
        subject5attendEntry.place(x=380,y=260)

        subject6=StringVar()
        subject6.set("")
        subject6label=Label(frame_attendence,text="Subject 6",font="Arial 10 bold",bg="#E8E8E8")
        subject6label.place(x=10,y=300)
        subject6Entry=Entry(frame_attendence,textvariable=subject6,width=35,font="Arial 10 bold",highlightbackground="skyblue",highlightthickness=1)
        subject6Entry.bind("<FocusIn>",lambda e:subject6Entry.config(highlightbackground="skyblue",highlightthickness=2))
        subject6Entry.bind("<FocusOut>",lambda e:subject6Entry.config(highlightbackground="black",highlightthickness=1))
        subject6Entry.place(x=80,y=300)

        subject6total=IntVar()
        subject6total.set("")
        subject6totalEntry=Entry(frame_attendence,textvariable=subject6total,width=15,font="Arial 10 bold",highlightbackground="skyblue",highlightthickness=1)
        subject6totalEntry.bind("<FocusIn>",lambda e:subject6totalEntry.config(highlightbackground="skyblue",highlightthickness=2))
        subject6totalEntry.bind("<FocusOut>",lambda e:subject6totalEntry.config(highlightbackground="black",highlightthickness=1))
        subject6totalEntry.place(x=570,y=300)

        subject6attend=IntVar()
        subject6attend.set("")
        subject6attendEntry=Entry(frame_attendence,textvariable=subject6attend,width=15,font="Arial 10 bold",highlightbackground="skyblue",highlightthickness=1)
        subject6attendEntry.bind("<FocusIn>",lambda e:subject6attendEntry.config(highlightbackground="skyblue",highlightthickness=2))
        subject6attendEntry.bind("<FocusOut>",lambda e:subject6attendEntry.config(highlightbackground="black",highlightthickness=1))
        subject6attendEntry.place(x=380,y=300)

        subject7=StringVar()
        subject7.set("")
        subject7label=Label(frame_attendence,text="Subject 7",font="Arial 10 bold",bg="#E8E8E8")
        subject7label.place(x=10,y=340)
        subject7Entry=Entry(frame_attendence,textvariable=subject7,width=35,font="Arial 10 bold",highlightbackground="skyblue",highlightthickness=1)
        subject7Entry.bind("<FocusIn>",lambda e:subject7Entry.config(highlightbackground="skyblue",highlightthickness=2))
        subject7Entry.bind("<FocusOut>",lambda e:subject7Entry.config(highlightbackground="black",highlightthickness=1))
        subject7Entry.place(x=80,y=340)

        subject7total=IntVar()
        subject7total.set("")
        subject7totalEntry=Entry(frame_attendence,textvariable=subject7total,width=15,font="Arial 10 bold",highlightbackground="skyblue",highlightthickness=1)
        subject7totalEntry.bind("<FocusIn>",lambda e:subject7totalEntry.config(highlightbackground="skyblue",highlightthickness=2))
        subject7totalEntry.bind("<FocusOut>",lambda e:subject7totalEntry.config(highlightbackground="black",highlightthickness=1))
        subject7totalEntry.place(x=570,y=340)

        subject7attend=IntVar()
        subject7attend.set("")
        subject7attendEntry=Entry(frame_attendence,textvariable=subject7attend,width=15,font="Arial 10 bold",highlightbackground="skyblue",highlightthickness=1)
        subject7attendEntry.bind("<FocusIn>",lambda e:subject7attendEntry.config(highlightbackground="skyblue",highlightthickness=2))
        subject7attendEntry.bind("<FocusOut>",lambda e:subject7attendEntry.config(highlightbackground="black",highlightthickness=1))
        subject7attendEntry.place(x=380,y=340)

        subject8=StringVar()
        subject8.set("")
        subject8label=Label(frame_attendence,text="Subject 8",font="Arial 10 bold",bg="#E8E8E8")
        subject8label.place(x=10,y=380)
        subject8Entry=Entry(frame_attendence,textvariable=subject8,width=35,font="Arial 10 bold",highlightbackground="skyblue",highlightthickness=1)
        subject8Entry.bind("<FocusIn>",lambda e:subject8Entry.config(highlightbackground="skyblue",highlightthickness=2))
        subject8Entry.bind("<FocusOut>",lambda e:subject8Entry.config(highlightbackground="black",highlightthickness=1))
        subject8Entry.place(x=80,y=380)

        subject8total=IntVar()
        subject8total.set("")
        subject8totalEntry=Entry(frame_attendence,textvariable=subject8total,width=15,font="Arial 10 bold",highlightbackground="skyblue",highlightthickness=1)
        subject8totalEntry.bind("<FocusIn>",lambda e:subject8totalEntry.config(highlightbackground="skyblue",highlightthickness=2))
        subject8totalEntry.bind("<FocusOut>",lambda e:subject8totalEntry.config(highlightbackground="black",highlightthickness=1))
        subject8totalEntry.place(x=570,y=380)

        subject8attend=IntVar()
        subject8attend.set("")
        subject8attendEntry=Entry(frame_attendence,textvariable=subject8attend,width=15,font="Arial 10 bold",highlightbackground="skyblue",highlightthickness=1)
        subject8attendEntry.bind("<FocusIn>",lambda e:subject8attendEntry.config(highlightbackground="skyblue",highlightthickness=2))
        subject8attendEntry.bind("<FocusOut>",lambda e:subject8attendEntry.config(highlightbackground="black",highlightthickness=1))
        subject8attendEntry.place(x=380,y=380)

        lab1=StringVar()
        lab1.set("")
        lab1label=Label(frame_attendence,text="Lab 1",font="Arial 10 bold",bg="#E8E8E8")
        lab1label.place(x=10,y=420)
        lab1Entry=Entry(frame_attendence,textvariable=lab1,width=35,font="Arial 10 bold",highlightbackground="skyblue",highlightthickness=1)
        lab1Entry.bind("<FocusIn>",lambda e:lab1Entry.config(highlightbackground="skyblue",highlightthickness=2))
        lab1Entry.bind("<FocusOut>",lambda e:lab1Entry.config(highlightbackground="black",highlightthickness=1))
        lab1Entry.place(x=80,y=420)

        lab1total=IntVar()
        lab1total.set("")
        lab1totalEntry=Entry(frame_attendence,textvariable=lab1total,width=15,font="Arial 10 bold",highlightbackground="skyblue",highlightthickness=1)
        lab1totalEntry.bind("<FocusIn>",lambda e:lab1totalEntry.config(highlightbackground="skyblue",highlightthickness=2))
        lab1totalEntry.bind("<FocusOut>",lambda e:lab1totalEntry.config(highlightbackground="black",highlightthickness=1))
        lab1totalEntry.place(x=570,y=420)

        lab1attend=IntVar()
        lab1attend.set("")
        lab1attendEntry=Entry(frame_attendence,textvariable=lab1attend,width=15,font="Arial 10 bold",highlightbackground="skyblue",highlightthickness=1)
        lab1attendEntry.bind("<FocusIn>",lambda e:lab1attendEntry.config(highlightbackground="skyblue",highlightthickness=2))
        lab1attendEntry.bind("<FocusOut>",lambda e:lab1attendEntry.config(highlightbackground="black",highlightthickness=1))
        lab1attendEntry.place(x=380,y=420)

        lab2=StringVar()
        lab2.set("")
        lab2label=Label(frame_attendence,text="Lab 2",font="Arial 10 bold",bg="#E8E8E8")
        lab2label.place(x=10,y=460)
        lab2Entry=Entry(frame_attendence,textvariable=lab2,width=35,font="Arial 10 bold",highlightbackground="skyblue",highlightthickness=1)
        lab2Entry.bind("<FocusIn>",lambda e:lab2Entry.config(highlightbackground="skyblue",highlightthickness=2))
        lab2Entry.bind("<FocusOut>",lambda e:lab2Entry.config(highlightbackground="black",highlightthickness=1))
        lab2Entry.place(x=80,y=460)

        lab2total=IntVar()
        lab2total.set("")
        lab2totalEntry=Entry(frame_attendence,textvariable=lab2total,width=15,font="Arial 10 bold",highlightbackground="skyblue",highlightthickness=1)
        lab2totalEntry.bind("<FocusIn>",lambda e:lab2totalEntry.config(highlightbackground="skyblue",highlightthickness=2))
        lab2totalEntry.bind("<FocusOut>",lambda e:lab2totalEntry.config(highlightbackground="black",highlightthickness=1))
        lab2totalEntry.place(x=570,y=460)

        lab2attend=IntVar()
        lab2attend.set("")
        lab2attendEntry=Entry(frame_attendence,textvariable=lab2attend,width=15,font="Arial 10 bold",highlightbackground="skyblue",highlightthickness=1)
        lab2attendEntry.bind("<FocusIn>",lambda e:lab2attendEntry.config(highlightbackground="skyblue",highlightthickness=2))
        lab2attendEntry.bind("<FocusOut>",lambda e:lab2attendEntry.config(highlightbackground="black",highlightthickness=1))
        lab2attendEntry.place(x=380,y=460)

        lab3=StringVar()
        lab3.set("")
        lab3label=Label(frame_attendence,text="Lab 3",font="Arial 10 bold",bg="#E8E8E8")
        lab3label.place(x=10,y=500)
        lab3Entry=Entry(frame_attendence,textvariable=lab3,width=35,font="Arial 10 bold",highlightbackground="skyblue",highlightthickness=1)
        lab3Entry.bind("<FocusIn>",lambda e:lab3Entry.config(highlightbackground="skyblue",highlightthickness=2))
        lab3Entry.bind("<FocusOut>",lambda e:lab3Entry.config(highlightbackground="black",highlightthickness=1))
        lab3Entry.place(x=80,y=500)

        lab3total=IntVar()
        lab3total.set("")
        lab3totalEntry=Entry(frame_attendence,textvariable=lab3total,width=15,font="Arial 10 bold",highlightbackground="skyblue",highlightthickness=1)
        lab3totalEntry.bind("<FocusIn>",lambda e:lab3totalEntry.config(highlightbackground="skyblue",highlightthickness=2))
        lab3totalEntry.bind("<FocusOut>",lambda e:lab3totalEntry.config(highlightbackground="black",highlightthickness=1))
        lab3totalEntry.place(x=570,y=500)

        lab3attend=IntVar()
        lab3attend.set("")
        lab3attendEntry=Entry(frame_attendence,textvariable=lab3attend,width=15,font="Arial 10 bold",highlightbackground="skyblue",highlightthickness=1)
        lab3attendEntry.bind("<FocusIn>",lambda e:lab3attendEntry.config(highlightbackground="skyblue",highlightthickness=2))
        lab3attendEntry.bind("<FocusOut>",lambda e:lab3attendEntry.config(highlightbackground="black",highlightthickness=1))
        lab3attendEntry.place(x=380,y=500)
        
        global addbutton,updatebutton,deletebutton,k,getbutton
        k=0
        def Down(e):
            global k
            k+=1
            if k==1:
                getbutton.focus_set()
                window.bind("<Return>",lambda event:Get())
            elif k==2:
                addbutton.focus_set()
                window.bind("<Return>",lambda event:add())
            elif k==3:
                updatebutton.focus_set()
                window.bind("<Return>",lambda event:Update())
            elif k==4:
                deletebutton.focus_set()
                window.bind("<Return>",lambda event:Delete())
                k-=4
                
        
        getbutton=Button(sideframe,text="Get Data",font="Arial 10 bold",width=15,height=2,command=Get)
        getbutton.bind("<FocusIn>",lambda e:getbutton.config(fg="green"))
        getbutton.bind("<FocusOut>",lambda e:getbutton.config(fg="black"))
        getbutton.focus_set()
        getbutton.place(x=70,y=70)
    
        window.bind("<Down>",Down)
        addbutton=Button(sideframe,text="Add",font="Arial 10 bold",width=15,height=2,command=add)
        addbutton.bind("<FocusIn>",lambda e:addbutton.config(fg="green"))
        addbutton.bind("<FocusOut>",lambda e:addbutton.config(fg="black"))
        addbutton.place(x=70,y=120)
        
        updatebutton=Button(sideframe,text="Update",font="Arial 10 bold",width=15,height=2,command=Update)
        updatebutton.bind("<FocusIn>",lambda e:updatebutton.config(fg="green"))
        updatebutton.bind("<FocusOut>",lambda e:updatebutton.config(fg="black"))
        updatebutton.place(x=70,y=170)
        
        deletebutton=Button(sideframe,text="Delete",font="Arial 10 bold",width=15,height=2)
        deletebutton.bind("<FocusIn>",lambda e:deletebutton.config(fg="green"))
        deletebutton.bind("<FocusOut>",lambda e:deletebutton.config(fg="black"))
        deletebutton.place(x=70,y=220)
        canclebutton=Button(sideframe,text="X",bg="red",fg="white",padx=5,command=cancle)
        canclebutton.place(x=220,y=0)
        
        date=datetime.date.today()
        datestr=str(date)
        Datestr=datestr.split("-")
        dates=Datestr[: : -1]
        d="-".join(dates)
        
        day=datetime.datetime.now().strftime("%A")
        dayLabel=Label(sideframe,text=f'{day},',font=(
            "Times New Roman", 10, "bold"),bg="lightgray")
        dayLabel.place(x=90,y=570)
        dateLabel=Label(sideframe,text=d,font=(
            "Times New Roman", 10, "bold"),bg="lightgray")
        dateLabel.place(x=150,y=570)
        
# ===================================******Search*******=====================        
    def search():
        def cancel():
            search_frame.destroy()
            frame.destroy()
            frame2.destroy()
            frame3.destroy()
        from test22 import getbyusn, getbyname
        search_frame=Frame(window,width=1100,height=610,bg="#E0E0EE",highlightbackground="skyblue",highlightthickness=3,highlightcolor="cyan")
        search_frame.place(x=5,y=50)
        frame = Frame(search_frame, width=400, height=550,bg="#E0E0EE")
        frame.place(x=0, y=50)
        frame2 = Frame(window, width=1098, height=50,bg="skyblue",relief=RAISED,highlightbackground="skyblue",highlightthickness=3,highlightcolor="cyan")
        frame2.place(x=5, y=50)
        frame3=Frame(search_frame,width=645,height=550,bg="#E0E0EE",highlightbackground="green",highlightcolor="cyan",highlightthickness=2)
        frame3.place(x=450,y=50)
        label1=Label(frame2,text="Search Student Information By Name",font="Arial 12 bold",bg="skyblue")
        label1.place(x=70,y=8)
        # ------------Buttons-----------------
        def detail(int,data):
            if int == 0:
                usn = data[0][1]
                # print(usn)
            elif int == 1:
                usn = data[1][1]
                # print(usn)
            elif int == 2:
                usn = data[2][1]
                # print(usn)
            elif int == 3:
                usn = data[3][1]
                # print(usn)
            elif int == 4:
                usn = data[4][1]
                # print(usn)
            elif int == 5:
                usn = data[5][1]
            elif int == 6:
                usn = data[6][1]
                # print(usn)
            elif int == 7:
                usn = data[7][1]
                # print(usn)
            elif int == 8:
                usn = data[8][1]
                # print(usn)
            elif int == 9:
                usn = data[9][1]
                # print(usn)
            else:
                pass
            from accessing import Access_institution_details
            data=Access_institution_details(usn.upper())
            # print(data)
            Usn.set(data[0][0])
            UsnEntry.update()
            name.set(data[0][1])
            nameEntry.update()
            phone.set(data[0][2])
            phoneEntry.update()
            Branch.set(data[0][3])
            BranchEntry.update()
            DOB.set(data[0][4])
            DOBEntry.update()
            Sem.set(data[0][5])
            SemEntry.update()
            Quota.set(data[0][6])
            QuotaEntry.update()
            Gender.set(data[0][7])
            GenderEntry.update()
            Domicile.set(data[0][8])
            DomicileEntry.update()
            Physical1.set(data[0][9])
            PhysicalEntry.update()
            Medium1.set(data[0][10])
            MediumEntry.update()
            Schooler1.set(data[0][11])
            SchoolerEntry.update()
            AdmissionYear1.set(data[0][12])
            AdmissionYearEntry.update()

        def guess(sort):
            try:
                for widgets in frame.winfo_children():
                    widgets.destroy()
            except:""
            if sort == []:
                pass
            else:
                total_rows = len(sort)
                total_columns = len(sort[0])

                p = Button(frame, text=">>>>>>>", width=10, fg="Green", font=('Arial', 8, 'bold'), relief=FLAT,
                        command=lambda: detail(0,sort),bg="#E0E0EE")
                p.grid(row=0, column=4)
                p1 = Button(frame, text=">>>>>>>", width=10, fg="Green", font=('Arial', 8, 'bold'), relief=FLAT,
                            command=lambda: detail(1,sort),bg="#E0E0EE")
                p1.grid(row=1, column=4)
                p2 = Button(frame, text=">>>>>>>", width=10, fg="Green", font=('Arial', 8, 'bold'), relief=FLAT,
                            command=lambda: detail(2,sort),bg="#E0E0EE")
                p2.grid(row=2, column=4)
                p3 = Button(frame, text=">>>>>>>", width=10, fg="Green", font=('Arial', 8, 'bold'), relief=FLAT,
                            command=lambda: detail(3,sort),bg="#E0E0EE")
                p3.grid(row=3, column=4)
                p4 = Button(frame, text=">>>>>>>", width=10, fg="Green", font=('Arial', 8, 'bold'), relief=FLAT,
                            command=lambda: detail(4,sort),bg="#E0E0EE")
                p4.grid(row=4, column=4)
                p5 = Button(frame, text=">>>>>>>", width=10, fg="Green", font=('Arial', 8, 'bold'), relief=FLAT,
                            command=lambda: detail(5,sort),bg="#E0E0EE")
                p5.grid(row=5, column=4)
                p6 = Button(frame, text=">>>>>>>", width=10, fg="Green", font=('Arial', 8, 'bold'), relief=FLAT,
                            command=lambda: detail(6,sort),bg="#E0E0EE")
                p6.grid(row=6, column=4)
                p7 = Button(frame, text=">>>>>>>", width=10, fg="Green", font=('Arial', 8, 'bold'), relief=FLAT,
                            command=lambda: detail(7,sort),bg="#E0E0EE")
                p7.grid(row=7, column=4)
                p8 = Button(frame, text=">>>>>>>", width=10, fg="Green", font=('Arial', 8, 'bold'), relief=FLAT,
                            command=lambda: detail(8,sort),bg="#E0E0EE")
                p8.grid(row=8, column=4)
                p9 = Button(frame, text=">>>>>>>", width=10, fg="Green", font=('Arial', 8, 'bold'), relief=FLAT,
                            command=lambda: detail(9,sort),bg="#E0E0EE")
                p9.grid(row=9, column=4)
                
                if total_rows == 0:
                    p.destroy()
                    p1.destroy()
                    p2.destroy()
                    p3.destroy()
                    p4.destroy()
                    p5.destroy()
                    p6.destroy()
                    p7.destroy()
                    p8.destroy()
                    p9.destroy()
                elif total_rows == 1:
                    p1.destroy()
                    p2.destroy()
                    p3.destroy()
                    p4.destroy()
                    p5.destroy()
                    p6.destroy()
                    p7.destroy()
                    p8.destroy()
                    p9.destroy()
                elif total_rows == 2:
                    p2.destroy()
                    p3.destroy()
                    p4.destroy()
                    p5.destroy()
                    p6.destroy()
                    p7.destroy()
                    p8.destroy()
                    p9.destroy()
                elif total_rows == 3:
                    p3.destroy()
                    p4.destroy()
                    p5.destroy()
                    p6.destroy()
                    p7.destroy()
                    p8.destroy()
                    p9.destroy()
                elif total_rows == 4:
                    p4.destroy()
                    p5.destroy()
                    p6.destroy()
                    p7.destroy()
                    p8.destroy()
                    p9.destroy()
                elif total_rows == 5:
                    p5.destroy()
                    p6.destroy()
                    p7.destroy()
                    p8.destroy()
                    p9.destroy()
                elif total_rows==6:
                    p6.destroy()
                    p7.destroy()
                    p8.destroy()
                    p9.destroy()
                elif total_rows==7:
                    p7.destroy()
                    p8.destroy()
                    p9.destroy()
                elif total_rows==8:
                    p8.destroy()
                    p9.destroy()
                elif total_rows==9:
                    p9.destroy()
                
                else:
                    pass
                for i in range(total_rows):
                    f = 3
                    for j in range(total_columns):
                        if f > 25:
                            f = 20
                        else:
                            pass
                        e = Label(frame, width=10,fg='blue', font=('Arial', 8, 'bold'),bg="#E0E0EE")
                        e.grid(row=i, column=j)
                        e.config(text=sort[i][j])
                        f = f + 20
        def ls():
            try:
                def key_press(e):
                    entry.after(2000, ls)
                    name = nm.get()
                    lst = []
                    j = 0
                    if name == "":
                        pass
                    else:
                        data = getbyname(name)
                        for i in data:
                            sort = i[:][:-11]
                            tup = (j + 1,) + sort[::1]
                            tup=list(tup)
                            tup1=tup[2].split(" ")
                            tup[2]=tup1[0]
                            # print(tup)
                            lst.insert(j, tup)
                            j += 1
                        guess(lst)
            except:""
            window.bind('<KeyPress>', key_press)
        nm = StringVar()
        entry = Entry(frame2, textvariable=nm, width=30, font=('Arial', 16, 'bold'),bg="lightgray")
        entry.place(x=400,y=10)
        def student():
            cancel()
            Student_details()
        label=Label(frame3,text="Student Information",font="Arial 15 bold",fg="red",bg="skyblue",relief=RAISED,padx=50)
        label.place(x=180,y=10)
        name = StringVar()
        name.set("")
        namevar = Label(frame3, text="Student Name      ",
                        font=("Arial 11 bold"),bg="#E0E0EE")
        namevar.place(x=20, y=75)
        nameEntry = Label(frame3, font=(
            "Arial 9 bold"),bg="#E0E0EE",textvariable=name)
        nameEntry.place(x=155, y=77)

        Usn = StringVar()
        Usn.set("")
        Usnvar = Label(frame3,text="Student USN        ",
                        font=("Arial 11 bold"), bg="#E0E0EE")
        Usnvar.place(x=20, y=105)
        UsnEntry = Label(frame3, font=(
            "Arial 9 bold"),bg="#E0E0EE",textvariable=Usn)
        UsnEntry.place(x=155, y=105)

        phone = StringVar()
        phone.set("")
        phonevar = Label(frame3, text="Phone Number     ",
                            font=("Arial 11 bold"), bg="#E0E0EE")
        phonevar.place(x=20, y=135)
        phoneEntry = Label(frame3, font=(
            "Arial 9 bold"),bg="#E0E0EE",textvariable=phone)
        phoneEntry.place(x=155, y=135)

        Branch = StringVar()
        Branch.set("")
        Branchvar = Label(frame3, text="Branch",
                        font=("Arial 11 bold"), bg="#E0E0EE")
        Branchvar.place(x=20, y=165)
        BranchEntry =Label(frame3, font=(
            "Arial 9 bold"),bg="#E0E0EE",textvariable=Branch)
        BranchEntry.place(x=155, y=165)

        DOB = StringVar()
        DOB.set("")
        DOBvar = Label(frame3, text="Date Of Birth",
                        font=("Arial 11 bold"), bg="#E0E0EE")
        DOBvar.place(x=20, y=195)
        DOBEntry = Label(frame3, font=(
            "Arial 9 bold"),bg="#E0E0EE",textvariable=DOB)
        DOBEntry.place(x=155, y=195)

        Sem = IntVar()
        Sem.set("")
        Semvar = Label(frame3, text="Semester",
                    font=("Arial 11 bold"), bg="#E0E0EE")
        Semvar.place(x=20, y=225)
        SemEntry = Label(frame3, font=(
            "Arial 9 bold"),bg="#E0E0EE",textvariable=Sem)
        SemEntry.place(x=155, y=225)

        Quota = StringVar()
        Quota.set("")
        Quotavar = Label(frame3, text="Admission Quota",
                    font=("Arial 11 bold"), bg="#E0E0EE")
        Quotavar.place(x=20, y=255)
        QuotaEntry = Label(frame3, font=(
            "Arial 9 bold"),bg="#E0E0EE",textvariable=Quota)
        QuotaEntry.place(x=155, y=255)

        Gender = StringVar()
        Gender.set("")
        Gendervar = Label(frame3, text="Gender",
                    font=("Arial 11 bold"), bg="#E0E0EE")
        Gendervar.place(x=20, y=285)
        GenderEntry = Label(frame3, font=(
            "Arial 9 bold"),bg="#E0E0EE",textvariable=Gender)
        GenderEntry.place(x=155, y=285)

        Domicile = StringVar()
        Domicile.set("")
        Domicilevar = Label(frame3, text="Domicile",
                    font=("Arial 11 bold"), bg="#E0E0EE")
        Domicilevar.place(x=20, y=315)
        DomicileEntry = Label(frame3, font=(
            "Arial 9 bold"),bg="#E0E0EE",textvariable=Domicile)
        DomicileEntry.place(x=155, y=315)

        Physical1 = StringVar()
        Physical1.set("")
        Physical = Label(frame3, text='''Handicapped''',
                        font=("Arial 11 bold"), bg="#E0E0EE")
        Physical.place(x=20, y=345)
        PhysicalEntry = Label(frame3, font=(
            "Arial 9 bold"),bg="#E0E0EE",textvariable=Physical1)
        PhysicalEntry.place(x=155, y=345)

        Medium1 = StringVar()
        Medium1.set("")
        Medium = Label(frame3, text='''Medium of 
Education''',
                        font=("Arial 11 bold"), bg="#E0E0EE")
        Medium.place(x=20, y=375)
        MediumEntry = Label(frame3, font=(
            "Arial 9 bold"),bg="#E0E0EE",textvariable=Medium1)
        MediumEntry.place(x=155, y=375)

        Schooler1 = StringVar()
        Schooler1.set("")
        Schooler = Label(frame3, text='''Hosteller/
Dayschooler''',
                        font=("Arial 11 bold"), bg="#E0E0EE")
        Schooler.place(x=10, y=423)
        SchoolerEntry = Label(frame3, font=(
            "Arial 9 bold"),bg="#E0E0EE",textvariable=Schooler1)
        SchoolerEntry.place(x=155, y=423)

        AdmissionYear1 = IntVar()
        AdmissionYear1.set("")
        AdmissionYear = Label(frame3, text='''Year of 
Admission''',
                        font=("Arial 11 bold"), bg="#E0E0EE")
        AdmissionYear.place(x=10, y=470)
        AdmissionYearEntry = Label(frame3, font=(
            "Arial 9 bold"),bg="#E0E0EE",textvariable=AdmissionYear1)
        AdmissionYearEntry.place(x=155, y=470)
        cancelbutton=Button(frame2,text="X",bg="red",fg="black",height=1,width=2,font="Arial 12 bold",command=cancel)
        cancelbutton.place(x=1060,y=0)
        editbutton=Button(frame3,text="Edit",font="Arial 10 bold",bg="green",padx=10,command=student)
        editbutton.place(x=500,y=500)
        ls()
# =============================================================
    def Export():
        import tkinter.messagebox as msg
        exportfram=Frame(window,width="500",height=200,bg="lightgreen",relief=RAISED,highlightbackground="cyan",highlightcolor="red",highlightthickness=3)
        exportfram.place(x=200,y=100)
        
        def add():
                
            if select.get()=="" and branch.get()=="":
                msg.showwarning("warning","Please Please Select Branch and semester")
            else:
                try:
                    data=mysql.connector.connect(host='localhost',user="root",password="guru8296jadhav@",database="student_information")
                    cur=data.cursor(buffered=True)
                    s=f"SELECT * FROM institution_details WHERE branch='{branch.get()}' AND sem={select.get()} ORDER BY USN"
                    path=os.path.abspath(__file__)
                    newFolder='studentDetails'
                    try:
                        if not os.path.exists(newFolder):
                            os.makedirs(newFolder)
                    except:""
                    df=pd.read_sql(sql=s,con=data)
                    df.to_excel(f"studentDetails\{select.get()} sem {branch.get()}.xlsx",index=False)
                    msg.showinfo("Export","Export Successfully")
                except:""       
            
        def cancel1():
            exportfram.destroy()   
        label=Label(exportfram,text="Exporting Data",font="Arial 15 bold",bg="cyan",padx=120,relief=RAISED)
        label.place(x=60,y=5)
        branch=StringVar()
        branch.set("")
        branchvalues=["Computer Science","Electronics and Communication","Robotics","Mechanical"]
        branchentry=ttk.Combobox(exportfram,textvariable=branch,width=28,font="Arial 10 bold",values=branchvalues)
        branchentry.place(x=70,y=75)
        
        label1=Label(exportfram,text="Brach",font="Arial 10 bold",bg="lightgreen",fg="red")
        label1.place(x=140,y=50)
        
        label2=Label(exportfram,text="Semester",font="Arial 10 bold",bg="lightgreen",fg="red")
        label2.place(x=350,y=50)

        btn=Button(exportfram,text="Export",font="Arial 10 bold",width=8,command=add,relief=RAISED)
        btn.place(x=180,y=125)
        values=[1,2,3,4,5,6,7,8]
        select=StringVar()
        box=ttk.Combobox(exportfram,textvariable=select,values=values,width=8)
        box.place(x=350,y=75)
        
        cancel=Button(exportfram,text="Cancel",font="Arial 10 bold",width=8,command=cancel1,relief=RAISED)
        cancel.place(x=260,y=125)
        
         #   Home_section
    def Home_section():
        for widgets in frame2.winfo_children():
            widgets.destroy()
        head = Frame(window)
        head.place(x=0,y=0)
        label = Label(head, text="Student Management System  ", font=(
                "Times New Roman", 20, "bold"), bg="skyblue", fg="black")
        label.pack(ipadx=510, ipady=2)
        global frame3,frame4,frame5,frame6
        frame3=Frame(window,width=140,height=25)
        frame3.place(x=1200,y=50)

        frame4=Frame(window,width=140,height=25)
        frame4.place(x=1200,y=80)
        
        frame5=Frame(window,width=140,height=25)
        frame5.place(x=1200,y=110)
        
        frame6=Frame(window,width=140,height=25)
        frame6.place(x=1200,y=140)
        
        regbutton=Button(frame3,text="Student Registration",font="Arial 10 bold",relief=FLAT,fg="black",bg="skyblue",command=register)
        regbutton.place(x=0,y=0)

        attendencebutton=Button(frame4,text="Student Attendence  ",font="Arial 10 bold",relief=FLAT,fg="black",bg="skyblue",command=attend)
        attendencebutton.place(x=0,y=0)
        
        resultbutton=Button(frame5,text="     Student Results    ",font="Arial 10 bold",relief=FLAT,fg="black",bg="skyblue",command=exam)
        resultbutton.place(x=0,y=0)
        
        searchbutton=Button(frame6,text="          Search           ",font="Arial 10 bold",relief=FLAT,fg="black",bg="skyblue",command=search)
        searchbutton.place(x=0,y=0)
        # IMAGE=os.path.abspath("CollegePhoto.png")
        collegeLogo = Image.open(r"C:\Users\User\Desktop\Student_Management\CollegePhoto.png")
        clgLogo = ImageTk.PhotoImage(collegeLogo)
        collegeLogoLable = Label(frame2, image=clgLogo, bg="white")
        collegeLogoLable.image = clgLogo
        collegeLogoLable.place(x=0, y=0)
    Home_section()
# ===================================================================================
                    #   Restart
    def RST():
        import os
        import sys
        os.execl(sys.executable,os.path.abspath(__file__),*sys.argv)
        
    def Exit():
        window.destroy()
        
    def Export_attendence():
        from test25 import getatten

        data = getatten()   # get attendance data
        j = tuple()
        for i in data:
            j = ("USN",) + i[1::3] + ("Average",)
        attendance = pd.DataFrame(columns=j)   #initialize attendence datagram

        info = []
        for i in data:
            info.clear()
            info.insert(0, i[0])
            a = i[3::3]  # attended classes
            b = i[2::3]  # total classes
            k = 0
            for j in a:
                tup = str(j) + "/" + str(b[k])
                info.append(tup)            #info is single list of single student
                k += 1
            #average value
            sum_attended,sum_total = 0,0
            for m in a:
                sum_attended = m + sum_attended
            for n in b:
                sum_total = n + sum_total
            average = (sum_attended/sum_total)*100
            info.append(round(average,2))
            attendance.loc[len(attendance)] = info
            path=os.path.abspath(__file__)
            NewFolder='studentAttendence'
            try:
                if not os.path.exists(NewFolder):
                    os.makedirs(NewFolder)
            except:""

        # print(attendance)
        attendance.to_excel(f"{NewFolder}\Attendence.xlsx", index=False)
        msg.showinfo("Export","Export Attendence Successfully")
        
# ================================================================================
                    #    Menubar
    menubar=Menu(window)
    Home=Menu(menubar,tearoff=0,bg="lightgray",relief=SUNKEN)
    menubar.add_cascade(label="Home",menu=Home)
    Home.add_command(label="        Home         ",font=("Arial",10,"bold"),command=Home_section)
    Home.add_cascade(label="        Register     ",font=("Arial",10,"bold"),command=register)
    Home.add_cascade(label="        Search       ",font="Arial 10 bold",command=search)
    Home.add_separator()
    Home.add_cascade(label="        Export Data  ",font="Arial 10 bold",command=Export)
    Home.add_cascade(label="        Export Attendence  ",font="Arial 10 bold",command=Export_attendence)
    Home.add_separator()
    Home.add_cascade(label="        Restart      ",font=("Arial",10,"bold"),command=RST)
    Home.add_cascade(label="        Exit         ",font=("Arial",10,"bold"),command=Exit)

    state="active"
    details=Menu(menubar,tearoff=0,bg="lightgray",relief=SUNKEN)
    menubar.add_cascade(label="Details",menu=details,state=state)
    details.add_command(label="       Student Details       ",font=("Arial",10,"bold"),command=Student_details,state=state)
    # details.add_separator()
    details.add_command(label="       Examination       ",font=("Arial",10,"bold"),state=state,command=exam)
    details.add_separator()
    details.add_command(label="       Account Section       ",font=("Arial",10,"bold"),state=state)
    details.add_separator()
    details.add_command(label="       Acadamic Details       ",font=("Arial",10,"bold"),state=state)
    details.add_separator()
    Login=Menu(menubar,tearoff=0)

    About=Menu(menubar,tearoff=0,bg="lightgray",relief=SUNKEN)
    menubar.add_cascade(label="About",menu=About)
    About.add_command(label="        College Details        ",font=("Arial",10,"bold"))
    About.add_command(label="        Staff Members       ",font=("Arial",10,"bold"))
    Help=Menu(menubar,tearoff=0)
    menubar.add_cascade(label="Help",menu=Help)
    window.config(menu=menubar)
    window.mainloop()
Restart()