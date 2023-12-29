import socket
import threading

class Client:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.name = ""

        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.enemyMoves = []

    def setName(self, name):
        self.name = name

    def start(self):
        self.client.connect((self.host, self.port))
        self.client.send(self.name.encode("utf-8"))

        thread = threading.Thread(target=self.handle)
        thread.start()

    def sendPosition(self, id, position):
        data = f"{id}:{position}"
        self.client.send(data.encode("utf-8"))

    def handle(self):
        while True:
            data = self.client.recv(1024)
            if data:
                self.enemyMoves.append(data.decode("utf-8"))

    def stop(self):
        self.client.close()