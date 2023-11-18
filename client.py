# Client.py

# This script contains the client-side logic for the chat application.
# It connects to the server and handles sending and receiving messages.


import socket
import threading
from tkinter import *


# Function to handle sending messages to the server
def send(listbox, entry):
    message_to_server = entry.get()
    listbox.insert('end', "Client: " + message_to_server)
    server_socket.send(bytes(message_to_server, "utf-8"))

# Function to handle receiving messages from the server
def receive(listbox):
    while True:
        message_from_server = server_socket.recv(100)
        if not message_from_server:
            break
        listbox.insert('end', "Server: " + message_from_server.decode("utf-8"))
        if 'bye' in message_from_server.decode("utf-8"):
            break
    server_socket.close()

# Function to set up the client socket and handle message communication
def setup_client():
    global server_socket
    HOST_NAME = socket.gethostname()
    PORT = 1234

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.connect((HOST_NAME, PORT))

    receive_thread = threading.Thread(target=receive, args=(listbox,))
    receive_thread.start()


# GUI setup for the client-side interface
root = Tk()
root.title("Chatbox: Client")

frame = Frame(root)
frame.pack(padx=10, pady=10)

entry = Entry(frame, width=40)
entry.grid(row=0, column=0, padx=5, pady=5)

listbox = Listbox(frame, width=35, height=15)
listbox.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

button = Button(frame, text="Send", width=10, command=lambda: send(listbox, entry))
button.grid(row=0, column=1, padx=5, pady=5)

# Start client setup in a separate thread
setup_thread = threading.Thread(target=setup_client)
setup_thread.start()

root.mainloop()
