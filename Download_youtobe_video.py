from tkinter import *
from pytube import YouTube

root = Tk()
root.geometry('400x400')
root.resizable(0,0)
root.title("Youtobe video Downloads")
Label(root,text = 'Youtobe video Downloads',font = 'arial 19 bold').pack()

link = StringVar()
Label(root,text ="Youtobe link past here: ",font = 'arial 15 bold').place(x = 100,y =50)
link_entery = Entry(root,width=70,textvariable =link).place(x = 32, y=90)

def Downloader():
    url =YouTube(str(link.get()))
    video = url.streams.first()
    video.download('E:\\python')
    Label(root,text='Downloaded',font='arial 15').place(x = 100, y = 3)

Button(root,text = 'DOWNLOAD', font = 'arial 15 bold' ,bg = 'pale violet red', padx = 2, command = Downloader).place(x=130 ,y = 150)

root.mainloop()
