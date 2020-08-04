from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
import random
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="sarthak",
  database="mydatabase"
)

mycursor=mydb.cursor()
#mycursor.execute("CREATE TABLE customers (pnr INT PRIMARY KEY NOT NULL, bpoint VARCHAR(255) NOT NULL, dpoint VARCHAR(255) NOT NULL, slots VARCHAR(255) NOT NULL, fname VARCHAR(255) NOT NULL, lname VARCHAR(255) NOT NULL, age INT NOT NULL, gender VARCHAR(25), phone_no INT NOT NULL)")
#mycursor.execute("CREATE TABLE rail (train_no INT PRIMARY KEY NOT NULL, train_name VARCHAR(255), price FLOAT, time VARCHAR(255), ipoint VARCHAR(255), fpoint VARCHAR(255))")

#mycursor.execute("INSERT INTO rail (train_no, train_name, price, time, ipoint, fpoint) VALUES (2345, 'Shatapdi Express', 1000, '5:00', 'Mumbai', 'Chennai')")
#mycursor.execute("INSERT INTO rail (train_no, train_name, price, time, ipoint, fpoint) VALUES (7324, 'Mum Ban EXP', 400, '6:00 ', 'Mumbai', 'Bangalore')")
#mycursor.execute("INSERT INTO rail (train_no, train_name, price, time, ipoint, fpoint) VALUES (3245, 'Mumbai Express', 600, '7:00 ', 'Mumbai', 'Delhi')")
#mycursor.execute("INSERT INTO rail (train_no, train_name, price, time, ipoint, fpoint) VALUES (8545, 'Karnataka Exp', 700, '8:00', 'Bangalore', 'Delhi')")
#mycursor.execute("INSERT INTO rail (train_no, train_name, price, time, ipoint, fpoint) VALUES (5345, 'Ban Mum EXP', 350, '9:00', 'Bangalore', 'Chennai')")
#mycursor.execute("INSERT INTO rail (train_no, train_name, price, time, ipoint, fpoint) VALUES (4345, 'Bangalore Express', 500, '11:00', 'Bangalore', 'Mumbai')")
#mycursor.execute("INSERT INTO rail (train_no, train_name, price, time, ipoint, fpoint) VALUES (9945, 'Kranti Express', 700, '10:00', 'Delhi', 'Chennai')")
#mycursor.execute("INSERT INTO rail (train_no, train_name, price, time, ipoint, fpoint) VALUES (1885, 'Del Mum Exp', 650, '8:00', 'Delhi', 'Mumbai')")
#mycursor.execute("INSERT INTO rail (train_no, train_name, price, time, ipoint, fpoint) VALUES (1745, 'Delhi Express', 7500, '5:00', 'Delhi', 'Bangalore')")
#mycursor.execute("INSERT INTO rail (train_no, train_name, price, time, ipoint, fpoint) VALUES (1145, 'Che Ban Express', 400, '6:00', 'Chennai', 'Bangalore')")
#mycursor.execute("INSERT INTO rail (train_no, train_name, price, time, ipoint, fpoint) VALUES (1235, 'CHE MUM EXP',650, '4:00', 'Chennai', 'Mumbai')")
#mycursor.execute("INSERT INTO rail (train_no, train_name, price, time, ipoint, fpoint) VALUES (1345, 'Chennai Express', 1000, '8:00', 'Chennai', 'Delhi')")

