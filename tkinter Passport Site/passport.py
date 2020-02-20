from tkinter import *
from tkinter import messagebox as ms
from tkinter import ttk
import random
#import time
#import datetime
from PIL import ImageTk,Image
import sqlite3
import re

def main():
    root=Tk()
    app= Window1(root)




class Window1():
    def __init__(self,master):
        self.master=master
        self.master.config(bg="sky blue")
        self.master.title('Online Passport Application')
        self.master.geometry('1350x750+0+0')
        self.frame=Frame(self.master)
        self.frame.config(bg="sky blue")
        self.frame.pack()

        self.photo=Image.open('P_Seva.jpg')
        self.ph=ImageTk.PhotoImage(self.photo)
        self.label = Label(self.frame,text='Label',image=self.ph)
        self.label.photo=self.photo
        self.label.grid(row=0,column=0)

        
        self.LabelTitle=Label(self.frame,text='Passport Seva Online Portal',font=('algerian',34,'bold'),bd=20,bg="sky blue",fg="navy")
        self.LabelTitle.grid(row=0,column=1,columnspan=2,pady=20)
        
# Registration Button
        self.btnRegistration=Button(self.frame,text="New User ?\n Register ",
                                                                            command=self.Registration_Window,height=5,width=20,bg="purple2",fg="red4",font=('Times',15,'bold'))
        self.btnRegistration.grid(row=1,column=0)
# Login Button
        self.btnLogin=Button(self.frame,text="Login ",
                                                                            command=self.Login_Window,height=5,width=20,bg="purple2",fg="red4",font=('Times',15,'bold'))
        self.btnLogin.grid(row=1,column=1)
# Application Status Button
        self.btnStatus=Button(self.frame,text="Track Application Status ",
                                                                            command=self.Tracking_Window,height=5,width=20,bg="purple2",fg="red4",font=('Times',15,'bold'))
        self.btnStatus.grid(row=2,column=0)
#Appointment Button
        self.btnAppointment=Button(self.frame,text="Check Appointment \n Availability ",
                                                                            command=self.Appointment_Window,height=5,width=20,bg="purple2",fg="red4",font=('Times',15,'bold'))
        self.btnAppointment.grid(row=2,column=1)
#=====================================================================================================
    def Registration_Window(self):
        self.newWindow=Toplevel(self.master)
        self.app=Window2(self.newWindow)

    def Login_Window(self):
        self.newWindow=Toplevel(self.master)
        self.app=Window3(self.newWindow)

    def Tracking_Window(self):
        self.newWindow=Toplevel(self.master)
        self.app=Window4(self.newWindow)

    def Appointment_Window(self):
        self.newWindow=Toplevel(self.master)
        self.app=Window5(self.newWindow)  
#=====================================================================================================
#=====================================================================================================
class Window2():
    def __init__(self,master):
        self.master=master
        self.master.title('Applicant registration form')
        self.master.geometry('1350x750+0+0')
        self.frame=Frame(self.master)
        self.frame.pack()

        self.cboNameTablets=StringVar()
        self.name=StringVar()
        self.surname=StringVar()
        self.email=StringVar()
        self.password=StringVar()
        self.confirmpassword=StringVar()
        self.Ref=IntVar()
        self.birthdate=StringVar()
        #global phone
        self.phone=StringVar()
        #phone=self.phone.get
        
        self.Registerframe1 = Frame(self.frame,width=1100,height=600,bd=15,relief='ridge')
        self.Registerframe1.grid(row=1,column=0)
        self.Registerframe2 = Frame(self.frame,width=1000,height=100,bd=15,relief='ridge')
        self.Registerframe2.grid(row=2,column=0)

        #Office
        self.lblNameTablet = Label(self.Registerframe1, font=('arial',15,'bold'), text="Select Office Zone", padx=2,pady=2)
        self.lblNameTablet.grid(row=0, column=0, sticky=W)

        self.cboNameTablet = ttk.Combobox(self.Registerframe1, font=('arial',15,'bold'), state='readonly',textvariable=self.cboNameTablets,
                                          width = 20)
        self.cboNameTablet['value']=('','Mumbai','Delhi','Kolkata','Chennai','Jammu & Kashmir','Arunachal Pradesh','Andhra Pradesh') 
        self.cboNameTablet.current(0)
        self.cboNameTablet.grid(row=0, column=1)


    
        #Name
        self.lblname=Label(self.Registerframe1,text='Enter Name',font=('arial',15,'bold'),bd=20)
        self.lblname.grid(row=1,column=0)
        self.txtname=Entry(self.Registerframe1,font=('arial',15,'bold'),bd=10,textvariable=self.name)
        self.txtname.grid(row=1,column=1)
        #SurName
        self.lblsurname=Label(self.Registerframe1,text='Enter Surname',font=('arial',15,'bold'),bd=20)
        self.lblsurname.grid(row=2,column=0)
        self.txtsurname=Entry(self.Registerframe1,font=('arial',15,'bold'),bd=10,textvariable=self.surname)
        self.txtsurname.grid(row=2,column=1)
        #E-mail ID
        self.lblemail=Label(self.Registerframe1,text='Enter E-mail ID',font=('arial',15,'bold'),bd=20)
        self.lblemail.grid(row=3,column=0)
        self.txtemail=Entry(self.Registerframe1,font=('arial',15,'bold'),bd=10,textvariable=self.email)
        self.txtemail.grid(row=3,column=1)
        #Birth Date
        self.lblname=Label(self.Registerframe1,text='Enter Birthdate \n as DD/MM/YYYY',font=('arial',15,'bold'),bd=20)
        self.lblname.grid(row=3,column=2)
        self.txtname=Entry(self.Registerframe1,font=('arial',15,'bold'),bd=10,textvariable=self.birthdate)
        self.txtname.grid(row=3,column=3)
        #Phone no
        self.lblphone=Label(self.Registerframe1,text='Enter Phone No.',font=('arial',15,'bold'),bd=20)
        self.lblphone.grid(row=4,column=0)
        self.txtphone=Entry(self.Registerframe1,font=('arial',15,'bold'),bd=10,textvariable=self.phone)
        self.txtphone.grid(row=4,column=1)
                
        #Password
        self.lblpassword=Label(self.Registerframe1,text='Enter Password',font=('arial',15,'bold'),bd=20)
        self.lblpassword.grid(row=5,column=0)
        self.txtpassword=Entry(self.Registerframe1,font=('arial',15,'bold'),show='*',bd=10,textvariable=self.password)
        self.txtpassword.grid(row=5,column=1)
        #Confirm Password
        self.lblconfirmpassword=Label(self.Registerframe1,text='Confirm Password',font=('arial',15,'bold'),bd=20)
        self.lblconfirmpassword.grid(row=6,column=0)
        self.txtconfirmpassword=Entry(self.Registerframe1,font=('arial',15,'bold'),show='*',bd=10,textvariable=self.confirmpassword)
        self.txtconfirmpassword.grid(row=6,column=1)



                          
        self.btnRegister=Button(self.Registerframe2 ,text="Register ",width=25,font=('arial',10,'bold'),
                                                                            command=self.check_data,height=3)
        self.btnRegister.grid(row=0,column=0,pady=5,padx=10)
        self.btnRegister=Button(self.Registerframe2 ,text="Reset ",width=25,font=('arial',10,'bold'),
                                                                            command=self.Reset,height=3)
        self.btnRegister.grid(row=0,column=1,pady=5,padx=10)
        self.btnRegister=Button(self.Registerframe2 ,text="Exit ",width=25,font=('arial',10,'bold'),
                                                                            command=self.iexit,height=3)
        self.btnRegister.grid(row=0,column=2,pady=5,padx=10)
        self.btnRegister = Button(self.Registerframe2,text = "Get Login ID",width=25,font=('arial',10,'bold'),
                                     state = DISABLED,command = self.reg_2,height=3)#  state = DISABLED
        self.btnRegister.grid(row = 0, column = 4,pady=5,padx=10)

