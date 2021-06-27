# -*- coding: utf-8 -*-


# import pip
# pip.main(['install','sklearn'])
import mysql.connector as mysqLtor
from tkinter import *
from tkcalendar import Calendar
import random
from tkinter import ttk
import tkinter.messagebox
from datetime import datetime
import pandas as pd
from sqlalchemy import create_engine
import pymysql
import numpy as np
import matplotlib.pyplot as plt

mycon=mysqLtor.connect(user='root',passwd='atharva2000',host='localhost',charset='utf8',use_pure=True)
cursor=mycon.cursor()
#cursor.execute("DROP DATABASE hotel3")
cursor.execute("CREATE DATABASE IF NOT EXISTS hotel3")
cursor.execute("USE hotel3")
cursor.execute("CREATE TABLE IF NOT EXISTS customer(name VARCHAR(50),city VARCHAR(50),email VARCHAR(20),mobile_no VARCHAR(13),stay_period INT(2))")
cursor.execute("CREATE TABLE IF NOT EXISTS cost(name VARCHAR(50), room_no INT(3) UNIQUE KEY,room VARCHAR(15), amount INT(5), checkinColumn VARCHAR(10), checkoutColumn VARCHAR(10), bookingMonth VARCHAR(10))")
cursor.execute("CREATE TABLE IF NOT EXISTS rooms(roomtype VARCHAR(12), room_no INT(4))")


#cursor.execute("CREATE TABLE IF NOT EXISTS evaluate(TotalCustomers INT(5),monthNo INT(2) ,Month VARCHAR(15))")

# sql="INSERT INTO rooms(roomtype, room_no) VALUES (%s,%s)"
# val=[('royal',101),('royal',102),('royal',103),('royal',104),
#       ('luxury',201),('luxury',202),('luxury',203),('luxury',204),
#       ('superior',301),('superior',302),('superior',303),('superior',304),
#       ('deluxe',401),('deluxe',402),('deluxe',403),('deluxe',404)]

# cursor.executemany(sql,val)
# mycon.commit()

# sql2="INSERT INTO evaluate(TotalCustomers, monthNo, Month) VALUES (%s,%s,%s)"
# val2=[(15,1,'January'),(10,2,'February'),(17,3,'March'),(20,4,'April'),(30,5,'May'),(27,6,'June'),
#       (25,7,'July'),(23,8,'August'),(18,9,'September'),(15,10,'October'),(14,11,'November'),(20,12,'December')]

# cursor.executemany(sql2,val2)
# mycon.commit()


root=Tk()
root.title('Marina Bay Sands Hotel')
root.geometry("890x580+0+0")


head=Frame(root)
head.pack()


frame1=Frame(root,padx=25)
frame1.pack(side=LEFT)

hotelImage=PhotoImage(file="Hotel1.gif")
lblImage=Label(frame1,image=hotelImage,height=500,width=500)
lblImage.pack(side=LEFT)

frame2=Frame(root)
frame2.pack(side=LEFT)

# =============================================================================
# royal=[101,102,103,104]
# luxury=[201,202,203,204]
# superior=[301,302,303,304]
# deluxe=[401,402,403,404]
# =============================================================================


def sel():
    
    v1=var.get()
    print("Room Cost is",var.get())
    
def amount():
    
    global v
    v=var.get()
    Cost=v
    Service_charge=v/99
    Gst=v*0.33
    Total=Cost+Service_charge+Gst
    
    c="Rs.",str('%.2f'%v)
    s="Rs.",str('%.2f'%Service_charge)
    g="Rs.",str('%.2f'%(v*0.33))
    st="Rs.",str('%.2f'%v)
    t="Rs.",str('%.2f'%Total)
    cost.set(c)
    service.set(s)
    gst.set(g)
    subtotal.set(st)
    total.set(t)
    
