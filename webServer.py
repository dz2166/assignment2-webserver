# import socket module
from socket import *
# In order to terminate the program
import sys


def webServer(port=13331):
    serverSocket = socket(AF_INET, SOCK_STREAM)

    # Prepare a server socket
    serverSocket.bind(("", port))

    # Listen for incoming connections
    serverSocket.listen(1)

    while True:
        # Establish the connection
        print('Ready to serve...')
        connectionSocket, addr = serverSocket.accept()

        try:
            # Receive the client request message
            message = connectionSocket.recv(1024).decode()

            # Extract the requested filename from the message
            filename = "helloworld.html"

            # Open the file and read its contents
            with open(filename, "rb") as f:
                file_data = f.read()

            # Build the HTTP response message
            response_header = b"HTTP/1.1 200 OK\r\n"
            response_header += b"Content-Type: text/html; charset=UTF-8\r\n"
            response_header += b"Content-Length: " + str(len(file_data)).encode() + b"\r\n"
            response_header += b"\r\n"

            # Send the HTTP response message header to the client
            connectionSocket.send(response_header)

            # Send the file contents to the client
            connectionSocket.send(file_data)

            # Close the connection socket
            connectionSocket.close()

        except Exception as e:
            # Send a 404 response message for invalid requests
            error_message = b"<html><body><h1>404 Not Found</h1></body></html>"
            response_header = b"HTTP/1.1 404 Not Found\r\n"
            response_header += b"Content-Type: text/html; charset=UTF-8\r\n"
            response_header += b"Content-Length: " + str(len(error_message)).encode() + b"\r\n"
            response_header += b"\r\n"
            response_data = response_header + error_message

            # Send the HTTP response message to the client
            connectionSocket.send(response_data)

            # Close the connection socket
            connectionSocket.close()

    serverSocket.close()


if __name__ == "__main__":
    webServer(13331)
