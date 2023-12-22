import socket
import threading

class Server:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.clients = {}
    
    def start(self):
        self.socket.bind((self.host, self.port))
        self.socket.listen()

        print(f"Server listening on {self.host}:{self.port}")

        while True:
            clientSocket, clientAddress = self.socket.accept()
            print(f"New connection from {clientAddress}")

            nickname = clientSocket.recv(1024).decode()
            self.clients[clientSocket] = nickname

            clientHandler = threading.Thread(target=self.handleClient, args=(clientSocket,))
            clientHandler.start()

    def broadcast(self, message, authorSocket):
        authorNickname = self.clients[authorSocket]
        for clientSocket, nickname in self.clients.items():
            if clientSocket != authorSocket:
                try:
                    clientSocket.send(f"{authorNickname}: {message}".encode())
                except Exception as e:
                    print(f"Error broadcasting message to {nickname}: {e}")
    
    def handleClient(self, clientSocket):
        nickname = self.clients[clientSocket]
        while True:
            try:
                message = clientSocket.recv(1024).decode()
                
                if not message:
                    break
            
                print(f"{nickname}: {message}")
                self.broadcast(message, clientSocket)
            except Exception as e:
                print(f"Error handling client {nickname}: {e}")
                break
        
        print(f"Closing connection from {nickname}")
        del self.clients[clientSocket]
        clientSocket.close()