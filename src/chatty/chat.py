import logging
from threading import Thread

from PySide6.QtCore import QObject, Slot, Signal

from chatty import network


logger = logging.getLogger()


class Chat(QObject):

    on_message = Signal(str)
    on_ready = Signal(bool)

    def __init__(self, addr: str | None=None):
        super().__init__()
        self.addr = addr
        Thread(target=self.chat_loop, daemon=True).start()
    
    def chat_loop(self):
        try:
            if self.addr:
                logger.info(f"Connecting to {self.addr}...")
                self.socket = network.connect(self.addr)
                logger.info("Connection successful")
                self.on_ready.emit(True)
            else:
                logger.info(f"Waiting for connection...")
                server_socket = network.serve()
                self.socket, _ = server_socket.accept()
                logger.info("Connection successful")
                self.on_ready.emit(True)
            while True:
                msg = network.receive(self.socket).decode("utf8")
                self.on_message.emit(msg)
        except Exception as e:
            logger.error(f"Error: {e}")

    @Slot(str)
    def send(self, msg: str):
        network.send(self.socket, msg.encode("utf8"))
    
    