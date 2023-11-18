# Chat Application using Sockets, Multi-Threading and Tkinter

This repository contains a simple chat application built using Python's socket module for network communication and Tkinter for the graphical user interface.

## Setup

### Prerequisites
    Python 3.x
## Installation
### 1. Clone the repository:
    git clone https://github.com/rohitreddy192/Chat-Application.git

### 2. Navigate to the project directory:
    cd Chat-Application

### 3. Run the server:
    python server.py

### 4. Run the client:
    python client.py


## Files
### Server.py
#### Description
  The server.py script contains the server-side logic for the chat application. It sets up a socket server, listens for incoming connections from clients, and handles message communication between clients.

#### Functions
  1. send(listbox, entry): Sends messages from the server to the connected client.
  2. receive(listbox): Receives messages from the connected client and displays them in the GUI.
  3. setup_server(): Binds to a port, listens for incoming connections, and starts a receiving thread for each client.

### Client.py
#### Description
  The client.py script contains the client-side logic for the chat application. It connects to the server, sends and receives messages, and displays them in the graphical user interface.

#### Functions
  1. send(listbox, entry): Sends messages from the client to the connected server.
  2. receive(listbox): Receives messages from the server and displays them in the GUI.
  3. setup_client(): Connects to the server, starts a receiving thread, and handles message sending.

## Usage
  1. Run server.py to start the server.
  2. Run client.py to start the client and connect to the server.

## Contributing
  Contributions are welcome! If you'd like to contribute to this project, please fork the repository and submit a pull request.
