import dotenv
import os
from client import Client

dotenv.load_dotenv()

HOST = os.getenv("HOST")
PORT = int(os.getenv("PORT"))

client = Client(HOST, PORT)
client.connect()