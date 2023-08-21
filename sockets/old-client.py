import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#IP and host that we want to connect to 
host = '127.0.0.1'
port = 9002

#connect
s.connect((host,port))
#we are not connected to the sever

#client receiving the data
data = s.recv(1024).decode()
print(data)
s.close()