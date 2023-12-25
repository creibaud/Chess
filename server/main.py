import socket
import threading

def handle_client(client_socket):
    while True:
        try:
            # Recevoir les données du client
            data = client_socket.recv(1024)
            if not data:
                break

            # Envoyer les données à tous les clients connectés
            broadcast(data, client_socket)
        except:
            break

    # Fermer la connexion avec le client
    client_socket.close()

def broadcast(message, author):
    for client in clients:
        if client != author:
            client.send(message)

# Configuration du serveur
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 5555))
server.listen(5)

print("[*] Serveur en attente de connexions sur le port 5555")

# Liste des clients connectés
clients = []

while True:
    # Accepter les connexions des clients
    client, addr = server.accept()
    print(f"[*] Nouvelle connexion acceptée depuis {addr}")

    # Ajouter le client à la liste
    clients.append(client)

    # Démarrer un thread pour gérer le client
    client_handler = threading.Thread(target=handle_client, args=(client,))
    client_handler.start()
