from tkinter import*
from PIL import ImageTk
from tkinter import messagebox
class Login:
    def __init__(self,root):
        self.root=root
        self.root.title("Login Page")
        self.root.geometry("1199x600+100+50")
        self.root.resizable(False,False)
        #BG Image
        self.bg=ImageTk.PhotoImage(file=r"C:\Users\hp\Desktop\Login.py\login.png.jpg")
        self.bg_image=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)

        #Login Frame
        Frame_login=Frame(self.root,bg="white")
        Frame_login.place(x=150,y=150,height=340,width=500)

        title=Label(Frame_login, text="Login Form", font=("Impact", 35, "bold"), fg="#FF82AB", bg="white").place(x=90, y=30)
        desc=Label(Frame_login, text="Log in to your account", font=("Goudy old style", 15, "bold"), fg="#EE799F", bg="white").place(x=90, y=100)

        label_user=Label(Frame_login, text="Username", font=("Goudy old style", 15, "bold"), fg="gray", bg="white").place(x=90, y=140)
        self.txt_user=Entry(Frame_login, font=("times new roman", 15), bg="light gray")
        self.txt_user.place(x=90, y=170,width=350,height=35)

        label_pass=Label(Frame_login, text="Password", font=("Goudy old style", 15, "bold"), fg="gray", bg="white").place(x=90, y=210)
        self.txt_pass=Entry(Frame_login, font=("times new roman", 15), bg="light gray")
        self.txt_pass.place(x=90, y=240,width=350,height=35)

        forget_btn=Button(Frame_login, text="Forget Password", bg="white", fg="#FF82AB", bd=0, font=("times new roman", 12)).place(x=90, y=280)
        Login_btn=Button(self.root, command=self.login_function, text="Login", fg="white", bg="#FF82AB", bd=0, font=("times new roman", 20)).place(x=300, y=470, width=180, height=40)

    def login_function(self):
        if self.txt_pass.get()=="" or self.txt_user.get()=="":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        elif self.txt_pass.get()!="123456" or self.txt_user.get()!="Sakshi":
            messagebox.showerror("Error", "Invalid Username/Password", parent=self.root)
        else:
            messagebox.showinfo("Welcome", f"Welcome {self.txt_user.get()}\nYour Password: {self.txt_pass.get()}", parent=self.root)
root=Tk()
obj=Login(root)
root.mainloop()