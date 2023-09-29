from tkinter import *
from tkinter import ttk

win = Tk()
win.geometry("1366x768")
win.minsize(1366, 768)
win.maxsize(1366, 768)

#info cha frame  change kar  win -> frame2
info = Frame(win, width=700, height=700, bg="#E8E8E8", highlightbackground="black", highlightthickness=2)
info.place(x=300, y=30)


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
fnameEntry.place(x=392, y=95)

usn = StringVar()
usnlabel = Label(info, text="USN",
                 font="Arial 15 bold", bg="#E8E8E8", fg="#003153")
usnlabel.place(x=50, y=150)
usnEntry = Entry(info, width=20, textvariable=usn, font="Arial 15 bold", bd=1,
                 bg="#E8E8E8", highlightcolor="#0f5289", highlightbackground="black", highlightthickness=1, relief=FLAT)
usnEntry.place(x=60, y=185)

Branch = StringVar()
branchlabel = Label(info, text="Branch",
                    font="Arial 15 bold", bg="#E8E8E8", fg="#003153")
branchlabel.place(x=380, y=150)
BranchEntry = Entry(info, textvariable=Branch, width=20, font="Arial 15 bold", bd=1,
                    bg="#E8E8E8", highlightcolor="#0f5289", highlightbackground="black", highlightthickness=1,
                    relief=FLAT)
BranchEntry.place(x=392, y=185)

phone = StringVar()
phonelabel = Label(info, text="Mobile No.",
                   font="Arial 15 bold", bg="#E8E8E8", fg="#003153")
phonelabel.place(x=50, y=240)
phoneEntry = Entry(info, width=20, textvariable=phone, font="Arial 15 bold", bd=1,
                   bg="#E8E8E8", highlightcolor="#0f5289", highlightbackground="black", highlightthickness=1,
                   relief=FLAT)
phoneEntry.place(x=60, y=275)

fphone = StringVar()
fphonelabel = Label(info, text="Father's Mobile No.",
                    font=("Arial 15 bold"), bg="#E8E8E8", fg="#003153")
fphonelabel.place(x=380, y=240)
fphoneEntry = Entry(info, width=20, textvariable=fphone, font="Arial 15 bold", bd=1,
                    bg="#E8E8E8", highlightcolor="#0f5289", highlightbackground="black", highlightthickness=1,
                    relief=FLAT)
fphoneEntry.place(x=392, y=275)

sem = StringVar()
semlabel = Label(info, text="Semester",
                 font="Arial 15 bold", bg="#E8E8E8", fg="#003153")
semlabel.place(x=50, y=330)
semEntry = Entry(info, width=20, textvariable=sem, font="Arial 15 bold", bd=1,
                 bg="#E8E8E8", highlightcolor="#0f5289", highlightbackground="black", highlightthickness=1, relief=FLAT)
semEntry.place(x=60, y=365)

gender = StringVar()
genderlabel = Label(info, text="Gender",
                    font="Arial 15 bold", bg="#E8E8E8", fg="#003153")
genderlabel.place(x=380, y=330)
genderEntry = Entry(info, width=20, textvariable=gender, font="Arial 15 bold", bd=1,
                    bg="#E8E8E8", highlightcolor="#0f5289", highlightbackground="black", highlightthickness=1,
                    relief=FLAT)
genderEntry.place(x=392, y=365)

email = StringVar()
emailabel = Label(info, text="Email Address",
                  font=("Arial 15 bold"), bg="#E8E8E8", fg="#003153")
emailabel.place(x=50, y=420)
emailEntry = Entry(info, width=35, textvariable=email, font="Arial 15 bold", bd=1,
                   bg="#E8E8E8", highlightcolor="#0f5289", highlightbackground="black", highlightthickness=1,
                   relief=FLAT)
emailEntry.place(x=60, y=455)

addr = StringVar()
addrlabel = Label(info, text="Address",
                  font=("Arial 15 bold"), bg="#E8E8E8", fg="#003153")
addrlabel.place(x=50, y=510)
addrEntry = Entry(info, width=40, textvariable=addr, font="Arial 15 bold", bd=1,
                  bg="#E8E8E8", highlightcolor="#0f5289", highlightbackground="black", highlightthickness=1,
                  relief=FLAT)
addrEntry.place(x=60, y=545)


def xxx():
    pass

#0e4c94
button = Button(info, width=27, text="SUBMIT", bg="#E8E8E8", fg="#003153", bd=0, font="Arial 15 bold",
                command=xxx, highlightcolor="#003153", highlightthickness=1)
button.place(x=180, y=610)

win.mainloop()
