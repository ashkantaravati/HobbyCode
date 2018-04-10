import socket


UDP_IP='192.168.0.100'
UDP_PORT=5005
#BUFFER_SIZE=1024
MESSAGE="hello, World"

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#s.connect((TCP_IP,TCP_PORT))
while True:
    x=input()
    s.sendto(x.encode('UTF-8'),(UDP_IP,UDP_PORT))
#data=s.recv(BUFFER_SIZE)
#s.close()

#print("received data:",data)