#=====================================================================================================
    def F_error(self):
        global screen1
        self.screen1 = Tk()
        self.screen1.geometry("150x90")
        self.screen1.title("Warning!")
        Label(self.screen1, text = "All fields required", fg = "red").pack()
        Button(self.screen1, text = "OK",command=self.screen1.destroy).pack()

    def PH_error(self):
        global screen2
        self.screen2= Tk()
        self.screen2.geometry("200x120")
        self.screen2.title("Warning!")
        Label(self.screen2, text = "Phone number already in used !! \n Try to Login with that number \n or\n Try with Another", fg = "red",font=('algerian',20)).pack()
        Button(self.screen2, text = "OK",command=self.screen2.destroy).pack()
        self.phone.set('')

    def PH_crct(self):
        self.screen5= Tk()
        self.screen5.geometry("200x120")
        self.screen5.title("Warning!")
        Label(self.screen5, text = "Please fill the Phone No. correctly" , fg = "red",font=('algerian',20)).pack()
        Button(self.screen5, text = "OK",command=self.screen5.destroy).pack()
        self.phone.set('')

    def E_crct(self):
        self.screen5= Tk()
        self.screen5.geometry("200x120")
        self.screen5.title("Warning!")
        Label(self.screen5, text = "Please fill the Email correctly" , fg = "red",font=('algerian',20)).pack()
        Button(self.screen5, text = "OK",command=self.screen5.destroy).pack()
        self.phone.set('')

    def protection(self):
        self.screen5= Tk()
        self.screen5.geometry("200x120")
        self.screen5.title("Warning!")
        Label(self.screen5, text = "Password doesn't match , \n try with correct password" , fg = "red",font=('algerian',20)).pack()
        Button(self.screen5, text = "OK",command=self.screen5.destroy).pack()
        self.confirmpassword.set('')

    def crct_birthdate(self):
        self.screen5= Tk()
        self.screen5.geometry("200x120")
        self.screen5.title("Warning!")
        Label(self.screen5, text = "Please Enter valid birthdate or correctly" , fg = "red",font=('algerian',20)).pack()
        Button(self.screen5, text = "OK",command=self.screen5.destroy).pack()
        self.confirmpassword.set('')

    def Register_success(self):
        global screen3
        self.screen3= Tk()
        self.screen3.geometry("500x170")
        self.screen3.title("Warning!")
        Label(self.screen3, text = "Registration succesfull \n click on \"Get Login ID \"for Login \n ", fg = "green",font=('algerian',20)).pack()
        Button(self.screen3, text = "OK",command=self.screen3.destroy,width=15).pack()

    def check_data(self):
        if (  (self.name.get())=='' or (self.surname.get())=='' or (self.email.get())=='' or
                           (self.birthdate.get())=='' or (self.phone.get())== '' or (self.password.get())=='' or (self.confirmpassword.get())==''):
            #ms.showerror('Error!','Please Enter all the necessary fields  !! .')
            print("No error")
            #self.Registration_Window()
            self.F_error()
        else:
            #print(self.name.get())

            m = "\d{10}"
            e = '[\w._%+-]{1,20}@[\w.-]{2,20}.[A-Za-z]{2,3}'
            b='\d{2}/\d{2}/\d{4}'
            print('ok')
            e1 = re.match(e,self.email.get())
            m1=re.match(m ,self.phone.get())
            b1=re.match(b,self.birthdate.get())

            if e1 :
                if m1:
                    if (self.password.get())==(self.confirmpassword.get()):
                        if b1:
                            self.database()
                        else:
                            self.crct_birthdate()
                    else:
                        self.protection()
                else:
                    flag = 0
                    self.PH_crct()
                    
            else:
                flag = 0
                self.E_crct()
   
    def database(self):
        self.Login_ID()
        # make database and users (if not exists already) table at programme start up
        with sqlite3.connect('start.db') as db:
            c = db.cursor()

        c.execute('''CREATE TABLE IF NOT EXISTS  startreg1(LOGIN_ID INT PRIMARY KEY NOT NULL,
                                                                                                                          OFFICE_ZONE  TEXT                  NOT NULL,
                                                                                                                           NAME                    TEXT                  NOT NULL,
                                                                                                                           SURNAME          TEXT                  NOT NULL,
                                                                                                                           EMAIL_ID            TEXT                  NOT NULL,
                                                                                                                           BIRTHDATE       TEXT                  NOT NULL,
                                                                                                                           PHONE_NO       TEXT                  NOT NULL,
                                                                                                                           PASSWORD      TEXT                 NOT NULL,
                                                                                                                           C_PASSWORD TEXT                 NOT NULL);''')
        
        insert = 'INSERT INTO startreg1(LOGIN_ID,OFFICE_ZONE,NAME,SURNAME,EMAIL_ID,BIRTHDATE,PHONE_NO,PASSWORD,C_PASSWORD) VALUES(?,?,?,?,?,?,?,?,?)'
        find_user = ('SELECT * FROM startreg1 WHERE PHONE_NO = ?')
        c.execute(find_user,[(self.phone.get())])        
        if c.fetchall():
            self.PH_error()
        else:        
            c.execute('INSERT INTO startreg1(LOGIN_ID,OFFICE_ZONE,NAME,SURNAME,EMAIL_ID,BIRTHDATE,PHONE_NO,PASSWORD,C_PASSWORD) VALUES(?,?,?,?,?,?,?,?,?)',
                          ((self.Ref.get()),(self.cboNameTablets.get()),(self.name.get()),(self.surname.get()),(self.email.get()),
                           (self.birthdate.get()),(self.phone.get()),(self.password.get()),(self.confirmpassword.get())))
            
            self.btnRegister.config(state = NORMAL)
            self.Register_success()
            db.commit()
            db.close()


    def Login_ID(self):
            Member_Ref=IntVar()
            x = random.randint(10903, 600873)
            randomRef = str(x)
            Member_Ref.set(randomRef)
            self.Ref.set(randomRef)
        
        

    def Reset(self):
        self.name.set('')
        self.surname.set('')
        self.email.set('')
        self.password.set('')
        self.confirmpassword.set('')
        self.txtname.focus()

    def iexit(self):
        self.exit = ms.askyesno('Exited ','Home')
        if self.exit>0:
            self.frame.destroy()
            return
    
    def Registration_Window(self):
        self.newWindow=Toplevel(self.master)
        self.app=Window2(self.newWindow)

    def Login_Window(self):
        self.newWindow=Toplevel(self.master)
        self.app=Window3(self.newWindow)

    def reg_2(self):
        self.master=Tk()
        self.master.title('Applicant registration form')
        self.master.geometry('1350x750+0+0')
        self.frame=Frame(self.master)
        self.frame.pack()

        self.Registerframe1 = Frame(self.frame,width=1100,height=600,bd=15,relief='ridge')
        self.Registerframe1.grid(row=1,column=0)
        self.Registerframe2 = Frame(self.frame,width=1000,height=100,bd=15,relief='ridge')
        self.Registerframe2.grid(row=2,column=0)
        with sqlite3.connect('start.db') as db:
            a = db.cursor()
        find_user = ('SELECT LOGIN_ID FROM startreg1 WHERE PHONE_NO = ?')
        a.execute(find_user,[(self.phone.get())])
        result=a.fetchall()
        if result:
            self.lblconfirmpassword=Label(self.Registerframe1,text=self.name.get()+'\n your login ID is \n',font=('arial',15,'bold'),bd=20)
            self.lblconfirmpassword.grid(row=1,column=0)
            self.lblconfirmpassword=Label(self.Registerframe1,text=result,font=('arial',15,'bold'),bd=20)
            self.lblconfirmpassword.grid(row=2,column=0)
            self.lblconfirmpassword=Label(self.Registerframe1,text=result,font=('arial',15,'bold'),bd=20)
            self.lblconfirmpassword.grid(row=2,column=0)

        else:
                print('error')

                      
                      

        self.btnRegister=Button(self.Registerframe2 ,text="OK ",width=25,font=('arial',10,'bold'),
                                                                            command=self.master.destroy,height=3)
        self.btnRegister.grid(row=0,column=0,pady=5,padx=10)
        
        
