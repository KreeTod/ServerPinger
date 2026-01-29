import socket
import asyncio
import subprocess

HEADER = 64 #bytes
PORT = 5050
ADDR = "127.0.0.1"#dunamic
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONNECT"

#client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

json_temporary_here = [
    {
        "ip" : "228.100.155.0",
        "port" : 49252,
        "services" : [
            "sshd.service"
        ]
    },
    {
        "ip" : "228.100.155.1",
        "port" : 49252,
        "services" : [
            "samba.service",
            "recfaak.service"
        ]
    }
]

# get list of servers
# get first ip and port
# ping ip and port, see that its alive

# ask server for service 1
# wait for responce 2 sec
# recieve and trace responce to console

# ask server for service 2
# wait for responce 2 sec
# recieve and trace responce to console

# ask server for service 3
# wait for responce 2 sec
# recieve and trace responce to console

# ask server for service X
# wait for responce 2 sec
# recieve and trace responce to console

# go to second ip and port and do same steps with it

for item in json_temporary_here:
    print(item["ip"])
    print(item["port"])
    for service in item["services"]:
        print(service)

#client.connect((ADDR, PORT))
#client.close()

def send(msg):
    message = msg.encode(FORMAT)
    msg_lenght = len(message)
    send_lenght = str(msg_lenght).encode(FORMAT)
    send_lenght += b" " * (HEADER - len(send_lenght))
    client.send(send_lenght)
    client.send(message)
    recieved_msg = client.recv(2048).decode(FORMAT)
    print(recieved_msg)
    

#while True():
#    pass


