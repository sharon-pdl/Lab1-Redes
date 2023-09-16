#Cliente (client.py):

#python
#Copy code
import socket

# Configuración del cliente
host = "127.0.0.1"
port = 12345

# Crear un socket TCP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conectar al servidor
client_socket.connect((host, port))

# Enviar un mensaje al servidor
message = "Hola, servidor!"
client_socket.send(message.encode())

# Recibir la respuesta del servidor
response = client_socket.recv(1024).decode()
print(f"Respuesta del servidor: {response}")

# Cerrar la conexión con el servidor
client_socket.close()