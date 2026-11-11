import struct
import logging 
import socket


log = logging.getLogger()


HOST = "0.0.0.0"
PORT = 9999
PACKET_SIZE = 1024


def serve():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen()
    log.info(f"Listening on {HOST}:{PORT}")
    return s


def connect(host: str, port=PORT):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    return s


def send(s: socket.socket, message: bytes):
    length = struct.pack("!I", len(message))
    s.sendall(length + message)


def receive(s: socket.socket):
    [length] = struct.unpack("!I", __recv_exact(s, 4))
    return __recv_exact(s, length)


def __recv_exact(s: socket.socket, size: int) -> bytes:
    data = bytearray()

    while len(data) < size:
        chunk = s.recv(size - len(data))

        if not chunk:
            raise ConnectionError("Connection closed")

        data.extend(chunk)

    return bytes(data)