#=====================================================================================================
#=====================================================================================================
#===================================================================================================== 
    def Registration_Window(self):
        self.newWindow=Toplevel(self.master)
        self.app=Window2(self.newWindow)

    def Login_Window(self):
        self.newWindow=Toplevel(self.master)
        self.app=Window3(self.newWindow)

#=====================================================================================================
#=====================================================================================================
class Window3():
    def __init__(self,master):
        self.master=master
        self.master.title('Login')
        self.master.geometry('1350x750+0+0')
        self.frame=Frame(self.master,padx=10,pady=10)
        self.frame.pack()
        
#Useful variables

        
        self.l_logID=StringVar()
        self.l_password=StringVar()
        
        self.cboAply_for=StringVar()
        self.cboType_apln=StringVar()
        self.cboType_Book=StringVar()
        
        self.l_name=StringVar()
        self.l_surname=StringVar()
        self.cbo_gender=StringVar()
        self.cbo_IsIN=StringVar()
        self.l_Bplace=StringVar()
        self.cbo_state=StringVar()
        self.cbo_Marital=StringVar()
        self.cbo_ctzn=StringVar()
        self.l_pan=StringVar()
        self.l_voter=StringVar()
        self.cbo_GS=StringVar()
        self.cbo_emptype=StringVar()
        self.cbo_eduQ=StringVar()
        
        self.l_dob=StringVar()
        
        self.l_Fname=StringVar()
        self.l_Mname=StringVar()
        self.l_LGname=StringVar()
        
        
        
        


