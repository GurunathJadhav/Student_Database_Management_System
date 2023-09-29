# Python program to create a table
from test22 import getbyusn, getbyname
from tkinter import *

root = Tk()
root.geometry("1000x500")
root.resizable(False, False)

frame = Frame(root, width=800, height=700)
frame.place(x=0, y=50)
frame2 = Frame(root,width=800, height=50)
frame2.place(x=0,y=0)

global sort
def guess(sort):
    global e, p
    for widgets in frame.winfo_children():
        widgets.destroy()

    if sort == []:
        pass
    else:
        total_rows = len(sort)
        total_columns = len(sort[0])

        for i in range(total_rows):
            for j in range(total_columns):
                e = Label(frame, width=10, fg='blue', font=('Arial', 12, 'bold'))
                e.grid(row=i, column=j)
                e.config(text=sort[i][j]) 
                
            p = Button(frame, width=20, fg="Green", font=('Arial', 16, 'bold'), relief=FLAT)
            p.grid(row=i, column=j+1)
            p.config(text=">>>>>>>")
            p.config(command=detail)
  
def detail():
    try:
        from accessing import Access_institution_details_name,Access_institution_details
        if lst[0][0]==1:
            data=Access_institution_details(lst[0][1])
        elif lst[1][0]==2:
            data=Access_institution_details(lst[1][1])
        namedata=Access_institution_details_name(data[0][1])
        print(namedata)
    except:""
    for widgets in frame.winfo_children():
        widgets.destroy()

def ls():
    def key_press(e):
        entry.after(2000, ls)
        name = nm.get()
        global lst
        lst = []
        j = 0
        if name == "":
            pass
        else:
            data = getbyname(name)
            global tup
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

    root.bind('<KeyPress>', key_press)

nm = StringVar()
entry = Entry(frame2, textvariable=nm, width=50,font=('Arial',16, 'bold'))
entry.pack()
ls()


root.mainloop()