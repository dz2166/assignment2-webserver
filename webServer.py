# import socket module
from socket import *
# In order to terminate the program
import sys


def webServer(port=13331):
    serverSocket = socket(AF_INET, SOCK_STREAM)

    # Prepare a server socket
    serverSocket.bind(("", port))

    # Fill in start
    serverSocket.listen(1)
    # Fill in end

    while True:
        # Establish the connection
        print('Ready to serve...')
        connectionSocket, addr = serverSocket.accept()

        try:
            message = connectionSocket.recv(1024).decode()
            filename = "helloworld.html"

            # opens the client requested file.
            # Plenty of guidance online on how to open and read a file in python. How should you read it though if you plan on sending it through a socket?
            f = open(filename[1:], "rb")

            outputdata = b"HTTP/1.1 200 OK\r\n"
            outputdata += b"Content-Type: text/html; charset=UTF-8\r\n\r\n"

            # Send an HTTP header line into socket for a valid request.
            connectionSocket.send(outputdata)

            # Send the content of the requested file to the client
            for i in f:  # for line in file
                connectionSocket.send(i)

            f.close()  # close the file

            # Closing the connection socket after sending the file
            connectionSocket.close()

        except Exception as e:
            # Send response message for invalid request due to the file not being found (404)
            outputdata = b"HTTP/1.1 404 Not Found\r\n\r\n"
            connectionSocket.send(outputdata)

            # Close client socket
            connectionSocket.close()

     
        
    serverSocket.close()


if __name__ == "__main__":
    webServer(13331)
