import socket
import asyncio
import subprocess

HEADER = 64 #bytes
PORT = 5050
ADDR = "127.0.0.1"#dunamic
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONNECT"

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((ADDR, PORT))

def send(msg):
    message = msg.encode(FORMAT)
    msg_lenght = len(message)
    send_lenght = str(msg_lenght).encode(FORMAT)
    send_lenght += b" " * (HEADER - len(send_lenght))
    client.send(send_lenght)
    client.send(message)
    recieved_msg = client.recv(2048).decode(FORMAT)
    print(recieved_msg)
    
service_list = [
    "sshd.service"
]

def receive_request():
    pass

def get_service_status(service_name):
    out = subprocess.check_output(
        ["systemctl", "show", "ssh.service", "--no-page"],
        text=True
    )

def send_data_back():
    pass

while True():
    pass


