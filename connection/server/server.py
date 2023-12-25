import socket
import threading

class Server:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.clients = {}
        self.serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    def start(self):
        self.serverSocket.bind((self.host, self.port))
        self.serverSocket.listen()
        print(f"[+] Server is listening on {self.host}:{self.port}")
        while True:
            clientSocket, clientAddress = self.serverSocket.accept()
            print(f"[+] {clientAddress} connected to the server")
            username = clientSocket.recv(1024).decode("utf-8")
            self.clients[clientSocket] = username
            clientThread = threading.Thread(target=self.handleClient, args=(clientSocket,))
            clientThread.start()

    def broadcast(self, message, sender):
        for client in self.clients:
            if client != sender:
                client.sendall(message)
    
    def handleClient(self, clientSocket):
        while True:
            try:
                data = clientSocket.recv(1024)
                if not data:
                    break
                self.broadcast(data, clientSocket)
            except Exception as e:
                print(f"[*] Error: {e}")
                break

        print(f"[-] {self.clients[clientSocket]} disconnected from the server")
        del self.clients[clientSocket]
        clientSocket.close()

    def stop(self):
        self.serverSocket.close()
        print("[-] Server stopped")