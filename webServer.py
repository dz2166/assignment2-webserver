# import socket module
from socket import *
# In order to terminate the program
import sys

def webServer(port=13331):
    serverSocket = socket(AF_INET, SOCK_STREAM)
  
    # Prepare a server socket
    serverSocket.bind(("", port))
  
    # Start listening on the serverSocket
    serverSocket.listen(1)

    while True:
        # Establish the connection
        print('Ready to serve...')
        connectionSocket, addr = serverSocket.accept()

        try:
            message = connectionSocket.recv(1024).decode()
            filename = message.split()[1]
      
            # Open the client requested file
            # 'rb' opens the file in binary mode so it can be sent through a socket
            f = open(filename[1:], 'rb')

            # Prepare the header to be sent with the response
            outputdata = b"Content-Type: text/html; charset=UTF-8\r\n"
            
            # Store the header information in the response variable
            response = "HTTP/1.1 200 OK\r\n"
            response += outputdata
            response += "\r\n"
            connectionSocket.send(response.encode())

            # Send the content of the requested file to the client
            for i in f:
                connectionSocket.send(i)
            f.close()

            # Close the connection socket
            connectionSocket.close()

        except IOError:
            # Send response message for file not found (404)
            response = "HTTP/1.1 404 Not Found\r\n\r\n"
            connectionSocket.send(response.encode())

            # Close the client socket
            connectionSocket.close()

    # Close the server socket
    serverSocket.close()
    sys.exit()

if __name__ == "__main__":
    webServer(13331)
