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
# is server is sending
data = "This is a test, thank you for connecting to the server"
client.sendall(str.encode(data))
client.close()
print(f'Connection with {addr} has been closed')