from tkinter import Label,Button,Tk,StringVar,Entry
from os import getcwd,mkdir,chdir
import youtube_dl
from threading import Thread
from PIL import Image,ImageTk
try:
        mkdir("Download")
except FileExistsError:
        pass
t=getcwd()+"\Download"
chdir(t)
def down():
  def Threadin():
    ydl_opts = {
        'format': ' bestvideo[ext=mp4]+bestaudio[ext=mp4]/mp4',
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([str(entrytext.get())])

    tt = "File saved in " + getcwd()
    l4 = Label(text="Downloaded Successfully!!!", bg="#161A27", fg="maroon1", font=20)
    l4.place(x=210, y=310)
    l6=Label(text=tt,bg="#161A27",fg="white")
    l6.place(x=10,y=370)

  l41 = Label(text="Downloading...", bg="#161A27", fg="maroon1", font=20)
  l41.place(x=240, y=310)
  t1=Thread(target=Threadin).start()

root=Tk()
root.title("SMS : Youtube video downloader")
root.geometry("600x400")
root.resizable(0,0)
l1=Label(bg="#161A27",width=400,height=600)
l1.place(x=0,y=0)
l2=Label(text="YOUTUBE VIDEO DOWNLOADER",fg="#42FF62",bg="#161A27",font=("NORMAL bold",22),padx=10,pady=10)
l2.place(x=60,y=50)
l3=Label(text="Paste Link Here :",fg="white",bg="#161A27",font=25)
l3.place(x=250,y=130)
entrytext=StringVar()
e1=Entry(width=39,textvariable=entrytext,border=2,relief="groove",bg="black",font="bold",fg="#29FFF4")
e1.place(x=100,y=170,height=50)
b1=Button(text="Download",command=down,bg="black",borderwidth=3,relief="ridge",font=15,fg="white")
b1.place(x=260,y=240,height=40,width=100)
root.mainloop()