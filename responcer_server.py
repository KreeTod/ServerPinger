import socket
import json

HEADER = 64 #bytes
PORT = 5050
ADDR = "127.0.0.1"#dunamic
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR, PORT)

service_list = ["sshd.service"]

def return_services_statuses(service_list):
    for service in service_list:
        result = subprocess.run(["systemctl", "status", service, "--no-pager"], out=subprocess.PIPE, text=True)
        print(out)
    return -1



def start():
    return_services_statuses()
    #server.listen()
    #while True:
    #    conn, addr = server.accept()
        


start()