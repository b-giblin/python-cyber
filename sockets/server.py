import socket

#socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#host and port
host = '127.0.0.1'
port = 9002
#bind
#set up to take connections
s.bind((host, port))
s.listen()
client, addr = s.accept()
#We now have someone connected
print(f'Connection recieved from {addr}')
while True:
    data = input("Enter a message:  ")
    client.sendall(str.encode(data))
    msg = client.recv(1024).decode()
    if not msg:
        break
    print(msg)
    
client.close()