# Calling Fuinction
        self.page1()

    def page1(self):
        #self.frame.pack_forget()
        
        self.Registerframe1 = Frame(self.frame,width=1100,height=600,bd=15,relief='ridge')
        self.Registerframe1.grid(row=1,column=0)
        self.Registerframe2 = Frame(self.frame,width=1000,height=100,bd=15,relief='ridge')
        self.Registerframe2.grid(row=2,column=0)

        Label(self.Registerframe1 ,text = 'Login ',font = ('',30),pady=5,padx=5).grid(row=0,column=0)
        Label(self.Registerframe1 ,text = 'Login ID: ',font = ('',20),pady=5,padx=5).grid(row=1,column=0)
        Entry(self.Registerframe1 ,textvariable = self.l_logID,bd = 5,font = ('',15)).grid(row=1,column=1)      #self.l_logID
        Label(self.Registerframe1 ,text = 'Password: ',font = ('',20),pady=5,padx=5).grid(row=2,column=0)
        Entry(self.Registerframe1 ,textvariable = self.l_password,bd = 5,font = ('',15),show = '*').grid(row=2,column=1)      #self.l_password
        Button(self.Registerframe2,text = ' Next ',bd = 3 ,font = ('',15),padx=5,pady=5,command=self.login).grid(row=0,column=0)
        Button(self.Registerframe2,text = ' Home ',bd = 3 ,font = ('',15),padx=5,pady=5,command=self.Login_Window).grid(row=0,column=1)

    
    def page2(self):
        #self.frame.pack_forget()
        
        self.Registerframe1 = Frame(self.frame,width=1100,height=600,bd=15,relief='ridge')
        self.Registerframe1.grid(row=1,column=0)
        self.Registerframe2 = Frame(self.frame,width=1000,height=100,bd=15,relief='ridge')
        self.Registerframe2.grid(row=2,column=0)

        Label(self.Registerframe1 ,text = 'Passport Type  ',font = ('',30),pady=5,padx=5).grid(row=0,column=0)
        Label(self.Registerframe1 ,text = 'Applying for * ',font = ('',20),pady=5,padx=5).grid(row=1,column=0)
        self.cboNameTablet = ttk.Combobox(self.Registerframe1, font=('arial',15,'bold'), state='readonly',textvariable=self.cboAply_for,width = 20)     #self.cboAply_for
        self.cboNameTablet['value']=('','Fresh Passport','Re-issue of Passport') 
        self.cboNameTablet.current(0)
        self.cboNameTablet.grid(row=1, column=1)        
        Label(self.Registerframe1 ,text = 'Type of Application *',font = ('',20),pady=5,padx=5).grid(row=2,column=0)
        self.cboNameTablet = ttk.Combobox(self.Registerframe1, font=('arial',15,'bold'), state='readonly',textvariable=self.cboType_apln,width = 20)     #self.cboType_apln
        self.cboNameTablet['value']=('','Normal','Tatkal') 
        self.cboNameTablet.current(0)
        self.cboNameTablet.grid(row=2, column=1)
        Label(self.Registerframe1 ,text = 'Type of Passport Booklet *',font = ('',20),pady=5,padx=5).grid(row=3,column=0)
        self.cboNameTablet = ttk.Combobox(self.Registerframe1, font=('arial',15,'bold'), state='readonly',textvariable=self.cboType_Book,width = 20)    #self.cboType_Book
        self.cboNameTablet['value']=('','36 Pages','60 Pages') 
        self.cboNameTablet.current(0)
        self.cboNameTablet.grid(row=3, column=1)
        
        Button(self.Registerframe2,text = ' Next ',bd = 3 ,font = ('',15),padx=5,pady=5,command=self.Database_P2).grid(row=0,column=0)     
        Button(self.Registerframe2,text = ' Home ',bd = 3 ,font = ('',15),padx=5,pady=5,command=self.Login_Window).grid(row=0,column=1)

    def page3(self):
        self.Registerframe1 = Frame(self.frame,width=1100,height=600,bd=15,relief='ridge')
        self.Registerframe1.grid(row=1,column=0)
        self.Registerframe2 = Frame(self.frame,width=1000,height=100,bd=15,relief='ridge')
        self.Registerframe2.grid(row=2,column=0)


        Label(self.Registerframe1 ,text = 'Applicant Details ',font = ('',30),pady=5,padx=5).grid(row=0,column=0)
        
        Label(self.Registerframe1 ,text = '\tName *\n (as on identity proof ) ',font = ('',15),pady=3,padx=5).grid(row=1,column=0)
        Entry(self.Registerframe1 ,textvariable = self.l_name,bd = 5,font = ('',15)).grid(row=1,column=1)
        
        Label(self.Registerframe1 ,text = '\t Surname * ',font = ('',15),pady=3,padx=5).grid(row=1,column=2)
        Entry(self.Registerframe1 ,textvariable = self.l_surname,bd = 5,font = ('',15)).grid(row=1,column=3)
        
        Label(self.Registerframe1 ,text = '\t Gender * ',font = ('',15),pady=3,padx=5).grid(row=2,column=0)
        self.cboNameTablet = ttk.Combobox(self.Registerframe1, font=('arial',15,'bold'), state='readonly',textvariable=self.cbo_gender,width = 20)     
        self.cboNameTablet['value']=('','Male','Female','Transgender') 
        self.cboNameTablet.current(0)
        self.cboNameTablet.grid(row=2, column=1)
        
        Label(self.Registerframe1 ,text = '\t Date of Birth *',font = ('',15),pady=3,padx=5).grid(row=3,column=0)
        Entry(self.Registerframe1 ,textvariable = self.l_dob,bd = 5,font = ('',15)).grid(row=3,column=1)
        
        Label(self.Registerframe1 ,text = '\t Is your place of birth \n Out of India* ',font = ('',15),pady=3,padx=5).grid(row=4,column=0)
        self.cboNameTablet = ttk.Combobox(self.Registerframe1, font=('arial',15,'bold'), state='readonly',textvariable=self.cbo_IsIN,width = 20)     
        self.cboNameTablet['value']=('','Yes','No') 
        self.cboNameTablet.current(0)
        self.cboNameTablet.grid(row=4, column=1)   
        
        Label(self.Registerframe1 ,text = 'Place of birth* ',font = ('',15),pady=3,padx=5).grid(row=5,column=0)
        Entry(self.Registerframe1 ,textvariable = self.l_Bplace,bd = 5,font = ('',15)).grid(row=5,column=1)
        
        Label(self.Registerframe1 ,text = 'State *',font = ('',15),pady=3,padx=5).grid(row=6,column=0)
        self.cboNameTablet = ttk.Combobox(self.Registerframe1, font=('arial',15,'bold'), state='readonly',textvariable=self.cbo_state,width = 20)     
        self.cboNameTablet['value']=('','ENter state') 
        self.cboNameTablet.current(0)
        self.cboNameTablet.grid(row=6, column=1)
        
        Label(self.Registerframe1 ,text = 'Marital Status * ',font = ('',15),pady=3,padx=5).grid(row=7,column=0)
        self.cboNameTablet = ttk.Combobox(self.Registerframe1, font=('arial',15,'bold'), state='readonly',textvariable=self.cbo_Marital,width = 20) 
        self.cboNameTablet['value']=('','Single','Married','Widowed','Divorced') 
        self.cboNameTablet.current(0)
        self.cboNameTablet.grid(row=7, column=1)
        
        Label(self.Registerframe1 ,text = 'Citizenship of India by * ',font = ('',15),pady=3,padx=5).grid(row=8,column=0)
        self.cboNameTablet = ttk.Combobox(self.Registerframe1, font=('arial',15,'bold'), state='readonly',textvariable=self.cbo_ctzn,width = 20)  
        self.cboNameTablet['value']=('','Birth','Registration/ Naturalization','Descent') 
        self.cboNameTablet.current(0)
        self.cboNameTablet.grid(row=8, column=1)
        
        Label(self.Registerframe1 ,text = 'PAN ( if available) ',font = ('',15),pady=3,padx=5).grid(row=9,column=0)
        Entry(self.Registerframe1 ,textvariable = self.l_pan,bd = 5,font = ('',15)).grid(row=9,column=1)
        
        Label(self.Registerframe1 ,text = 'Voter ID ( if available) ',font = ('',15),pady=3,padx=5).grid(row=9,column=2)
        Entry(self.Registerframe1 ,textvariable = self.l_voter,bd = 5,font = ('',15)).grid(row=9,column=3)
        
        Label(self.Registerframe1 ,text = 'Employment Type ',font = ('',15),pady=3,padx=5).grid(row=10,column=0)
        self.cboNameTablet = ttk.Combobox(self.Registerframe1, font=('arial',15,'bold'), state='readonly',textvariable=self.cbo_emptype,width = 20)     
        self.cboNameTablet['value']=('','Government','PSU','Statutory body','Retired Government Servent','Private','HomeMaker','Not Employed','Student','Self-Employed','Others') 
        self.cboNameTablet.current(0)
        self.cboNameTablet.grid(row=10, column=1)

        Label(self.Registerframe1 ,text = 'Is either of your parent\(in case of minor\)/spouse \n a Government Servent ',font = ('',15),pady=3,padx=5).grid(row=11,column=0)
        self.cboNameTablet = ttk.Combobox(self.Registerframe1, font=('arial',15,'bold'), state='readonly',textvariable=self.cbo_GS,width = 20)    
        self.cboNameTablet['value']=('','Yes','No') 
        self.cboNameTablet.current(0)
        self.cboNameTablet.grid(row=11, column=1)

        Label(self.Registerframe1 ,text = 'Educational Qualification ',font = ('',15),pady=3,padx=5).grid(row=12,column=0)
        self.cboNameTablet = ttk.Combobox(self.Registerframe1, font=('arial',15,'bold'), state='readonly',textvariable=self.cbo_eduQ,width = 20)     
        self.cboNameTablet['value']=('','Graduate and Above','10 th Pass or Above','7 th Pass or Less','Between 8th and 9th') 
        self.cboNameTablet.current(0)
        self.cboNameTablet.grid(row=12, column=1)

        Button(self.Registerframe2,text = ' Home',bd = 3 ,font = ('',15),padx=5,pady=5,command=self.Login_Window).grid(row=0,column=0)
        Button(self.Registerframe2,text = ' Save my Data',bd = 3 ,font = ('',15),padx=5,pady=5,command=self.Database_P3).grid(row=0,column=1)
        self.btnpage3=Button(self.Registerframe2,text = ' Next ',state = DISABLED,bd = 3 ,font = ('',15),padx=5,pady=5,command=self.page4)
        self.btnpage3.grid(row=0,column=2)



    def login(self):
    	#Establish Connection
        with sqlite3.connect('start.db') as db:
            c = db.cursor()

        #Find user If there is any take proper action
        find_user = ('SELECT LOGIN_ID,PASSWORD  FROM startreg1 WHERE LOGIN_ID = ? and PASSWORD = ?')
        c.execute(find_user,[(self.l_logID.get()),(self.l_password.get())])
        result = c.fetchall()
        if result:
            self.page2()

        else:
            ms.showerror('Oops!','Username Not Found.')
    def Database_P2(self):
        # make database and users (if not exists already) table at programme start up
        with sqlite3.connect('start.db') as db:
            c = db.cursor()

        c.execute('''CREATE TABLE IF NOT EXISTS  startLOG2(APPLYING_FOR TEXT NOT NULL,
                                                                                                                          TYPE_OF_APPLICATION  TEXT                  NOT NULL,
                                                                                                                           TYPE_OF_PASSPORT_BOOKLET                  TEXT                  NOT NULL);''')
        print("Table is created")
        insert = 'INSERT INTO startLOG2(APPLYING_FOR,TYPE_OF_APPLICATION,TYPE_OF_PASSPORT_BOOKLET ) VALUES(?,?,?)'
        c.execute(insert,[(self.cboAply_for.get()),(self.cboType_apln.get()),(self.cboType_Book.get())])
        self.page3()
        db.commit()
        db.close()
        
        
    def Database_P3(self):
                # make database and users (if not exists already) table at programme start up
        with sqlite3.connect('start.db') as db:
            c = db.cursor()

        c.execute('''CREATE TABLE IF NOT EXISTS  startLOG3(NAME TEXT  NOT NULL,
                                                                                                                          SURNAME  TEXT                  NOT NULL,
                                                                                                                           GENDER                 TEXT                  NOT NULL,
                                                                                                                           DOB          TEXT                  NOT NULL,
                                                                                                                           InINDIA         TEXT                  NOT NULL,
                                                                                                                           BIRTHPLACE       TEXT                  NOT NULL,
                                                                                                                           STATE       TEXT                  NOT NULL,
                                                                                                                           MARITAL_STATUS      TEXT                 NOT NULL,
                                                                                                                           PAN_ID            TEXT                 NOT NULL,
                                                                                                                           VOTER_ID       TEXT                 NOT NULL,
                                                                                                                           EMP_TYPE                 TEXT                 NOT NULL,
                                                                                                                           ISGS              TEXT                 NOT NULL,
                                                                                                                           EDUCATIONAL_QUALIFICATION             TEXT                 NOT NULL);''')
        print("Table is created")
        insert = 'INSERT INTO startLOG3(NAME,SURNAME,GENDER,DOB,InINDIA,BIRTHPLACE,STATE,MARITAL_STATUS,PAN_ID,VOTER_ID,EMP_TYPE,ISGS,EDUCATIONAL_QUALIFICATION) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)'
        c.execute(insert,[(self.l_name.get()),(self.l_surname.get()),(self.cbo_gender.get()),(self.cbo_IsIN.get()),(self.l_Bplace.get()),
        (self.cbo_state.get()),(self.cbo_Marital.get()),(self.cbo_ctzn.get()),(self.l_pan.get()),(self.l_voter.get()),(self.cbo_GS.get()),(self.cbo_emptype.get()),(self.cbo_eduQ.get())])
        print('page 3 ok')
        self.btnpage3.config(state = NORMAL)
        db.commit()
        db.close()



        
    

    def page4(self):
        self.newWindow=Toplevel(self.master)
        self.app=page4(self.newWindow)

    def Registration_Window(self):
        self.newWindow=Toplevel(self.master)
        self.app=Window2(self.newWindow)

    def Login_Window(self):
        self.newWindow=Toplevel(self.master)
        self.app=Window3(self.newWindow)



