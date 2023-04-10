import socket
from threading import Thread
from playsound import playsound
import pygame
from pygame import mixer 
import os
import time
import ftplib
import ftplib import FTP 
import ntpath
from pathlib import path 

global song_counter
song_counter=0

PORT= 8050
IP_ADDRESS='127.0.0.1'
SERVER=None
BUFFER_SIZE=4096

def setup():
    global SERVER
    global PORT
    global IP_ADDRESS

    SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER.connect((IP_ADDRESS, PORT))   

setup()

from tkinter import *
from tkinter import ttk
from tkinter import filedialog

window= Tk()
window.title('Music Window')
window.geometry('300x300')
window.configure(bg='LightSkyBlue')

selectlabel = Label(window, text="Select Song",bg='LightSkyBlue', font = ("Calibri",0)) 
selectlabel.place(x=2, y=1)

listbox=Listbox(window, height=10, width=39, activestyle = 'dotbox',bg='LightSkyBlue',borderwidth=2, font=("Calibri",10)) 
listbox.place(x=10,y=18)

scrollbar1 = Scrollbar(listbox)
scrollbar1.place(relheight=1,relx=1)
scrollbar1.config(command = listbox.yview)

PlayButton=Button (window, text="Play", width=10,bd=1,bg="SkyBlue", font=("Calibri",10))
PlayButton.place(x=30,y=200)

Stop=Button (window, text="stop",bd=1,width=10,bg="SkyBlue", font = ("Calibri",10)) 
Stop.place (x=200,y=200)

Upload=Button (window, text="Upload",width=10,bd=1,bg='SkyBlue', font=("Calibri",10)) 
Upload.place (x=30,y=250)

Download =Button (window, text="Download", width=10,bd=1,bg="SkyBlue", font = ("Calibri",10)) 
Download.place (x=200,y=250)

infoLabel= Label(window, text="",fg= "blue", font=("Calibri",8))
infoLabel.place (x=4, y=280)


window.mainloop()

for file in os.listdir('shared_files'):
    filename= os.fsdecode(file)
    listbox.insert(song_counter,filename)
    song_counter= song_counter+1

def play():
    global song_selected
    song_selected= listbox.get(ANCHOR)

    pygame
    mixer.init()
    mixer.music.load('shared_files/'+song_selected)
    mixer.music.play()
    if (song_selected !=""):
        infoLabel.configure(text= 'Now Playing: '+song_selected)
    else:
        infoLabel.configure(text="")


playButton= Button(window,text= 'play',width= 10,bd= 1,bg='SkyBlue',font= ('Calibiri',10),command=play)
playButton.place(x=10,y=200)

def stop():
    global song_selected
    pygame
    mixer.init()
    mixer.music.load('shared_files/'+song_selected)
    mixer.music.pause()
    infoLabel.configure(text="") 

Stop= Button(window,text= 'stop',width= 10,bd= 1,bg='SkyBlue',font= ('Calibiri',10),command=stop)
Stop.place(x=200,y=200)

def resume():
    global song_selected
    mixer.init()
    mixer.music.load('shared_files/'+song_selected)
    mixer.music.play()    

def pause():
    global song_selected
    mixer.init()
    mixer.music.load('shared_files/'+song_selected)
    mixer.music.pause()    

resumeButton= Button(window,text= 'resume',width= 10,bd= 1,bg='SkyBlue',font= ('Calibiri',10),command=resume)
resumeButton.place(x=30,y=250)

pauseButton= Button(window,text= 'pause',width= 10,bd= 1,bg='SkyBlue',font= ('Calibiri',10),command=pause)
pauseButton.place(x=200,y=250)


def browseFiles():
   global listbox
   global song_counter
   global filePathLabel

try:
    filename = filedialog.askopenfilename ()
    HOSTNAME = "127.0.0.1"
    USERNAME = 'lftpd'
    PASSWORD = 'lftpd'

    ftp_server = FTP (HOSTNAME, USERNAME, PASSWORD)
    ftp_server.encoding = "utf-8"
    ftp_server.cwd('shared_files')
    fname=ntpath.basename(filename)
    with open (filename, 'rb') as file:
        ftp_server.storbinary(f'STOR {fname}', file)

    ftp_server.dir()
    ftp_server.quit ()

except FileNotFoundError:
    print ("Cancel Button Pressed")

def setup():
    global PORT
    global IP_ADDRESS
    global SERVER

    SERVER = socket. socket (socket .AF_INET, socket.SOCK_STREAM)
    SERVER.connect((IP_ADDRESS, PORT))   

    window()

setup() 