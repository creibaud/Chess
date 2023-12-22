import socket
import threading

class Client:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.usernames = input("Enter your username: ")
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self):
        self.socket.connect((self.host, self.port))
        self.socket.send(self.usernames.encode())

        print(f"Connected to {self.host}:{self.port} as {self.usernames}")

        receiveHandler = threading.Thread(target=self.handleReceive)
        receiveHandler.start()

        self.sendMessage()

    def handleReceive(self):
        while True:
            try:
                message = self.socket.recv(1024).decode()
                print(message)
            except Exception as e:
                print(f"Error receiving message: {e}")
                break

    def sendMessage(self):
        while True:
            message = input("You : ")
            self.socket.send(message.encode())