from tkinter import *
import speedtest
def speedDekho():
    sp = speedtest.Speedtest()

    sp.get_servers()
    Down = str(round(sp.download()/(10**6),3))+"Mbps"
    Up = str(round(sp.upload()/(10**6),3))+"Mbps"
    lab_down.config(text= Down)
    lab_upload.config(text= Up)

sp = Tk()
sp.title("check internet speed ")
sp.geometry("600x600")
sp.config(bg="pink")
lab = Label(sp,text="Internet Speed Test",font=("Time New Roman",30,"bold"),bg="#BCA19B",fg="pink",relief=RAISED,cursor="plus")
lab.place(x=110,y=40)

lab = Label(sp,text="Download speed",font=("Time New Roman",30,"bold"),bg="#BCA19B",fg="pink",relief=RAISED,cursor="plus")
lab.place(x=100,y=130,height=50,width=390)

lab_down = Label(sp,text="00",font=("Time New Roman",30,"bold"),bg="#BCA19B",fg="pink",relief=RAISED,cursor="plus")
lab_down.place(x=100,y=200,height=50,width=390)

lab = Label(sp,text="Upload Speed",font=("Time New Roman",30,"bold"),bg="#BCA19B",fg="pink",relief=RAISED,cursor="plus")
lab.place(x=100,y=280,height=50,width=390)
#
lab_upload = Label(sp,text="00",font=("Time New Roman",30,"bold"),bg="#BCA19B",fg="pink",relief=RAISED,cursor="plus")
lab_upload.place(x=100,y=360,height=50,width=390)


Button=Button(sp,text="Check",font=("Time New Roman",25,"bold"),bg="pink",fg="#BCA19B",relief=RAISED,cursor="plus",command=speedDekho)
Button.place(x=225,y=500,height=50,width=160)


sp.mainloop()