class page4:
    def __init__(self,master):
        self.master=master
        self.master.title('Family Details')
        self.master.geometry('1350x750+0+0')
        self.frame=Frame(self.master)
        self.frame.pack()
        
        self.Registerframe1 = Frame(self.frame,width=1100,height=600,bd=15,relief='ridge')
        self.Registerframe1.grid(row=1,column=0)
        self.Registerframe2 = Frame(self.frame,width=1000,height=100,bd=15,relief='ridge')
        self.Registerframe2.grid(row=2,column=0)

        self.l_fname=StringVar()
        self.l_mname=StringVar()
        self.l_lgname=StringVar()


        Label(self.Registerframe1 ,text = 'Family Details  ',font = ('',30),pady=5,padx=5).grid(row=0,column=0)
        
        Label(self.Registerframe1 ,text = '** Please enter Father ,Mother or Legal Guardian Names as per applicable ',font = ('',10),pady=5,padx=5).grid(row=1,column=0)
        
        Label(self.Registerframe1 ,text = 'Father\' s Full Name',font = ('',20),pady=3,padx=5).grid(row=2,column=0)
        Entry(self.Registerframe1 ,textvariable = self.l_fname,bd = 5,font = ('',15)).grid(row=2,column=1)
        
        Label(self.Registerframe1 ,text = 'Mother\' s Full Name',font = ('',20),pady=3,padx=5).grid(row=3,column=0)
        Entry(self.Registerframe1 ,textvariable = self.l_mname,bd = 5,font = ('',15)).grid(row=3,column=1)
        
        Label(self.Registerframe1 ,text = 'Legal Guardian\' s Full Name',font = ('',20),pady=3,padx=5).grid(row=4,column=0)
        Entry(self.Registerframe1 ,textvariable = self.l_lgname,bd = 5,font = ('',15)).grid(row=4,column=1)

        Button(self.Registerframe2,text = ' Home',bd = 3 ,font = ('',20),padx=5,pady=5,command=self.Login_Window).grid(row=0,column=0)
        Button(self.Registerframe2,text = ' Save my Data',bd = 3 ,font = ('',20),padx=5,pady=5,command=self.Database_P4).grid(row=0,column=1)
        Button(self.Registerframe2,text = ' Next ',bd = 3 ,font = ('',20),padx=5,pady=5,command=self.page5).grid(row=0,column=2)



    def F_error(self):
        self.screen1 = Tk()
        self.screen1.geometry("150x90")
        self.screen1.title("Warning!")
        Label(self.screen1, text = "All fields required", fg = "red").pack()
        Button(self.screen1, text = "OK",command=self.screen1.destroy).pack()
    def Database_P4(self):
                # make database and users (if not exists already) table at programme start up
        with sqlite3.connect('start.db') as db:
            c = db.cursor()

        c.execute('''CREATE TABLE IF NOT EXISTS  startLOG4(FATHER_NAME TEXT  NOT NULL,
                                                                                                                          MOTHER_NAME  TEXT                  NOT NULL,
                                                                                                                         GUARDIAN_NAME                 TEXT                  NOT NULL);''')
        print("Table is created")
        insert = 'INSERT INTO startLOG4(FATHER_NAME,MOTHER_NAME,GUARDIAN_NAME) VALUES(?,?,?)'
        c.execute(insert,[(self.l_fname.get()),(self.l_mname.get()),(self.l_lgname.get())])
        print(self.l_fname.get())
        print('page 4 ok')
        db.commit()
        db.close()

    def page5(self):
        self.newWindow=Toplevel(self.master)
        self.app=page5(self.newWindow)

    def Registration_Window(self):
        self.newWindow=Toplevel(self.master)
        self.app=Window2(self.newWindow)

    def Login_Window(self):
        self.newWindow=Toplevel(self.master)
        self.app=Window3(self.newWindow)


