import threading
import socket
import json
def read_config():
    '''Read configuration return json data '''
    file = open("client.json", "r")
    return json.loads(file.read())
def data_recv(client):
    while True:
        data = client.recv(1024)
        data =data.decode()
        if (data!=''):
            print("recvdata: ", data)
        data=b''
try:
    config = read_config()
    config_addr = config["IPaddr"]
    config_port = config["Port"]
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((config_addr, config_port))
    print_recv = threading.Thread(target=data_recv, args=(client,))
    print_recv.start()#持续监听服务端发送数据
    while True:
        pass
except:
    client.close()
