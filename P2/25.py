import socket
hostname =  socket.gethostname()
addr = socket.gethostbyname(hostname)
print(hostname)
print(addr)