def savebtn():
    
    dbname=name.get()
    dbaddress=address.get()
    dbemail=email.get()
    dbmobile_no=number.get()
    dbstay_period=days.get()
    dbcheckin=checkin.get()
    dbcheckout=checkout.get()
    dbmonth=calMonth
    
    
    #royal=[101,102,103,104]
    #luxury=[201,202,203,204]
    #superior=[301,302,303,304]
    #deluxe=[401,402,403,404]
    
    # print("1st value in list:",royal[0])
    # r=royal[0]
    # royal.remove(r)
    #r=random.choice(royal)
    # l=random.choice(luxury)
    # sup=random.choice(superior)
    # d=random.choice(deluxe)
    
    
    if v==5000:
        
        cursor.execute("SELECT min(room_no) FROM rooms WHERE roomtype='royal'")
        data=cursor.fetchone()
        for row in data:
            print(row)
            r=row
            sqlDel=("DELETE FROM rooms WHERE room_no=%s")
            value=(r,)
            cursor.execute(sqlDel,value)
            mycon.commit()
            
        roomtype="Royal Suite"
        roomNo=r
        
    elif v==4000:
        
        cursor.execute("SELECT min(room_no) FROM rooms WHERE roomtype='luxury'")
        data=cursor.fetchone()
        for row in data:
            print(row)
            l=row
            sqlDel=("DELETE FROM rooms WHERE room_no=%s")
            value=(l,)
            cursor.execute(sqlDel,value)
            mycon.commit()
        
        roomtype="Luxury Suite"
        roomNo=l
        
    elif v==2000:
        
        cursor.execute("SELECT min(room_no) FROM rooms WHERE roomtype='superior'")
        data=cursor.fetchone()
        for row in data:
            print(row)
            sup=row
            sqlDel=("DELETE FROM rooms WHERE room_no=%s")
            value=(sup,)
            cursor.execute(sqlDel,value)
            mycon.commit()
        
        roomtype="Superior Suite"
        roomNo=sup
        
    else:
        
        cursor.execute("SELECT min(room_no) FROM rooms WHERE roomtype='deluxe'")
        data=cursor.fetchone()
        for row in data:
            print(row)
            d=row
            sqlDel=("DELETE FROM rooms WHERE room_no=%s")
            value=(d,)
            cursor.execute(sqlDel,value)
            mycon.commit()
        
        roomtype="Deluxe Suite"
        roomNo=d
        
    print(roomtype,"",roomNo)
    print(dbmonth)
    
    try:
        #
        cursor.execute("")
        cursor.execute("INSERT INTO cost(name,room_no,room,amount,checkinColumn,checkoutColumn,bookingMonth) VALUES('{}',{},'{}',{},'{}','{}','{}')".format(dbname,roomNo,roomtype,v,dbcheckin,dbcheckout,dbmonth))
        cursor.execute("INSERT INTO customer(name,city,email,mobile_no,stay_period) VALUES('{}','{}','{}', '{}', {})".format(dbname,dbaddress,dbemail,dbmobile_no,dbstay_period))
        mycon.commit()
        tkinter.messagebox.showinfo("Booking confirmed", str(roomtype)+" - "+str(roomNo))

    
    except:
        tkinter.messagebox.showinfo("","Sorry the rooms are full")
        
def reset():
    
    name.set("")
    address.set("")
    email.set("")
    number.set("")
    days.set("")
    
    var.set("")
    
    cost.set("")
    service.set("")
    gst.set("")
    subtotal.set("")
    total.set("")

def Exit():
    
    top.destroy()
    
