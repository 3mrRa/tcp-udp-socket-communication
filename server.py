from socket import *

serverPort = 8090

tcpSocket = socket(AF_INET, SOCK_STREAM)


tcpSocket.bind(('', serverPort))

tcpSocket.listen(1)


conn, addr = tcpSocket.accept()

startMsg = conn.recv(1024).decode()
print("TCP:", startMsg)  #Strat


udpSocket = socket(AF_INET, SOCK_DGRAM)


udpSocket.bind(('', serverPort))

wrongOrder = 0
total = 0
expected = 0


while total < 1000000: #UDP
    message, clientAddress = udpSocket.recvfrom(2048)
    number = int(message.decode())

    if number != expected:
        wrongOrder += 1

    total += 1
    expected += 1

print("UDP received:", total)
print("Wrong order:", wrongOrder)


endMsg = conn.recv(1024).decode()
print("TCP:", endMsg)     #End

conn.close()
tcpSocket.close()
udpSocket.close()