class page5:
    def __init__(self,master):
        self.master=master
        self.master.title('Residential Information')
        self.master.geometry('1350x750+0+0')
        self.frame=Frame(self.master)
        self.frame.pack()
        
        self.Registerframe1 = Frame(self.frame,width=1100,height=600,bd=15,relief='ridge')
        self.Registerframe1.grid(row=1,column=0)
        self.Registerframe2 = Frame(self.frame,width=1000,height=100,bd=15,relief='ridge')
        self.Registerframe2.grid(row=2,column=0)

        self.l_house=StringVar()
        self.l_village=StringVar()
        self.l_district=StringVar()
        self.cbo_l_state=StringVar()
        self.l_pincode=StringVar()
        self.l_mobileno=StringVar()
        self.l_telephone=StringVar()
        self.l_Email=StringVar()

        Label(self.Registerframe1 ,text = 'Present Residential Address   ',font = ('',30),pady=5,padx=5).grid(row=0,column=0)
        
        Label(self.Registerframe1 ,text = 'House number and Street Name*',font = ('',20),pady=3,padx=5).grid(row=1,column=0)
        Entry(self.Registerframe1 ,textvariable = self.l_house,bd = 5,font = ('',15)).grid(row=1,column=1)
        Label(self.Registerframe1 ,text = 'Village/ Town / City*',font = ('',20),pady=3,padx=5).grid(row=2,column=0)
        Entry(self.Registerframe1 ,textvariable = self.l_village,bd = 5,font = ('',15)).grid(row=2,column=1)
        Label(self.Registerframe1 ,text = 'District *',font = ('',20),pady=3,padx=5).grid(row=3,column=0)
        Entry(self.Registerframe1 ,textvariable = self.l_district,bd = 5,font = ('',15)).grid(row=3,column=1)
        Label(self.Registerframe1 ,text = 'State *',font = ('',20),pady=3,padx=5).grid(row=4,column=0)
        self.cboNameTablet = ttk.Combobox(self.Registerframe1, font=('arial',15,'bold'), state='readonly',textvariable=self.cbo_l_state,width = 20)     
        self.cboNameTablet['value']=('','Enter state') 
        self.cboNameTablet.current(0)
        self.cboNameTablet.grid(row=4,column=1)
        Label(self.Registerframe1 ,text = 'Pin Code *',font = ('',20),pady=3,padx=5).grid(row=5,column=0)
        Entry(self.Registerframe1 ,textvariable = self.l_pincode,bd = 5,font = ('',15)).grid(row=5,column=1)
        Label(self.Registerframe1 ,text = 'Mobile No.*',font = ('',20),pady=3,padx=5).grid(row=6,column=0)
        Entry(self.Registerframe1 ,textvariable = self.l_mobileno,bd = 5,font = ('',15)).grid(row=6,column=1)
        Label(self.Registerframe1 ,text = 'Telephone No.',font = ('',20),pady=3,padx=5).grid(row=7,column=0)
        Entry(self.Registerframe1 ,textvariable = self.l_telephone,bd = 5,font = ('',15)).grid(row=7,column=1)
        Label(self.Registerframe1 ,text = 'E-mail ID *',font = ('',20),pady=3,padx=5).grid(row=8,column=0)
        Entry(self.Registerframe1 ,textvariable = self.l_Email,bd = 5,font = ('',15)).grid(row=8,column=1)

        Button(self.Registerframe2,text = ' Home',bd = 3 ,font = ('',20),padx=5,pady=5,command=self.Login_Window).grid(row=0,column=0)
        Button(self.Registerframe2,text = ' Save my Data',bd = 3 ,font = ('',20),padx=5,pady=5,command=self.check_P5).grid(row=0,column=1)
        self.dis_btn=Button(self.Registerframe2,text = ' Next ',state=DISABLED,bd = 3 ,font = ('',20),padx=5,pady=5,command=self.page6)
        self.dis_btn.grid(row=0,column=2)


    def F_error(self):
        self.screen1 = Tk()
        self.screen1.geometry("150x90")
        self.screen1.title("Warning!")
        Label(self.screen1, text = "All fields required", fg = "red").pack()
        Button(self.screen1, text = "OK",command=self.screen1.destroy).pack()

    def check_P5(self):
        if (  (self.l_house.get())=='' or (self.l_village.get())=='' or (self.l_district.get())=='' or
                           (self.cbo_l_state.get())=='' or (self.l_pincode.get())== '' or (self.l_mobileno.get())=='' or (self.l_Email.get())==''):
            #ms.showerror('Error!','Please Enter all the necessary fields  !! .')
            print(" error")
            #self.Registration_Window()
            self.F_error()
        else:
            self.Database_P5()

        
    def Database_P5(self):
            
                # make database and users (if not exists already) table at programme start up
        with sqlite3.connect('start.db') as db:
            c = db.cursor()

        c.execute('''CREATE TABLE IF NOT EXISTS  startLOG5(HOUSE_STREET TEXT  NOT NULL,
                                                                                                                          VILLAGE_NAME  TEXT                  NOT NULL,
                                                                                                                         DISTRICT_NAME                 TEXT                  NOT NULL,
                                                                                                                         STATE TEXT NOT NULL,
                                                                                                                         PIN_CODE                 TEXT                  NOT NULL,
                                                                                                                         MOBILE_NO                TEXT                  NOT NULL,
                                                                                                                         EMAIL_ID                 TEXT                  NOT NULL);''')
        print("Table is created")
        insert = 'INSERT INTO startLOG5(HOUSE_STREET,VILLAGE_NAME,DISTRICT_NAME,STATE,PIN_CODE,MOBILE_NO,EMAIL_ID) VALUES(?,?,?,?,?,?,?)'
        c.execute(insert,[(self.l_house.get()),(self.l_village.get()),(self.l_district.get()),
                           (self.cbo_l_state.get()),(self.l_pincode.get()),(self.l_mobileno.get()),(self.l_Email.get())])
        
        print('page 5 ok')
        self.dis_btn.config(state=NORMAL)
        db.commit()
        db.close()



    #=====================================================================================================

    def page6(self):
        self.newWindow=Toplevel(self.master)
        self.app=page6(self.newWindow)
    def Registration_Window(self):
        self.newWindow=Toplevel(self.master)
        self.app=Window2(self.newWindow)

    def Login_Window(self):
        self.newWindow=Toplevel(self.master)
        self.app=Window3(self.newWindow)



