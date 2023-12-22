import dotenv
import os
from server import Server

dotenv.load_dotenv()

HOST = os.getenv("HOST")
PORT = int(os.getenv("PORT"))

server = Server(HOST, PORT)
server.start()