from server import Server

host = str(input("Enter the host: "))
port = int(input("Enter the port: "))
server = Server(host, port)
server.start()