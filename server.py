
# Server.py

# This script contains the server-side logic for the chat application.
# It sets up a socket server and handles incoming connections from clients.

import socket
import threading
from tkinter import *

# Function to handle sending messages to the client
def send(listbox, entry):
    message_to_client = entry.get()
    listbox.insert('end', "Server: " + message_to_client)
    client_socket.send(bytes(message_to_client, "utf-8"))

# Function to handle receiving messages from the client
def receive(listbox):
    while True:
        message_from_client = client_socket.recv(100)
        if not message_from_client:
            break
        listbox.insert('end', "Client: " + message_from_client.decode("utf-8"))
        if 'bye' in message_from_client.decode("utf-8"):
            break
    client_socket.close()

# Function to set up the server socket and handle incoming connections
def setup_server():
    global client_socket
    HOST_NAME = socket.gethostname()
    PORT = 1234

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST_NAME, PORT))
    server_socket.listen(4)

    client_socket, address = server_socket.accept()

    receive_thread = threading.Thread(target=receive, args=(listbox,))
    receive_thread.start()


# GUI setup for the server-side interface
root = Tk()
root.title("Chatbox: Server")

frame = Frame(root)
frame.pack(padx=10, pady=10)

entry = Entry(frame, width=40)
entry.grid(row=0, column=0, padx=5, pady=5)

listbox = Listbox(frame, width=35, height=15)
listbox.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

button = Button(frame, text="Send", width=10, command=lambda: send(listbox, entry))
button.grid(row=0, column=1, padx=5, pady=5)

# Start server setup in a separate thread
setup_thread = threading.Thread(target=setup_server)
setup_thread.start()

root.mainloop()