#----------------------------------------------------------Check In----------------------------------
def processCheckIn():
    
    global var
    global cost,service,gst,subtotal,total
    global name,address,email,number,days
    global checkin,checkout,date
    #global calMonth
    global top
    
    
    top=Toplevel()
    top.title("Check In")
    top.geometry("1000x600+0+0")
    
    f1=Frame(top,height=25,width=170) #CheckIN
    f1.pack(side=TOP)
    
    f2=Frame(top,pady=25,height=25,width=170) #bottom buttons
    f2.pack(side=BOTTOM)
    
    f3=Frame(top,pady=10,padx=10,height=50,width=100) #Total
    f3.pack(side=RIGHT,anchor='nw')
    
    f6=Frame(top,padx=15,pady=10,height=25,width=100) #calendar
    f6.pack(side=RIGHT,anchor='ne')
    
    f4=Frame(top,pady=10,height=50,width=100) #Name
    f4.pack(side=TOP,anchor='w')
    
    f5=Frame(top,padx=10,pady=30,height=25,width=100) #radio buttons
    f5.pack(side=TOP,anchor='w')
    
    
  #---------------------------------------------frame 1-------------------------------------------------
    
    checkinmsg=Label(f1,text="Check In",font="arial 20 bold italic",fg='orangered2',justify='center')
    checkinmsg.grid(pady=20)

  #---------------------------------------------frame 2-------------------------------------------------
    
    savebt=Button(f2,text='Save',font="ariel 16 bold",fg='white', bg='orangered2',padx=16,bd=10,width=10,command=savebtn)
    savebt.grid(row=17,column=10,padx=10)
    
    totalbt=Button(f2,text='Total',font="ariel 16 bold",fg='white', bg='orangered2',padx=16,bd=10,width=10,command=amount)
    totalbt.grid(row=17,column=11,padx=10)
    
    resetbt=Button(f2,text='Reset',font="ariel 16 bold",fg='white', bg='orangered2',padx=16,bd=10,width=10,command=reset)
    resetbt.grid(row=17,column=12,padx=10)
    
    exitbt2=Button(f2,text='Exit',font="ariel 16 bold",fg='white', bg='orangered2',padx=16,bd=10,width=10,command=Exit)
    exitbt2.grid(row=17,column=13,padx=10)
    
  #---------------------------------------------frame 3-------------------------------------------------   
    
    cost=DoubleVar()
    service=DoubleVar()
    gst=DoubleVar()
    subtotal=DoubleVar()
    total=DoubleVar()
    checkin=StringVar()
    checkout=StringVar()
    
    lblcost=Label(f3,text="Cost",font="arial 12 bold")
    textcost=Entry(f3,textvariable=cost,font="arial 12 bold",bd=6,insertwidth=4)
    
    lblservice=Label(f3,text="Service Charge",font="arial 12 bold")
    textservice=Entry(f3,textvariable=service,font="arial 12 bold",bd=6,insertwidth=4)
    
    lblgst=Label(f3,text="Gst",font="arial 12 bold")
    textgst=Entry(f3,textvariable=gst,font="arial 12 bold",bd=6,insertwidth=4)
    
    lblsubtotal=Label(f3,text="Subtotal",font="arial 12 bold")
    textsubtotal=Entry(f3,textvariable=subtotal,font="arial 12 bold",bd=6,insertwidth=4)
    
    lbltotal=Label(f3,text="Total",font="arial 12 bold")    
    texttotal=Entry(f3,textvariable=total,font="arial 12 bold",bd=6,insertwidth=4)
    
    lblcheckin=Label(f3,text="Check In",font="arial 12 bold")    
    textcheckin=Entry(f3,textvariable=checkin,font="arial 12 bold",bd=6,insertwidth=4)
    
    lblcheckout=Label(f3,text="Check Out",font="arial 12 bold")    
    textcheckout=Entry(f3,textvariable=checkout,font="arial 12 bold",bd=6,insertwidth=4)
    
    lblcost.grid(row=10,column=10,padx=5,pady=5)
    lblservice.grid(row=11,column=10,padx=5,pady=5)
    lblgst.grid(row=12,column=10,padx=5,pady=5)
    lblsubtotal.grid(row=13,column=10,padx=5,pady=5)
    lbltotal.grid(row=14,column=10,padx=5,pady=5)
    lblcheckin.grid(row=15,column=10,padx=5,pady=5)
    lblcheckout.grid(row=16,column=10,padx=5,pady=5)
    
    textcost.grid(row=10,column=20,padx=5,pady=5)
    textservice.grid(row=11,column=20,padx=5,pady=5)
    textgst.grid(row=12,column=20,padx=5,pady=5)
    textsubtotal.grid(row=13,column=20,padx=5,pady=5)
    texttotal.grid(row=14,column=20,padx=5,pady=5)
    textcheckin.grid(row=15,column=20,padx=5,pady=5)
    textcheckout.grid(row=16,column=20,padx=5,pady=5)
     
  #---------------------------------------------frame 4-------------------------------------------------       
    
    name=StringVar()
    address=StringVar()
    email=StringVar()
    number=StringVar()
    days=StringVar()
    
    lblname=Label(f4,text="Enter Name",font="arial 12 bold",fg='forest green',justify='right')
    textname=Entry(f4,textvariable=name,font="arial 12 bold",bd=6,insertwidth=4)
    
    lbladdress=Label(f4,text="Enter City",font="arial 12 bold",fg='forest green',justify='right')
    textaddress=Entry(f4,textvariable=address,font="arial 12 bold",bd=6,insertwidth=4)
    
    lblemail=Label(f4,text="Enter Email",font="arial 12 bold",fg='forest green',justify='right')
    textemail=Entry(f4,textvariable=email,font="arial 12 bold",bd=6,insertwidth=4)
    
    lblnumber=Label(f4,text="Enter Phone Number",font="arial 12 bold",fg='forest green',justify='right')
    textnumber=Entry(f4,textvariable=number,font="arial 12 bold",bd=6,insertwidth=4)
    
    lbldays=Label(f4,text="Enter Stay Period(In Days)",font="arial 12 bold",fg='forest green',justify='right')
    textdays=Entry(f4,textvariable=days,font="arial 12 bold",bd=6,insertwidth=4)
    
    lblname.grid(row=1,column=0,padx=5,pady=5)
    lbladdress.grid(row=2,column=0,padx=5,pady=5)
    lblemail.grid(row=3,column=0,padx=5,pady=5)
    lblnumber.grid(row=4,column=0,padx=5,pady=5)    
    lbldays.grid(row=5,column=0,padx=5,pady=5)
    
    textname.grid(row=1,column=3,padx=5,pady=5)
    textaddress.grid(row=2,column=3,padx=5,pady=5)
    textemail.grid(row=3,column=3,padx=5,pady=5)
    textnumber.grid(row=4,column=3,padx=5,pady=5)
    textdays.grid(row=5,column=3,padx=5,pady=5)
    
