# Python Socket Programming

This is a simple socket programming project I made while learning networking and cybersecurity.

The project has a Python client and a Bash server that uses Netcat.

## Files

* `client.py` - Python client that connects to the server
* `server.sh` - Starts a Netcat server on port 5000

## How to run

First, give the server permission:

```bash
chmod +x server.sh
```

Start the server:

```bash
./server.sh
```

Then, in another terminal, run the client:

```bash
python3 client.py
```

The client connects to:

```text
127.0.0.1:5000
```

## What I learned

* How sockets work
* TCP connections
* IP addresses and ports
* Client and server communication
* Using Netcat
* Basic Python socket programming
