# import socket module
from socket import *
# In order to terminate the program
import sys


def webServer(port=13331):
    serverSocket = socket(AF_INET, SOCK_STREAM)

    # Prepare a server socket
    serverSocket.bind(("", port))

    serverSocket.listen(1)

    while True:
        # Establish the connection
        print('Ready to serve...')
        connectionSocket, addr = serverSocket.accept()

        try:
            message = connectionSocket.recv(1024).decode()
            filename = "helloworld.html"
            f = open(filename, "rb")
            outputdata = b"HTTP/1.1 200 OK\r\n"
            outputdata += b"Content-Type: text/html; charset=UTF-8\r\n\r\n"

            connectionSocket.send(outputdata)

            for i in f:
                connectionSocket.send(i)

            f.close()
            connectionSocket.close()

        except FileNotFoundError:
            outputdata = b"HTTP/1.1 404 Not Found\r\n\r\n"
            connectionSocket.send(outputdata)
            connectionSocket.close()

    serverSocket.close()


if __name__ == "__main__":
    webServer(13331)