#---------------------------------------------frame 5-------------------------------------------------
    
    lblchoose=Label(f5,text="Choose Room Type:",font="arial 15 bold italic",fg='blue2',justify='center')
    lblchoose.grid(row=9,column=1,padx=5,pady=7)

    var=IntVar()
    
    royalbt=Radiobutton(f5,text="Royal Suite",font="arial 12 bold", fg='DodgerBlue2',variable=var, value=5000,command=sel)
    luxurybt=Radiobutton(f5,text="Luxury Suite",font="arial 12 bold", fg='DodgerBlue2', variable=var, value=4000,command=sel)
    superiorbt=Radiobutton(f5,text="Superior Suite",font="arial 12 bold", fg='DodgerBlue2', variable=var, value=2000,command=sel)
    deluxebt=Radiobutton(f5,text="Deluxe Suite",font="arial 12 bold", fg='DodgerBlue2', variable=var, value=1500,command=sel)
    
    royalbt.grid(row=10,column=1,padx=5)
    luxurybt.grid(row=10,column=3,padx=5)
    superiorbt.grid(row=11,column=1,padx=10)
    deluxebt.grid(row=11,column=3,padx=5)    
    
#---------------------------------------------frame 6-------------------------------------------------   

    calMonth=StringVar() 
    
    cal = Calendar(f6, selectmode = 'day',
                year = 2020, month = 5,
                day = 22,date_pattern='dd-MM-yyyy')
  
    cal.pack(pady = 20)
  
    def grad_date():
        #date.config(text = "Selected Date is: " + cal.get_date())
        dateof=str(cal.get_date())
        date_dt3 = datetime.strptime(dateof, '%d-%m-%Y')
        dti = pd.date_range(date_dt3, periods = 1)
        
        #print(dti.month)
        global calMonth
        
        if(dti.month==1):
            calMonth='January'
            print(calMonth)
            
        if(dti.month==2):
            calMonth='February'
            print(calMonth)
            
        if(dti.month==3):
            calMonth='March'
            print(calMonth)
            
        if(dti.month==4):
            calMonth='April'
            print(calMonth)
        
        if(dti.month==5):
            calMonth='May'
            print(calMonth)
            
        if(dti.month==6):
            calMonth='June'
            print(calMonth)
            
        if(dti.month==7):
            calMonth='July'
            print(calMonth)
            
        if(dti.month==8):
            calMonth='August'
            print(calMonth)
            
        if(dti.month==9):
            calMonth='September'
            print(calMonth)
        
        if(dti.month==10):
            calMonth='October'
            print(calMonth)
            
        if(dti.month==11):
            calMonth='November'
            print(calMonth)
        
        if(dti.month==12):
            calMonth='December'
            print(calMonth)
        
        # month=cal.see(date_dt3)
        # print(month)
        checkin.set(dateof)
        
    def grad_date_out():
    #date.config(text = "Selected Date is: " + cal.get_date())
        date=str(cal.get_date())
        checkout.set(date)
  
    # Add Button and Label
    Button(f6, text = "CheckIN Date",
            command = grad_date).pack(pady = 20)
    Button(f6, text = "CheckOut Date",
            command = grad_date_out).pack(padx = 10)
      
    #date = Label(f6, text = "")
    #date.pack(pady = 20)
    
    top.mainloop()
    
#-------------------------------------------------Check Out-------------------------------------------    

