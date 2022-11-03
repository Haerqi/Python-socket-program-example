import socket
import threading
from xml.sax.saxutils import prepare_input_source
import threadpool
import time
import json
def send_message(msg):
    """发送数据给所有客户端"""
    for i in connect_list:
        i.sendall(msg.encode())

def read_config():
    '''Read configuration return json data '''
    file = open("server.json", "r")
    return json.loads(file.read())
def send_welcome(conn):
    conn.sendall(("连接成功 "+config_welcome).encode())
def wait_for_connection(server):
    server.listen(2048)
    while True:
        
        conn,addr = server.accept()
        print(addr,"连接")
        send_welcome(conn)
        connect_list.append(conn)
        addr_list.append(addr)
def show_connections():
    while True:
        time.sleep(10)
        if (addr_list == []):
            print("无客户端连接")
            continue
        print("客户端：")
        for i in addr_list:
            print(i,end="\t")
def now_time():
    while True:
        time.sleep(10)
        current_time = int(time.time())
        current_time = time.localtime(current_time)
        print(time.strftime('%Y:%m:%d %H:%M:%S',current_time))
try:
    connect_list=[]
    addr_list=[]
    config = read_config()
    config_addr = config["IPaddr"]
    config_port = config["Port"]
    config_welcome = config["welcome"]
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((config_addr, config_port))
    time_thread = threading.Thread(target=now_time)
    time_thread.start()#计时器
    waiting = threading.Thread(target=wait_for_connection, args=(server,))
    waiting.start()#持续等待连接进程
    showing = threading.Thread(target=show_connections, args=())
    showing.start()#持续显示连接数量进程
    while True:
        pass
except:
    server.close()