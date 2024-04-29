import socket
import threading

def senddataclient(msg):
    global client
    client.send(msg.encode())

def recvdatasee():
    global client
    while True:
        data = client.recv(1024).decode()
        print(data)

def chatsend():
    global client, name
    while True:
        msg = input("")
        client.send(f"{name} : {msg}".encode())

if __name__ == "__main__":
    host = "192.168.0.13"
    port = 5050
    client = socket.socket()
    client.connect((host, port))
    print("Connect a server now.")
    print("Inputing your name.")
    name = input(">>")
    threading.Thread(target=chatsend).start()
    recvdatasee()