class page6:
    def __init__(self,master):
        self.master=master
        self.master.title('Emergency Contact')
        self.master.geometry('1350x750+0+0')
        self.frame=Frame(self.master)
        self.frame.pack()
        
        self.Registerframe1 = Frame(self.frame,width=1100,height=600,bd=15,relief='ridge')
        self.Registerframe1.grid(row=1,column=0)
        self.Registerframe2 = Frame(self.frame,width=1000,height=100,bd=15,relief='ridge')
        self.Registerframe2.grid(row=2,column=0)
        self.ename=StringVar()
        self.eaddress=StringVar()
        self.ephone=StringVar()
        self.eemail=StringVar()

        Label(self.Registerframe1 ,text = 'Emergency Contact  ',font = ('',30),pady=5,padx=5).grid(row=0,column=0)

        Label(self.Registerframe1 ,text = 'Name *',font = ('',20),pady=3,padx=5).grid(row=1,column=0)
        Entry(self.Registerframe1 ,textvariable =self.ename,bd = 5,font = ('arial',15)).grid(row=1,column=1)
        Label(self.Registerframe1 ,text = 'Address *',font = ('',20),pady=3,padx=5).grid(row=2,column=0)
        Entry(self.Registerframe1 ,textvariable =self.eaddress,bd = 5,font = ('arial',15)).grid(row=2,column=1)
        Label(self.Registerframe1 ,text = 'Phone no. *',font = ('',20),pady=3,padx=5).grid(row=3,column=0)
        Entry(self.Registerframe1 ,textvariable =self.ephone,bd = 5,font = ('arial',15)).grid(row=3,column=1)
        Label(self.Registerframe1 ,text = 'E-mail ID.',font = ('',20),pady=3,padx=5).grid(row=5,column=0)
        Entry(self.Registerframe1 ,textvariable =self.eemail,bd = 5,font = ('arial',15)).grid(row=5,column=1)

        Button(self.Registerframe2,text = ' Home',bd = 3 ,font = ('',20),padx=5,pady=5,command=self.Login_Window).grid(row=0,column=0)
        Button(self.Registerframe2,text = ' Save my Data',bd = 3 ,font = ('',20),padx=5,pady=5,command=self.check_P6).grid(row=0,column=1)                   #self.Database_P7
        Button(self.Registerframe2,text = ' Next ',bd = 3 ,font = ('',20),padx=5,pady=5,command=self.page7).grid(row=0,column=2)


    def Database_P6(self):
            
                # make database and users (if not exists already) table at programme start up
        with sqlite3.connect('start.db') as db:
            c = db.cursor()

        c.execute('''CREATE TABLE IF NOT EXISTS  startLOG6(NAME TEXT  NOT NULL,
                                                                                                                          ADDRESS  TEXT                  NOT NULL,
                                                                                                                         PHONE_NO                 TEXT                  NOT NULL,
                                                                                                                         STATE TEXT NOT NULL,
                                                                                                                         EMAIL_ID                 TEXT                  NOT NULL);''')
        print("Table is created")
        insert = 'INSERT INTO startLOG6(NAME,ADDRESS,PHONE_NO,STATE,EMAIL_ID) VALUES(?,?,?,?,?)'
        c.execute(insert,[(self.ename.get()),(self.eaddress.get()),(self.ephone.get()),(self.eemail.get())])
        
        print('page 6 ok')
        self.dis_btn.config(state=NORMAL)
        db.commit()
        db.close()

    def PH_crct(self):
        self.screen5= Tk()
        self.screen5.geometry("200x120")
        self.screen5.title("Warning!")
        Label(self.screen5, text = "Please fill the Phone No. correctly" , fg = "red",font=('algerian',20)).pack()
        Button(self.screen5, text = "OK",command=self.screen5.destroy).pack()
        self.phone.set('')

    def E_crct(self):
        self.screen5= Tk()
        self.screen5.geometry("200x120")
        self.screen5.title("Warning!")
        Label(self.screen5, text = "Please fill the Email correctly" , fg = "red",font=('algerian',20)).pack()
        Button(self.screen5, text = "OK",command=self.screen5.destroy).pack()
        self.phone.set('')


    def check_P6(self):
        if ((self.ename.get())=='' or (self.eaddress.get())=='' or (self.ephone.get())=='' ):
            print('error')
            
            print(self.ename.get())
            print(self.eaddress.get())
            print(self.ephone.get())
            self.F_error()
        else:
            m = "\d{10}"
            e = '[\w._%+-]{1,20}@[\w.-]{2,20}.[A-Za-z]{2,3}'
            print('ok')
            e1 = re.match(e,self.eemail.get())
            m1=re.match(m ,self.ephone.get())

            if e1:
                if m1:
                  self.Database_P6()
                else:
                  self.PH_crct()
            else:
                  self.E_crct()
                
                #self.page7()

    def F_error(self):
        global screen1
        self.screen1 = Tk()
        self.screen1.geometry("150x90")
        self.screen1.title("Warning!")
        Label(self.screen1, text = "Please fill all required fields ", fg = "red").pack()
        Button(self.screen1, text = "OK",command=self.screen1.destroy).pack()

    def page7(self):
        self.newWindow=Toplevel(self.master)
        self.app=page7(self.newWindow)

    def Registration_Window(self):
        self.newWindow=Toplevel(self.master)
        self.app=Window2(self.newWindow)

    def Login_Window(self):
        self.newWindow=Toplevel(self.master)
        self.app=Window3(self.newWindow)

    def Tracking_Window(self):
        self.newWindow=Toplevel(self.master)
        self.app=Window4(self.newWindow)

    def Appointment_Window(self):
        self.newWindow=Toplevel(self.master)
        self.app=Window5(self.newWindow)

