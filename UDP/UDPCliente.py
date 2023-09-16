from socket import *
serverName = "localhost"
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)

while True:
    message = input("Escriba una frase en minúsculas:")

    mayusculas = message.upper()
    if mayusculas == message:
        print("Tu texto ya esta en mayusculas, no es necesario procesarlo")
    else:
        clientSocket.sendto(message.encode(),(serverName, serverPort))
        modifiedMessage, serverAddress = clientSocket.recvfrom(2048)

        print(modifiedMessage.decode())

        clientSocket.close()
        break