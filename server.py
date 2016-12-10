import socket
from Tkinter import *
from threading import Thread
import time

top = Tk()
top.wm_title("TCP/IP Socket Application: Server")
lMessage = Label(top, text = 'Message from client')
tMessage = Text(top)
lMessage.pack()
tMessage.pack()

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverAddress = socket.gethostname()
port = 8611
serverSocket.bind((serverAddress, port))
serverSocket.listen(5)

class worker(Thread):
    def run(self):
        clientSocket, clientAddress = serverSocket.accept()
        while True:
            try:
                data = clientSocket.recv(1024)
            except socket.error, e:
                tMessage.insert(END, time.strftime("%H:%M:%S", time.gmtime()) + '  Client is disconnected\r\n')
                break
            else:
                tMessage.insert(END, time.strftime("%H:%M:%S", time.gmtime()) + '  ' + data + '\r\n')
                clientSocket.send(data + " from server\r\n")
                time.sleep(1)

def startApplication():
    worker().start()

top.after(1, startApplication())
top.mainloop()