#=====================================================================================================
#=====================================================================================================
#=====================================================================================================

class page7:        
    def __init__(self,master):
        self.master=master
        self.master.title('Self-Declaration form')
        self.master.geometry('1350x750+0+0')
        self.frame=Frame(self.master)
        self.frame.pack()
        
        self.Registerframe1 = Frame(self.frame,width=1100,height=600,bd=15,relief='ridge')
        self.Registerframe1.grid(row=1,column=0)
        self.Registerframe2 = Frame(self.frame,width=1000,height=100,bd=15,relief='ridge')
        self.Registerframe2.grid(row=2,column=0)

        self.CheckVar2=IntVar()
        Label(self.Registerframe1 ,text = 'Self Declaration ',font = ('',30),pady=5,padx=5).grid(row=0,column=0)

        T = Text(self.Registerframe1, height=15, width=90)
        T.grid(row=1,column=0)
        quote = ''' I owe allegiance to sovereignity , unity and integrity of India
and have not voluntarily acquired citizenship or travel document document
of any another country.
        I assure that information given by me in this form and the enclosures is true ,
             I am solely responsible for its accuracy and
             I am liable to be penalized or prosecuted if found otherwise.'''
        T.insert(END, quote)
        Checkbutton(self.Registerframe1, text = " I Accept", variable =self.CheckVar2, onvalue = 1, offvalue = 0, height=5, width = 20).grid(row=2,column=0)
        self.btnRegister=Button(self.Registerframe2 ,text="Home ",width=25,font=('arial',10,'bold'),
                                                                            command=self.Login_Window,height=3)
        self.btnRegister.grid(row=0,column=0,pady=5,padx=10)


        self.btnpage7 = Button(self.Registerframe2,text = "Submit",width=25,font=('arial',10,'bold'),
                                     command = self.page8,height=3)#  state = DISABLED
        self.btnpage7.grid(row = 0, column = 1,pady=5,padx=10)



#=====================================================================================================

    def page8(self):
        self.newWindow=Toplevel(self.master)
        self.app=page8(self.newWindow)
        
    def Registration_Window(self):
        self.newWindow=Toplevel(self.master)
        self.app=Window2(self.newWindow)

    def Login_Window(self):
        self.newWindow=Toplevel(self.master)
        self.app=Window3(self.newWindow)

    def Tracking_Window(self):
        self.newWindow=Toplevel(self.master)
        self.app=Window4(self.newWindow)

    def Appointment_Window(self):
        self.newWindow=Toplevel(self.master)
        self.app=Window5(self.newWindow)


class page8:
    def __init__(self,master):
        self.screen4 =master
        self.screen4.geometry("300x200")
        self.screen4.title("Complete!")
        Label(self.screen4, text = "Registration Done", fg = "red").pack()
        Button(self.screen4, text = "Ok",command=self.screen4.destroy).pack()
            

        
#=====================================================================================================
    def Registration_Window(self):
        self.newWindow=Toplevel(self.master)
        self.app=Window2(self.newWindow)

    def Login_Window(self):
        self.newWindow=Toplevel(self.master)
        self.app=Window3(self.newWindow)

    def Tracking_Window(self):
        self.newWindow=Toplevel(self.master)
        self.app=Window4(self.newWindow)

    def Appointment_Window(self):
        self.newWindow=Toplevel(self.master)
        self.app=Window5(self.newWindow)
#=====================================================================================================
#=====================================================================================================
class Window4():
    def __init__(self,master):
        self.master=master
        self.master.title('Track Application Status')
        self.master.geometry('1350x750+0+0')
        self.frame=Frame(self.master)
        self.frame.pack()
#=====================================================================================================
    def Registration_Window(self):
        self.newWindow=Toplevel(self.master)
        self.app=Window2(self.newWindow)

    def Login_Window(self):
        self.newWindow=Toplevel(self.master)
        self.app=Window3(self.newWindow)

    def Tracking_Window(self):
        self.newWindow=Toplevel(self.master)
        self.app=Window4(self.newWindow)

    def Appointment_Window(self):
        self.newWindow=Toplevel(self.master)
        self.app=Window5(self.newWindow)
#=====================================================================================================
#=====================================================================================================
class Window5():
    def __init__(self,master):
        self.master=master
        self.master.title('Appointment Availability')
        self.master.geometry('1350x750+0+0')
        self.frame=Frame(self.master)
        self.frame.pack()
#=====================================================================================================
    def Registration_Window(self):
        self.newWindow=Toplevel(self.master)
        self.app=Window2(self.newWindow)

    def Login_Window(self):
        self.newWindow=Toplevel(self.master)
        self.app=Window3(self.newWindow)

    def Tracking_Window(self):
        self.newWindow=Toplevel(self.master)
        self.app=Window4(self.newWindow)

    def Appointment_Window(self):
        self.newWindow=Toplevel(self.master)
        self.app=Window5(self.newWindow)
#=====================================================================================================




if __name__=='__main__':
    main() 