#mycursor.execute("CREATE TABLE flight (flight_no varchar(225) PRIMARY KEY NOT NULL, name VARCHAR(255), price FLOAT, time VARCHAR(255), ipoint VARCHAR(255), fpoint VARCHAR(255))")
#mycursor.execute("INSERT INTO flight (flight_no, name, price, time, ipoint, fpoint) VALUES ('AI235', 'Air India', 2000, '5:00', 'Mumbai', 'chennai')")
#mycursor.execute("INSERT INTO flight (flight_no, name, price, time, ipoint, fpoint) VALUES ('9W134', 'Jet Airways', 3000, '7:00 ', 'Mumbai', 'Delhi')")
#mycursor.execute("INSERT INTO flight (flight_no, name, price, time, ipoint, fpoint) VALUES ('36E24', 'IndiGo', 1800, '6:00 ', 'Mumbai', 'Bangalore')")
#mycursor.execute("INSERT INTO flight (flight_no, name, price, time, ipoint, fpoint) VALUES ('IX545', 'Air India Express', 1500, '8:00', 'Bangalore', 'Delhi')")
#mycursor.execute("INSERT INTO flight (flight_no, name, price, time, ipoint, fpoint) VALUES ('SG534', 'Spicejet', 1000, '5:00', 'Bangalore', 'Chennai')")
#mycursor.execute("INSERT INTO flight (flight_no, name, price, time, ipoint, fpoint) VALUES ('G8045', 'GoAir', 1400, '9:00', 'Bangalore', 'Mumbai')")
#mycursor.execute("INSERT INTO flight (flight_no, name, price, time, ipoint, fpoint) VALUES ('I5994', 'AirAsia India', 2500, '10:00', 'Delhi', 'Chennai')")
#mycursor.execute("INSERT INTO flight (flight_no, name, price, time, ipoint, fpoint) VALUES ('UK885', 'Vistara', 2200, '8:00', 'Delhi', 'Mumbai')")
#mycursor.execute("INSERT INTO flight (flight_no, name, price, time, ipoint, fpoint) VALUES ('9I174', 'Alliance Air', 2400, '11:00', 'Delhi', 'Bangalore')")
#mycursor.execute("INSERT INTO flight (flight_no, name, price, time, ipoint, fpoint) VALUES ('2T745', 'TruJet', 1200, '4:00', 'Chennai', 'Bangalore')")
#mycursor.execute("INSERT INTO flight (flight_no, name, price, time, ipoint, fpoint) VALUES ('TA546','TajAir', 1800, '5:00', 'Chennai', 'Mumbai')")
#mycursor.execute("INSERT INTO flight (flight_no, name, price, time, ipoint, fpoint) VALUES ('QO153', 'Quikjet', 2000, '8:00', 'Chennai', 'Delhi')")

#mycursor.execute("CREATE TABLE bus (bus_no INT PRIMARY KEY NOT NULL, bus_name VARCHAR(255), price FLOAT, time VARCHAR(255), ipoint VARCHAR(255), fpoint VARCHAR(255))")
#mycursor.execute("INSERT INTO bus (bus_no, bus_name, price, time, ipoint, fpoint) VALUES (2345, 'A5', 300, '5:00', 'Mumbai', 'Chennai')")
#mycursor.execute("INSERT INTO bus (bus_no, bus_name, price, time, ipoint, fpoint) VALUES (7345, 'C7', 450, '7:00 ', 'Mumbai', 'Delhi')")
#mycursor.execute("INSERT INTO bus (bus_no, bus_name, price, time, ipoint, fpoint) VALUES (1245, 'B3', 350, '6:00 ', 'Mumbai', 'Bangalore')")
#mycursor.execute("INSERT INTO bus (bus_no, bus_name, price, time, ipoint, fpoint) VALUES (8545, 'D4', 500, '8:00', 'Bangalore', 'Delhi')")
#mycursor.execute("INSERT INTO bus (bus_no, bus_name, price, time, ipoint, fpoint) VALUES (5345, 'E1', 200, '4:00', 'Bangalore', 'Chennai')")
#mycursor.execute("INSERT INTO bus (bus_no, bus_name, price, time, ipoint, fpoint) VALUES (0345, 'F8', 280, '9:00', 'Bangalore', 'Mumbai')")
#mycursor.execute("INSERT INTO bus (bus_no, bus_name, price, time, ipoint, fpoint) VALUES (9945, 'G4', 600, '10:00', 'Delhi', 'Chennai')")
#mycursor.execute("INSERT INTO bus (bus_no, bus_name, price, time, ipoint, fpoint) VALUES (1885, 'H9', 550, '11:00', 'Delhi', 'Mumbai')")
#mycursor.execute("INSERT INTO bus (bus_no, bus_name, price, time, ipoint, fpoint) VALUES (1745, 'I4', 650, '3:00', 'Delhi', 'Bangalore')")
#mycursor.execute("INSERT INTO bus (bus_no, bus_name, price, time, ipoint, fpoint) VALUES (1145, 'J3', 250, '9:00', 'Chennai', 'Bangalore')")
#mycursor.execute("INSERT INTO bus (bus_no, bus_name, price, time, ipoint, fpoint) VALUES (1235, 'K5', 500, '5:00', 'Chennai', 'Mumbai')")
#mycursor.execute("INSERT INTO bus (bus_no, bus_name, price, time, ipoint, fpoint) VALUES (1345, 'L1', 800, '8:00', 'Chennai', 'Delhi')")


