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
      # Receive and decode the message from the client
      message = connectionSocket.recv(1024).decode()
      filename = message.split()[1]
      
      # Open the file requested by the client
      f = open(filename[1:], 'rb')
      outputdata = b"Content-Type: text/html; charset=UTF-8\r\n"
      
      # Send an HTTP header line into socket for a valid request
      response = "HTTP/1.1 200 OK\r\n"
      response += outputdata
      response += "\r\n"
      connectionSocket.send(response.encode())
      
      # Send the content of the requested file to the client
      for i in f:
        connectionSocket.send(i)
      
      # Close the connection socket
      connectionSocket.close()
      
    except IOError:
      # Send response message for invalid request due to the file not being found (404)
      response = "HTTP/1.1 404 Not Found\r\n"
      response += "\r\n"
      connectionSocket.send(response.encode())
      
      # Close the connection socket
      connectionSocket.close()

  # Close the server socket
  serverSocket.close()
  sys.exit()  # Terminate the program after sending the corresponding data

if __name__ == "__main__":
  webServer(13331)
