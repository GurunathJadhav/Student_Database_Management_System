from tkinter import *
def Login():
    window = Tk()
    window.title("Login")
    window.geometry("500x500")
    window.configure(bg="#fff")
    window.resizable(False, False)


    def login():
        # return [username.get() ,password.get()]
        a=[username.get() ,password.get()]
        print(a)

    def signin():
        return

    # -------------------------------------------------------------
    frame = Frame(window, width=450, height=390, bg="#FFF",borderwidth=5,highlightbackground="blue",highlightthickness=5)
    frame.pack(pady=50)

    head = Label(frame, text="Login", fg="#57a1f8", bg="white", font=("Microsoft Yahei UI Light", 23, "bold"))
    head.place(x=175, y=5)

    # ----------------------------------------------------------
    def enter(e):
        user.delete(0, "end")
    def leave(e):
        if user.get() == "":
            user.insert(0, "Username")

    username=StringVar()
    username.set("")
    user = Entry(frame, textvariable=username,width=30, fg="black", bd=0, bg="white", font=("Microsoft Yahei UI Light", 11))
    user.place(x=105, y=70)
    user.insert(0, "Username")
    user.bind("<FocusIn>", enter)
    user.bind("<FocusOut>", leave)

    Frame(frame, width=250, height=2, bg="black").place(x=103, y=94)

    # ---------------------------------------------------------------

    def enter(e):
        passw.delete(0, "end")
    def leave(e):
        if passw.get() == "":
            passw.insert(0, "Password")

    password=StringVar()
    password.set("")
    passw = Entry(frame, textvariable=password,width=30, fg="black", bd=0, bg="white", font=("Microsoft Yahei UI Light", 11))
    passw.place(x=105, y=120)
    passw.insert(0, "Password")
    passw.bind("<FocusIn>", enter)
    passw.bind("<FocusOut>", leave)

    Frame(frame, width=250, height=2, bg="black").place(x=103, y=144)

    Button(frame, width=27, pady=5, text="Login", bg="#57a1f8", fg="white", bd=0, font=("Microsoft Yahei UI Light", 11), command=login,borderwidth=2,highlightbackground="black",highlightthickness=3).place(x=103, y=200)
    # label = Label(frame, text="Don't have an account?", fg="black", bg="white", font=("Microsoft Yahei UI Light", 9))
    # label.place(x=130, y=250)

    # signin = Button(frame, width=6, text="Sign in", bd=0, bg="white", cursor="hand2", fg="#57a1f8", font=("Microsoft Yahei UI Light", 9), command=signin )
    # signin.place(x=270, y=250)

    window.mainloop()
    
Login()
    
