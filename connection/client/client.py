import socket
import threading
import sys

class Client:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.username = None
    
    def start(self):
        self.clientSocket.connect((self.host, self.port))
        print(f"[+] Connected to {self.host}:{self.port}")

        self.username = input("Enter your username: ")
        self.clientSocket.sendall(self.username.encode("utf-8"))

        messageReceiver = threading.Thread(target=self.receiveMessage)
        messageReceiver.start()

        messageSender = threading.Thread(target=self.sendMessage)
        messageSender.start()

    def receiveMessage(self):
        while True:
            try:
                data = self.clientSocket.recv(1024)
                print(data.decode("utf-8"))
            except Exception as e:
                print(f"[*] Error: {e}")
                break

    def sendMessage(self):
        while True:
            message = input()
            message = f"{self.username}: {message}"
            if message == "exit":
                break
            self.clientSocket.sendall(message.encode("utf-8"))

        self.clientSocket.close()
    
    def stop(self):
        self.clientSocket.close()
        print("[-] Disconnected from the server")