window=Tk()
window.title("TRAVELLING")
window.configure(background="steel blue")
#window.geometry("1200x300")

lbl_a=Label(window,text="   TRAVELLING MANAGEMENT SYSTEM  ",font=("Arial Bold",22))
lbl_a.grid(column=1,row=1)


lbl_f=Label(window,text="From",font=("Arial Bold", 16))
lbl_f.grid(column=0,row=3)
txt_f=Combobox(window,font=("Arial Bold",14))
txt_f['values']=("Mumbai","Chennai","Delhi","Banglore")
txt_f.grid(column=1,row=3)
txt_f.focus()


lbl_t=Label(window,text="To",font=("Arial Bold", 14))
lbl_t.grid(column=2,row=3)
txt_t = Combobox(window,font=("Arial Bold",12))
txt_t['values']=("Mumbai","Chennai","Delhi","Banglore")
txt_t.grid(column=3 ,row=3)
txt_t.focus()

lbl_s=Label(window,text="Slots",font=("Arial Bold", 14))
lbl_s.grid(column=0,row=4)
txt_s = Combobox(window,font=("Arial Bold",12))
txt_s['values']=("Morning","Evening")
txt_s.grid(column=1, row=4)
txt_s.focus()

lbl_fn=Label(window,text="First Name",font=("Arial Bold", 14))
lbl_fn.grid(column=0,row=8)
txt_fn=Entry(window,font=("Arial Bold",15))
txt_fn.grid(column=1,row=8)
txt_fn.focus()

lbl_ln=Label(window,text="Last Name",font=("Arial Bold", 14))
lbl_ln.grid(column=2,row=8)
txt_ln=Entry(window,font=("Arial Bold",14))
txt_ln.grid(column=3,row=8)


lbl_ag=Label(window,text="  Age  ",font=("Arial Bold", 14))
lbl_ag.grid(column=0,row=9)
txt_ag=Entry(window,font=("Arial Bold",14))
txt_ag.grid(column=1,row=9)


lbl_g=Label(window,text="Gender",font=("Arial Bold", 14))
lbl_g.grid(column=2,row=9)
txt_g = Combobox(window,font=("Arial Bold",12))
txt_g['values']=("Male","Female")
txt_g.grid(column=3, row=9)
txt_g.focus()

lbl_pn=Label(window,text="Phone number",font=("Arial Bold", 14))
lbl_pn.grid(column=0,row=11)
txt_pn=Entry(window,font=("Arial Bold",13))
txt_pn.grid(column=1,row=11)


lbl_g=Label(window,text="Mode",font=("Arial Bold", 14))
lbl_g.grid(column=2,row=11)
txt_m = Combobox(window,font=("Arial Bold",12))
txt_m['values']=("Bus","Rail","Flight")
txt_m.grid(column=3, row=11)
txt_m.focus()

global c
c=""
def check_cbox(event):
    global c
    if txt_f.get() == 'Mumbai':
        c = txt_f.get() # this will assign the variable c the value of cbox
    if txt_f.get() == 'Chennai':
        c = txt_f.get()
    if txt_f.get() == 'Delhi':
        c = txt_f.get()
    if txt_f.get() == 'Banglore':
        c = txt_f.get()
txt_f.bind("<<ComboboxSelected>>", check_cbox)

global d
d=""
def check_cbox(event):
    global d
    if txt_t.get() == 'Mumbai':
        d = txt_t.get() # this will assign the variable d the value of cbox
    if txt_t.get() == 'Chennai':
        d = txt_t.get()
    if txt_t.get() == 'Delhi':
        d = txt_t.get()
    if txt_t.get() == 'Banglore':
        d = txt_t.get()
