import socket
UDP_IP = '192.168.0.100'
UDP_PORT = 5005
#BUFFER_SIZE = 20  # Normally 1024, but we want fast response
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((UDP_IP, UDP_PORT))
#s.listen(1)
#conn, addr = s.accept()
#print ('Connection address:', addr)
while True:
    data,addr = s.recvfrom(1024)
    #if not data: break
    print ("received data:", data)
    #conn.send(data)  # echo
#conn.close()
