import socket
import json
import subprocess

HEADER = 64 #bytes
PORT = 5050
ADDR = "127.0.0.1"#dunamic
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#server.bind((ADDR, PORT))


def return_services_status(service):
    result = subprocess.run(["systemctl", "show", service, "--no-pager", "--property=ActiveState"], stdout=subprocess.PIPE, text=True)
    #print(result.stdout)
    if ("inactive" in result.stdout):
        return False
    else:
        return True
#    return -1


servtoask="sshd"

ServiceMaxTextLenght = 25

def start():
    #if (return_services_status(servtoask) == True):
    #    print(f"Service [{servtoask}]" + "." *ServiceMaxTextLenght - len(servtoask) + "- \033[32mACTIVE \033[0m")
    #else:
    #    print(f"\033[32mService\033[0m \033[34m[\033[36m{servtoask}\033[34m]\033[90m" + ("." * (ServiceMaxTextLenght - len(servtoask))) + "\033[97m - \033[31mINACTIVE \033[0m")
        ## Move it to client side


    #print(return_services_statuses(service_list))
    server.listen()
    while True:
        conn, addr = server.accept()

        recieved_service_name_lenght = server.recieve(HEADER).decode(FORMAT)
        print(int(recieved_service_name_lenght))
        recieved_service_name = server.recieve(int(recieved_service_name_lenght)).decode(FORMAT)
        print(recieved_service)




        
start()## <---- The hero