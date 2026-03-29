import sys
from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QStackedWidget,
    QLineEdit,
)
from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import QFont
from password_tool.config import *
from password_tool.core.pass_generator import *
from password_tool.core.phrase_generator import *
from password_tool.core.pin_generator import *

class MainMenuPage(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        
        layout = QVBoxLayout()

        title = QLabel("Password Toolkit")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("""
            QLabel {
                font-size: 22px;
                font-weight: bold;
                color: white;
                background-color: #2a2a2a;
                padding: 12px;
                margin-bottom: 10px;
            }
        """)

        open_pass_btn = QPushButton("Password Generator")
        open_phrase_btn = QPushButton("Passphrase Generator")
        open_pin_btn = QPushButton("Pin Generator")
        quit_btn = QPushButton("Quit")

        layout.addWidget(title)
        layout.addWidget(open_pass_btn)
        layout.addWidget(open_phrase_btn)
        layout.addWidget(open_pin_btn)
        layout.addWidget(quit_btn)

        self.setLayout(layout)

        open_pass_btn.clicked.connect(self.open_pass_page)
        open_phrase_btn.clicked.connect(self.open_phrase_page)
        open_pin_btn.clicked.connect(self.open_pin_page)
        quit_btn.clicked.connect(QApplication.quit)

    def open_pass_page(self):
        self.main_window.stack.setCurrentWidget(self.main_window.pass_page)

    def open_phrase_page(self):
        self.main_window.stack.setCurrentWidget(self.main_window.phrase_page)
    
    def open_pin_page(self):
        self.main_window.stack.setCurrentWidget(self.main_window.pin_page)


class PassPage(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        
        layout = QVBoxLayout()

        title = QLabel("Password Generator")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("""
            QLabel {
                font-size: 22px;
                font-weight: bold;
                color: white;
                background-color: #2a2a2a;
                padding: 12px;
                margin-bottom: 10px;
            }
        """)
        self.gen_btn = QPushButton("Generate Passphrase")
        self.output = QLineEdit()
        self.output.setAlignment(Qt.AlignCenter)
        self.output.setReadOnly(True)
        self.copy_btn = CopyButton(self.output)
        back_btn = BackButton(self.main_window, self.output)

        layout.addWidget(title)
        layout.addWidget(self.output)
        layout.addWidget(self.gen_btn)
        layout.addWidget(self.copy_btn)
        layout.addWidget(back_btn)

        self.setLayout(layout)

        self.gen_btn.clicked.connect(self.gen_pass)

    def gen_pass(self):
        password = generate_password()
        self.output.setText(password)

class PhrasePage(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        
        layout = QVBoxLayout()

        title = QLabel("Passphrase Generator")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("""
            QLabel {
                font-size: 22px;
                font-weight: bold;
                color: white;
                background-color: #2a2a2a;
                padding: 12px;
                margin-bottom: 10px;
            }
        """)
        
        self.gen_btn = QPushButton("Generate Passphrase")
        self.output = QLineEdit()
        self.output.setAlignment(Qt.AlignCenter)
        self.output.setReadOnly(True)
        self.copy_btn = CopyButton(self.output)
        back_btn = BackButton(self.main_window, self.output)

        layout.addWidget(title)
        layout.addWidget(self.output)
        layout.addWidget(self.gen_btn)
        layout.addWidget(self.copy_btn)
        layout.addWidget(back_btn)

        self.setLayout(layout)

        self.gen_btn.clicked.connect(self.gen_phrase)

    def gen_phrase(self):
        passphrase = generate_passphrase()
        self.output.setText(passphrase)

class PinPage(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        
        layout = QVBoxLayout()

        title = QLabel("Pin Generator")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("""
            QLabel {
                font-size: 22px;
                font-weight: bold;
                color: white;
                background-color: #2a2a2a;
                padding: 12px;
                margin-bottom: 10px;
            }
        """)
        
        self.gen_btn = QPushButton("Generate Pin Code")
        self.output = QLineEdit()
        self.output.setAlignment(Qt.AlignCenter)
        self.output.setReadOnly(True)
        self.copy_btn = CopyButton(self.output)
        back_btn = BackButton(self.main_window, self.output)

        layout.addWidget(title)
        layout.addWidget(self.output)
        layout.addWidget(self.gen_btn)
        layout.addWidget(self.copy_btn)
        layout.addWidget(back_btn)

        self.setLayout(layout)

        self.gen_btn.clicked.connect(self.gen_pin)


    def gen_pin(self):
        pin = generate_pin()
        self.output.setText(pin)

class BackButton(QPushButton):
    def __init__(self, main_window, source_widget=None, text="Back to the Main Menu"):
        super().__init__(text)
        self.main_window = main_window
        self.source_widget = source_widget
        self.clicked.connect(self.go_back)
    
    def go_back(self):
        if self.source_widget is not None:
            self.source_widget.clear()
        self.main_window.stack.setCurrentWidget(self.main_window.main_menu)
class CopyButton(QPushButton):
    def __init__(self, source_widget, text="Copy"):
        super().__init__(text)
        self.source_widget = source_widget
        self.clicked.connect(self.copy_text)

    def copy_text(self):
        text = self.source_widget.text().strip()
        if text:
            QApplication.clipboard().setText(text)
            self.setText("Copied!")
            QTimer.singleShot(1500, lambda: self.setText("Copy"))
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Password Tool Shiz")
        self.setFixedSize(400, 250)

        self.stack = QStackedWidget()

        self.main_menu = MainMenuPage(self)
        self.pass_page = PassPage(self)
        self.phrase_page = PhrasePage(self)
        self.pin_page = PinPage(self)

        self.stack.addWidget(self.main_menu)
        self.stack.addWidget(self.pass_page)
        self.stack.addWidget(self.phrase_page)
        self.stack.addWidget(self.pin_page)
        
        layout = QVBoxLayout()
        layout.addWidget(self.stack)
        self.setLayout(layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyleSheet("""
            QWidget {
                background-color: #2a2a2a;
            }

            QPushButton {
                background-color: #3a3a3a;
                color: white;
                border: 1px solid #666666;
                border-radius: 8px;
                padding: 8px;
            }

            QPushButton:hover {
                background-color: #2c2c2c;
            }

            QLineEdit {
                background-color: #1f1f1f;
                color: white;
                border: 1px solid #555555;
                border-radius: 8px;
                padding: 8px;
                selection-background-color: #5a5a5a
            }
        """)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())