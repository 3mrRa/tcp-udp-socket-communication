# TCP & UDP Socket Communication Test

A Python client-server networking project that demonstrates TCP connection management and UDP datagram transmission through a practical packet-sequence monitoring experiment.

## Overview

The client establishes a TCP connection with the server, sends a `START` control message, transmits **1,000,000 numbered UDP datagrams**, and finally sends an `END` control message over TCP.

While receiving UDP datagrams, the server counts the packets and compares each received sequence number with the next expected number.

This project illustrates an important distinction between the two transport protocols:

- **TCP** provides a connection-oriented, reliable, ordered byte stream.
- **UDP** sends connectionless datagrams and does not guarantee delivery or ordering.

## Project Structure

```text
tcp-udp-socket-communication/
├── client.py   # Sends TCP control messages and UDP datagrams
├── server.py   # Receives traffic and monitors packet sequence
└── README.md
```

## Requirements

- Python 3.8 or newer (the code uses only Python's standard library).
- Two terminal windows on the same machine, or suitable network configuration if adapting the project for different hosts.

No third-party packages are required.

## How It Works

### 1. Server

1. Creates a TCP socket and listens on port `8090`.
2. Accepts a client connection.
3. Receives and prints the TCP `START` message.
4. Creates a UDP socket and binds it to port `8090`.
5. Receives 1,000,000 UDP datagrams.
6. Converts each datagram's payload to an integer and compares it with the expected sequence number.
7. Prints the total received count and the number of sequence mismatches.
8. Receives and prints the TCP `END` message, then closes the sockets.

### 2. Client

1. Connects to the server at `127.0.0.1:8090` over TCP.
2. Sends the `START` control message.
3. Waits briefly before creating the UDP socket.
4. Sends the integers `0` through `999999` as UDP datagrams.
5. Sends the `END` control message over TCP and closes both sockets.

## Run the Project

Clone the repository:

```bash
git clone https://github.com/3mrRa/tcp-udp-socket-communication.git
cd tcp-udp-socket-communication
```

**Terminal 1 — Start the server first:**

```bash
python server.py
```

**Terminal 2 — Start the client:**

```bash
python client.py
```

On systems where Python is invoked as `python3`, use `python3` instead.

## Example Output

A possible server output is:

```text
TCP: START
UDP received: 1000000
Wrong order: 0
TCP: END
```

The values shown are illustrative; actual results depend on runtime and network conditions.

## Understanding the Results

- **UDP received:** Number of UDP datagrams processed by the server.
- **Wrong order:** Number of times a received number differs from the next expected sequence number.

A non-zero mismatch count can result from datagrams arriving out of order or being lost. This counter is a simple sequence-mismatch indicator; it is not a complete measurement of packet loss or network performance.

## Important Notes & Limitations

- The client is configured to connect to `127.0.0.1`, so the project runs locally by default.
- Both sockets use port `8090`, but TCP and UDP have separate transport-layer port spaces.
- UDP does not guarantee delivery, ordering, or retransmission.
- The server waits until it has processed exactly 1,000,000 UDP datagrams before reading the TCP `END` message. If UDP datagrams are lost, the server may wait indefinitely.
- The current implementation is a learning experiment, not a production-ready protocol or benchmarking tool.

## Concepts Demonstrated

- Client-server architecture
- Python socket programming
- TCP connection setup and teardown
- UDP datagram transmission and reception
- Sequence-number checking
- Differences between reliable streams and connectionless datagrams

---

**Topics:** Python · Computer Networks · Socket Programming · TCP · UDP
