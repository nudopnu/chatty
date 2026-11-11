import sys
import logging
from argparse import ArgumentParser

from PySide6.QtWidgets import QMainWindow, QApplication, QWidget, QVBoxLayout, QHBoxLayout, QTextEdit, QLineEdit, QPushButton
from PySide6.QtCore import Signal, Slot

from chatty.chat import Chat


logger = logging.getLogger()
logger.setLevel(logging.INFO)


class MainWindow(QMainWindow):

    message = Signal(str)
    log = Signal(str)
    

    def __init__(self):
        super().__init__()
        root = QWidget()
        main = QVBoxLayout()
        self.setCentralWidget(root)

        self.te_console = QTextEdit()
        self.te_console.setReadOnly(True)
        self.le_chat = QLineEdit()
        self.le_chat.setDisabled(True)
        self.le_chat.returnPressed.connect(lambda: self.message.emit(self.le_chat.text()))
        self.btn_submit = QPushButton("send")
        self.btn_submit.setDisabled(True)
        self.btn_submit.clicked.connect(lambda: self.message.emit(self.le_chat.text()))
        controls = QHBoxLayout()
        controls.addWidget(self.le_chat)
        controls.addWidget(self.btn_submit)
        main.addWidget(self.te_console)
        main.addLayout(controls)

        self.message.connect(print)
        self.log.connect(self.te_console.append)

        root.setLayout(main)
        self.setWindowTitle("Chatty")
        self.show()
    
    @Slot()
    def enable(self):
        self.btn_submit.setEnabled(True)
        self.le_chat.setEnabled(True)
    
    def add_msg(self, msg: str, outgoing=True):
        prefix = ">" if outgoing else "<"
        self.te_console.append(f"{prefix} {msg}")


def parse_args():
    parser = ArgumentParser()
    parser.add_argument("--remote", "-r", required=False)
    return parser.parse_args()


def main() -> None:

    app = QApplication(sys.argv)
    window = MainWindow()
    handler = logging.Handler()
    handler.emit = lambda record: window.log.emit(handler.format(record))
    logger.addHandler(handler)

    args = parse_args()
    chat = Chat(args.remote)
    window.message.connect(chat.send)
    chat.on_message.connect(lambda msg: window.add_msg(msg, False))
    chat.on_ready.connect(window.enable)

    app.exec()
