import socket
import threading

def receive_messages():
    while True:
        try:
            # Recevoir les données du serveur
            data = client_socket.recv(1024)
            print(data.decode('utf-8'))
        except:
            break

def send_messages():
    while True:
        # Saisir le message à envoyer
        message = input()
        # Envoyer le message au serveur
        client_socket.send(message.encode('utf-8'))

# Configuration du client
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("0.tcp.eu.ngrok.io", 18579))

# Démarrer deux threads pour gérer la réception et l'envoi des messages
receive_thread = threading.Thread(target=receive_messages)
send_thread = threading.Thread(target=send_messages)

receive_thread.start()
send_thread.start()
