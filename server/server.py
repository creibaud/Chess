import socket
import threading

class Server:
    def __init__(self, host, port):
        self.host = host
        self.port = port

        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.clients = {}

    def start(self):
        self.server.bind((self.host, self.port))
        self.server.listen(2)

        print(f"[+] Server is listening on {self.host}:{self.port}")

        while True:
            client, address = self.server.accept()
            print(f"[*] New connection from {address[0]}:{address[1]}")

            name = client.recv(1024).decode("utf-8")
            self.clients[name] = client
            
            thread = threading.Thread(target=self.handle, args=(client,))
            thread.start()

    def handle(self, client):
        while True:
            try:
                data = client.recv(1024)
                if data:
                    self.broadcast(data, client)
            except:
                break
    
    def broadcast(self, data, client=None):
        for name in self.clients:
            if self.clients[name] != client:
                self.clients[name].send(data)

    def stop(self):
        print("[-] Server stopped !")
        self.server.close()