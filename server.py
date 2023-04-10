import socket
from threading import Thread
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
import os
import time
import ftplib
import ntpath


IP_ADDRESS='127.0.0.1'
PORT= 8050
SERVER= None
BUFFER_SIZE= 4096
Clients= {}


def setup ():
    print('\n\t\t\t\t\t\tIP MESSENGER\n')

    # Getting global values
    global PORT
    global IP_ADDRESS
    global SERVER

    SERVER = socket. socket (socket .AF_INET, socket.SOCK_STREAM)
    SERVER.bind((IP_ADDRESS, PORT))

    SERVER. listen (100)

    print ("\t\t\t\tSERVER IS WAITING FOR INCOMMING CONNECTIONS...")
    print("\n")

def acceptconnections():
    global SERVER
    global Clients

    while True:
        client, addr= SERVER.accept()
        client_name= client.recv(4096).decode().lower()
        Clients[client_name] = {
                'client'       : client,
                'address'      : addr,
                'connected_with': "",
                'file_name'    : "",
                'file_size'   : 4096
        }
    print(f'connection established with {client_name} : {addr}')

    thread= Thread(target= handleClient, args= (client,client_name,))
    thread.start()


def ftp():
    global IP_ADDRESS
    
    authorizer =DummyAuthorizer ()
    authorizer.add_user ("lftpd","lftpd",".",perm= "elradfw")

    handler = FTPHandler
    handler.authorizer = authorizer

    ftp_server = FTPServer ((IP_ADDRESS,21),handler)
    ftp_server.serve_forever()

setup_thread = Thread(target=setup)
setup_thread.start()

ftp_thread = Thread(target=ftp)
ftp_thread.start ()

is_dir_exists = os.path.isdir('shared_files')
print (is_dir_exists)
if(not is_dir_exists):
    os.makedirs('shared_files')

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

    song_counter= song_counter+1
    listbox.insert(song_counter,fname)


def download():
    song_to_download=1istbox.get(ANCHOR)
    infoLabel.configure(text="Downloading "+ song_to_download)

    HOSTNAME = "127.0.0.1"
    USERNAME = 'lftpd'
    PASSWORD = 'lftpd'

    home = str(Path.home())
    download_path=home+"/Downloads"
    ftp_server = ftplib.FTP(HOSTNAME, USERNAME, PASSWORD)
    ftp_server.encoding= "utf-8"
    ftp_server.cwd('shared files')
    local_filename = os.path.join (download_path, song_to_download)
    file = open(local_filename, 'wb')
    ftp_server.retrbinary('RETR '+ song_to_download, file.write)
    ftp_server.dir()
    file.close()
    ftp_server.quit ()
    infoLabel.configure(text='Download Complete')
    time.sleep (1)
    if (song_selected!= ""):
        infolabel.configure(text='Now Playing'+ song_selected)
    else:
        infolabel.configure(text='')



def setup ():
    print('\n\t\t\t\t\t\tIP MESSENGER\n')


    # Getting global values
    global PORT
    global IP_ADDRESS
    global SERVER

    SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER.bind((IP_ADDRESS, PORT))

    SERVER. Listen (100)

    print('\t\t\t\tSERVER IS WAITING FOR INCONMING CONNECTIONS...')
    print ("\n")


    acceptconnections ()

setup_thread = Thread (target=setup) #receiving multiple messages
setup_thread.start()