txt_t.bind("<<ComboboxSelected>>", check_cbox)

a=txt_f.get()
b=txt_t.get()
def clicked_b():
    
     
    p=random.randint(100,900)
    a=txt_f.get()
    b=txt_t.get()
    c=txt_s.get()
    d=txt_fn.get()
    e=txt_ln.get()
    f=txt_ag.get()
    g=txt_g.get()
    h=txt_pn.get()
    sq = """ INSERT INTO `customers`
                          (`pnr`, `bpoint`, `dpoint`, `slots`, `fname`, `lname`, `age`, `gender`, `phone_no`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
    dq = (p,a,b,c,d,e,f,g,h)
    mycursor.execute(sq,dq)
    mydb.commit()
     
    mode=Toplevel()
    mode.title("Details")
    mode.configure(background="steel blue")
    mode.geometry("600x400")

    m=""
    def check_cbox(event):
        global m
        if txt_m.get() == 'Bus':
            m = txt_m.get() # this will assign the variable c the value of cbox
        if txt_m.get() == 'Flight':
            m = txt_m.get()
        if txt_m.get() == 'Rail':
            m = txt_m.get()
    txt_m.bind("<<ComboboxSelected>>", check_cbox)

    if txt_m.get()=="Rail":
        a=txt_f.get()
        b=txt_t.get()
        mycursor.execute("""select * from rail where ipoint = '%s' AND fpoint='%s'""" % (a,b))
        result=mycursor.fetchall()
        for x in result:
            a6=x[0]
            a2=x[1]
            a3=x[2]
            a4=x[3]
        lbl_pn=Label(mode,text="Train Details",font=("Arial Bold",24))
        lbl_pn.grid(column=2,row=1)
        lbl_pn=Label(mode,text="  Train No.  ",font=("Arial Bold", 18))
        lbl_pn.grid(column=1,row=3)
        lbl_pn=Label(mode,text=a6,font=("Arial Bold", 18))
        lbl_pn.grid(column=2,row=3)  
        lbl_pn=Label(mode,text="  Train Name:  ",font=("Arial Bold", 18))
        lbl_pn.grid(column=1,row=4)    
        lbl_pn=Label(mode,text=a2,font=("Arial Bold", 18))
        lbl_pn.grid(column=2,row=4)    
        lbl_pn=Label(mode,text="  Price  ",font=("Arial Bold", 18))
        lbl_pn.grid(column=1,row=6)    
        lbl_pn=Label(mode,text=a3,font=("Arial Bold", 18))
        lbl_pn.grid(column=2,row=6)    
        lbl_pn=Label(mode,text="  Time  ",font=("Arial Bold", 18))
        lbl_pn.grid(column=1,row=8)    
        lbl_pn=Label(mode,text=a4,font=("Arial Bold", 18))
        lbl_pn.grid(column=2,row=8)
        
    if txt_m.get()=="Flight":
        a=txt_f.get()
        b=txt_t.get()
        mycursor.execute("""select * from flight where ipoint = '%s' AND fpoint='%s'""" % (a,b))
        result=mycursor.fetchall()
        for x in result:
            a6=x[0]
            a2=x[1]
            a3=x[2]
            a4=x[3]
        lbl_pn=Label(mode,text="Flight Details",font=("Arial Bold",24))
        lbl_pn.grid(column=2,row=1)
        lbl_pn=Label(mode,text="  Flight No.  ",font=("Arial Bold", 18))
        lbl_pn.grid(column=1,row=3)
        lbl_pn=Label(mode,text=a6,font=("Arial Bold", 18))
        lbl_pn.grid(column=2,row=3)  
        lbl_pn=Label(mode,text="  Flight Name:  ",font=("Arial Bold", 18))
        lbl_pn.grid(column=1,row=4)    
        lbl_pn=Label(mode,text=a2,font=("Arial Bold", 18))
        lbl_pn.grid(column=2,row=4)    
        lbl_pn=Label(mode,text="  Price  ",font=("Arial Bold", 18))
        lbl_pn.grid(column=1,row=6)    
        lbl_pn=Label(mode,text=a3,font=("Arial Bold", 18))
        lbl_pn.grid(column=2,row=6)    
        lbl_pn=Label(mode,text="  Time  ",font=("Arial Bold", 18))
        lbl_pn.grid(column=1,row=8)    
        lbl_pn=Label(mode,text=a4,font=("Arial Bold", 18))
        lbl_pn.grid(column=2,row=8)
        
    if txt_m.get()=="Bus":
        a=txt_f.get()
        b=txt_t.get()
        mycursor.execute("""select * from bus where ipoint = '%s' AND fpoint='%s'""" % (a,b))
        result=mycursor.fetchall()
        for x in result:
            a6=x[0]
            a2=x[1]
            a3=x[2]
            a4=x[3]        
        lbl_pn=Label(mode,text="Bus Details",font=("Arial Bold",24))
        lbl_pn.grid(column=2,row=1)
        lbl_pn=Label(mode,text="  Bus No.  ",font=("Arial Bold", 18))
        lbl_pn.grid(column=1,row=3)
        lbl_pn=Label(mode,text=a6,font=("Arial Bold", 18))
        lbl_pn.grid(column=2,row=3)  
        lbl_pn=Label(mode,text="Bus Name  ",font=("Arial Bold", 18))
        lbl_pn.grid(column=1,row=4)    
        lbl_pn=Label(mode,text=a2,font=("Arial Bold", 18))
        lbl_pn.grid(column=2,row=4)    
        lbl_pn=Label(mode,text="  Price  ",font=("Arial Bold", 18))
        lbl_pn.grid(column=1,row=6)    
        lbl_pn=Label(mode,text=a3,font=("Arial Bold", 18))
        lbl_pn.grid(column=2,row=6)    
        lbl_pn=Label(mode,text="  Time  ",font=("Arial Bold", 18))
        lbl_pn.grid(column=1,row=8)    
        lbl_pn=Label(mode,text=a4,font=("Arial Bold", 18))
        lbl_pn.grid(column=2,row=8)    
                    
    #messagebox.showinfo('Confirmation', 'Ticket booked...!')

def update():
    top=Toplevel()
    top.title("Update")
    lbl_pn=Label(top,text="Phone number",font=("Arial Bold", 10))
    lbl_pn.grid(column=0,row=1)
    txt_pn=Entry(top,width=10)
    txt_pn.grid(column=1,row=1)
       
    lbl_pnr=Label(top,text="PNR",font=("Arial Bold", 10))
    lbl_pnr.grid(column=2,row=1)
    txt_pnr=Entry(top,width=10)
    txt_pnr.grid(column=3,row=1)
    def update_u():

        sql = """Update customers set phone_no = %s where pnr = %s"""
        pnu=txt_pn.get()
        pnru=txt_pnr.get()
        dq = (pnu,pnru)
        mycursor.execute(sql,dq)
        mydb.commit()
        messagebox.showinfo('Confirmation', 'Updated...!')

    btn=Button(top,text="Update",command=update_u)
    btn.grid(column=0,row=2)


def cancelt():
    top1=Toplevel()
    lbl_ag=Label(top1,text="PNR",font=("Arial Bold", 10))
    lbl_ag.grid(column=0,row=1)
    txt_ag=Entry(top1,width=10)
    txt_ag.grid(column=1,row=1)
    def clear():
        sql_Delete_query = """Delete from customers where pnr = %s"""
        mobile_id = txt_ag.get()
        mycursor.execute(sql_Delete_query,(mobile_id,))
        mydb.commit()
        messagebox.showinfo('Confirmation', 'Cancelled...!')

    btn=Button(top1,text="Cancel",command=clear)
    btn.grid(column=2,row=1)

btn=Button(window,text='Next',width=40,command=clicked_b)
btn.grid(column=1,row=20)

btn=Button(window,text="Update",width=40,command=update)
btn.grid(column=1,row=28)


btn=Button(window, text="Cancel Ticket",width=40,command=cancelt)
btn.grid(column=2,row=28)


window.mainloop()
