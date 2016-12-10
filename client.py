import socket
from Tkinter import *
import time

top = Tk()
top.wm_title("TCP/IP Socket Application: Client")
fHeader = Frame(top)
lMessage = Label(fHeader, text = "Write your message")
eMessage = Entry(fHeader)
tResponse = Text(top)

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverAddress = socket.gethostname()
port = 8611
clientSocket.connect((serverAddress, port))

def sendMessage():
    data = eMessage.get()
    clientSocket.send(data)
    data = clientSocket.recv(1024)
    tResponse.insert(END,time.strftime("%H:%M:%S", time.gmtime()) + '  ' + data)

bSend = Button(fHeader, text = "Send", command = sendMessage)


fHeader.pack(side = 'top')
lMessage.pack(side = 'left')
eMessage.pack(side = 'left')
bSend.pack(side = 'left')
tResponse.pack()

top.mainloop()