def dele():
    
    royal='royal'
    luxury='luxury'
    superior='superior'
    deluxe='deluxe'
    
    rnum=Roomno.get()
    
    if rnum>100 and rnum<=104:
        cursor.execute("INSERT INTO rooms(roomtype,room_no)VALUES('{}',{})".format(royal,rnum))
        mycon.commit()
    
    if rnum>200 and rnum<=204:
        cursor.execute("INSERT INTO rooms(roomtype,room_no)VALUES('{}',{})".format(luxury,rnum))
        mycon.commit()
        
    if rnum>300 and rnum<=304:
        cursor.execute("INSERT INTO rooms(roomtype,room_no)VALUES('{}',{})".format(superior,rnum))
        mycon.commit()
        
    if rnum>400 and rnum<=404:
        cursor.execute("INSERT INTO rooms(roomtype,room_no)VALUES('{}',{})".format(deluxe,rnum))
        mycon.commit()
    
    #royal.append(Roomno.get())
    cursor.execute("DELETE FROM customer WHERE name='{}'".format(Name.get()))
    mycon.commit()
    cursor.execute("DELETE FROM cost WHERE name='{}' and room_no={}".format(Name.get(),Roomno.get()))
    mycon.commit()
    
def reset2():
    
    Name.set("")
    Roomno.set("")
    
def Exit2():
    top2.destroy()

def processCheckOut():
    
    global top2,Name,Roomno
    
    top2=Toplevel()
    top2.title("Check Out")
    top2.geometry("800x580+0+0")
    
    F1=Frame(top2)
    F1.pack(side=TOP)
    
    F2=Frame(top2)
    F2.pack(side=TOP)
    
    F3=Frame(top2,pady=55)
    F3.pack(side=TOP)
    
    F4=Frame(top2,padx=10)
    F4.pack(side=TOP)

#-----------------------------------------------------F1----------------------------------------------------
    
    checkoutmsg=Label(F1,text="Check Out",font="arial 20 bold italic",fg='orangered2',justify='center')
    checkoutmsg.grid(pady=20)
    
#-----------------------------------------------------F2----------------------------------------------------    
    
    my_tree=ttk.Treeview(F2)                                   
    my_tree.grid()
    my_tree['columns']=("1","2")
    my_tree.column("1", width = 90,anchor='w')
    my_tree.column("2", width = 90,anchor='w')
    my_tree['show'] = 'headings'
    my_tree.heading("1", text="Name",anchor='w')
    my_tree.heading("2", text="Room No.",anchor='w')
    cursor.execute("SELECT name,room_no FROM cost")
    i=cursor.fetchall()
    for row in i:
        my_tree.insert("", 'end', text ="L1", values =(row[0], row[1]))
    
#-----------------------------------------------------F3----------------------------------------------------
    
    Name=StringVar()
    Roomno=IntVar()
    
    labelname=Label(F3,text="Enter Name:",font="arial 16 bold",fg='forest green')
    labelname.grid(row=1,column=1,padx=5,pady=5)
    entername=Entry(F3,textvariable=Name,font="arial 16 bold",bd=6,insertwidth=4)
    entername.grid(row=1,column=2,padx=5,pady=5)
    labelroom=Label(F3,text="Enter Room No.",font="arial 16 bold",fg='forest green')
    labelroom.grid(row=2,column=1,padx=5,pady=5)
    enterroom=Entry(F3,textvariable=Roomno,font="arial 16 bold",bd=6,insertwidth=4)
    enterroom.grid(row=2,column=2,padx=5,pady=5)
    
#-----------------------------------------------------F4----------------------------------------------------   
    
    deletebt=Button(F4,text="Check Out",font="arial 16 bold",fg='white', bg='orangered2',padx=16,bd=10,width=10,command=dele)
    deletebt.grid(row=1,column=1,padx=10)
    
    resetbt2=Button(F4,text="Reset",font="arial 16 bold",fg='white', bg='orangered2',padx=16,bd=10,width=10,command=reset2)
    resetbt2.grid(row=1,column=2,padx=10)
    
    exitbt=Button(F4,text="Exit",font="arial 16 bold",fg='white', bg='orangered2',padx=16,bd=10,width=10,command=Exit2)
    exitbt.grid(row=1,column=3,padx=10)
    
    top2.mainloop()
#-----------------------------------------------------Exit----------------------------------------------------    

def processExit():
    root.destroy()
    
#-----------------------------------------------------main window----------------------------------------------------
    
checkInbt=Button(frame2,text="Check In",font="arial 15 bold", height=2,width=25, fg='white', bg='orangered2',activebackground="white",bd=10, command=processCheckIn,relief=RAISED)
checkOutbt=Button(frame2,text="Check Out",font="arial 15 bold",height=2,width=25, fg='white',bg='orangered2', command=processCheckOut,bd=10,relief=RAISED)
exitbt=Button(frame2,text="Exit",font="arial 15 bold",height=2,width=25, fg='white',bg='orangered2',bd=10,command=processExit,relief=RAISED)
checkInbt.pack(pady=5)
checkOutbt.pack(pady=5)
exitbt.pack(pady=5)
          
root.mainloop()
