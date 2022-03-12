from tkinter import *
from openpyxl import load_workbook
from PIL import ImageTk, Image
book=load_workbook("my_data.xlsx")

sheet=book.active
sheet['A1']='NAME'
sheet['B1']='ADDRESS'
sheet['C1']='PHONE'
sheet['D1']='DOB'
sheet['E1']='PASSWORD'
global window,window1,window2,window3
book.save('my_data.xlsx')

window=Tk()

window.geometry("2000x2000")

window.title("Zoho")

window.configure(bg="white")
def fun3 ():
    window2=Tk()
    window2.title("zoho.com")
    window2.geometry("2000x2000")
    window2.configure(bg="white")
    lab1=Label(window2,text="Sign In",font=("boston",20),bg="white",fg="blue")
    lab1.pack()
    lab2=Label(window2,text="Don't have an account?",font=("garamond",20),bg="white",fg="black")
    lab2.place(x=400,y=100)
    
    lab3=Label(window2,text="Email",font=("garamond",20),fg="black")
    lab3.place(x=400,y=150)
    lab4=Label(window2,text="Password",font=("garamond",20),fg="black")
    lab4.place(x=400,y=250)
    ent=Entry(window2,width=25)
    ent.place(x=400,y=200)
    ent1=Entry(window2,width=25)
    ent1.place(x=400,y=300)
    btn4=Button(window2,text="🔒    Sign In",font=("bold",25),bg="blue",fg="white",command=fun1)
    btn4.place(x=400,y=400)
    btn3=Button(window2,text="Sign Up",font=("garamond",20),fg="blue",command=fun4)
    btn3.place(x=700,y=100)
def fun4 ():
    global et,et1,et2,enr3,window,window1,window2
    window3=Tk()
    window3.title("zoho.com")
    window3.geometry("2000x2000")
    window3.configure(bg="white")
    lab1=Label(window3,text="Sign Up",font=("boston",20),bg="white",fg="blue")
    lab1.pack()
    lab2=Label(window3,text="Already have an account?",font=("garamond",20),bg="white",fg="black")
    lab2.place(x=400,y=100)
    
    lab3=Label(window3,text="Email",font=("garamond",20),fg="black")
    lab3.place(x=400,y=150)
    lab4=Label(window3,text="Password",font=("garamond",20),fg="black")
    lab4.place(x=400,y=250)
    lab5=Label(window3,text="Secret",font=("garamond",20),fg="black")
    lab5.place(x=400,y=350)
    et=Entry(window3,width=25)
    et.place(x=400,y=200)
    et1=Entry(window3,width=25)
    et1.place(x=400,y=300)
    et2=Entry(window3,width=25)
    et2.place(x=400,y=400)
    btn4=Button(window3,text="🔒    Sign Up",font=("bold",25),bg="blue",fg="white",command=fun1)
    btn4.place(x=400,y=450)
    btn3=Button(window3,text="Sign In",font=("garamond",20),fg="blue",command=fun5)
    btn3.place(x=700,y=100)
    
def fun5():
    
       global et,et1,et2,enr3,window,window1,window2
       email=et.get()
       print(email)
       password=et1.get()
       print(password)
       secret=et2.get()
       print(secret)
      
       
   
       
def fun1():
    global enr,enr1,enr2,enr3,enr4,window1
    window1=Tk()
    window1.title("zoho.com")
    window1.geometry("2000x2000")
    window1.configure(bg="light green")

    lbl4=Label(window1,text="Enter your information",font=("segoe print",30),bg="green",fg="orange")
    lbl4.pack()
    lbl5=Label(window1,text="Name: ",font=("segoe print",20),bg="light green",fg="purple")
    lbl5.place(x=20,y=100)
    lbl6=Label(window1,text="Address:",font=("segoe print",20),bg="light green",fg="purple")
    lbl6.place(x=20,y=150)
    lbl7=Label(window1,text="phone: ",font=("segoe print",20),bg="light green",fg="purple")
    lbl7.place(x=20,y=200)
    lbl8=Label(window1,text="DOB:",font=("segoe print",20),bg="light green",fg="purple")
    lbl8.place(x=20,y=250)
    lbl9=Label(window1,text="password:",font=("segoe print",20),bg="light green",fg="purple")
    lbl9.place(x=20,y=300)
    enr=Entry(window1,width=25)
    enr.place(x=200,y=120)
    enr1=Entry(window1,width=25)
    enr1.place(x=200,y=170)
    enr2=Entry(window1,width=25)
    enr2.place(x=200,y=220)
    enr3=Entry(window1,width=25)
    enr3.place(x=200,y=270)
    enr4=Entry(window1,width=25,show="*")
    enr4.place(x=200,y=320)

    btn2=Button(window1,text="Register",font=("segoe print", 25),bg="light blue",fg="purple",command=fun2)
    btn2.place(x=150,y=350)
    
    
   
   
def fun2():
    
       global enr,enr1,enr2,enr3,enr4,window,window1,window2,window3
       name_data=enr.get()
       print(name_data)
       address_data=enr1.get()
       print(address_data)
       phone_data=enr2.get()
       print(phone_data)
       DOB_data=enr3.get()
       print(DOB_data)
       password_data=enr4.get()
       print(password_data)
   
       sheet.append([name_data,address_data,phone_data,DOB_data,password_data])
       
       book.save('my_data1.xlsx')
       window1.destroy()       
       window.destroy()
       
   



label1=Label(window,text="Z",font=("italic",40),bg="red",fg="white")
label1.place(x=420)
label1=Label(window,text="O",font=("italic",40),bg="green",fg="white")
label1.place(x=460,y=10)
label1=Label(window,text="H",font=("italic",40),bg="blue",fg="white")
label1.place(x=510)
label1=Label(window,text="O",font=("italic",40),bg="yellow",fg="white")
label1.place(x=555,y=10)
        

lbl2=Label(window,text="welcome",font=("segoe print",20),bg="orange",fg="blue")
lbl2.place(x=450,y=200)

lbl3=Label(window,text="everything for you",font=("segoe print",15),bg="blue",fg="red")
lbl3.place(x=700,y=100)
btn1=Button(window,text="Next",font=("segoe print", 25),bg="light blue",fg="green",command=fun3)
btn1.place(x=450,y=300)





window.mainloop()