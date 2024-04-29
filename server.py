import socket, threading
connlist = []

def clientsee():
    global server
    server.listen(2)
    while True:
        conn, addr = server.accept()
        print("Client is connect a server.")
        print(f"ipv4 ip addr : {addr}")
        connlist.append(conn)
        threading.Thread(target=clientrecvsee, args=[conn, addr,]).start()

def sendallcleint(msg):
    global connlist
    print(f"Sending msg all client. msg : {msg}")
    for conn in connlist:
        conn.send(msg.encode())
    print(f"Sending msg all client good.")

def clientrecvsee(conn, addr):
    while True:
        data = conn.recv(1024).decode()
        print(f"client [{addr}] is sending by server a msg [{data}].")
        sendallcleint(data)

if __name__ == "__main__":
    host = "192.168.0.13"
    port = 5050
    server = socket.socket()
    server.bind((host, port))
    print("Server is binding now.")
    print("Wait client connect..")
    clientsee()