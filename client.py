from socket import *
import time

serverName = "127.0.0.1"
serverPort = 8090


TCP_clientSocket = socket(AF_INET, SOCK_STREAM)
TCP_clientSocket.connect((serverName, serverPort))

TCP_clientSocket.send("START".encode())
time.sleep(0.1) 

# UDP socket
UDP_clientSocket = socket(AF_INET, SOCK_DGRAM)

for i in range(1000000):
    UDP_clientSocket.sendto(str(i).encode(), (serverName, serverPort))





TCP_clientSocket.send("END".encode())
TCP_clientSocket.close()
UDP_clientSocket.close()
