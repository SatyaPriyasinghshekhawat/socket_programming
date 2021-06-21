import socket
socket.socket()
s=socket.socket (socket.AF_INET,socket,SOCK_DGRAM)
recv_add=("127.0.0.1",9999)
user_data=input("enter your message:-")
newdata=user.data.encode('ascii')
s.senderto(new_data, recv_addr)
print("your msg has been send..")