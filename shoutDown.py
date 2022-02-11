from tkinter import *
import os
def restart():
    os.system("shutdown/r")

def Re_Time():
    os.system("shutdown/r /t 20")
def LogOut():
    os.system("shutdown /l")
def ShutDown():
    os.system("shutdown/s")


st = Tk()
st.title("system shout Down")
st.geometry('400x400')
st.config(bg="pink")
Button(st,text="Restart",font=("Time New Roman",27,"bold"),
       relief=RAISED,cursor="plus",command=restart).place(x=130,y=50,height=50,width=160)

Button(st,text="Re_Time",font=("Time New Roman",25,"bold"),
       relief=RAISED,cursor="plus",command=Re_Time).place(x=130,y=130,height=50,width=160)

Button(st,text="Log-Out",font=("Time New Roman",25,"bold"),
       relief=RAISED,cursor="plus",command=LogOut).place(x=130,y=210,height=50,width=160)

Button(st,text="ShutDown",font=("Time New Roman",21,"bold"),
       relief=RAISED,cursor="plus",command=ShutDown).place(x=130,y=290,height=50,width=160)



st.mainloop()
# R_button