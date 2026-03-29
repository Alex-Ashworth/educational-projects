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
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont

class MainMenuPage(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        
        

        layout = QVBoxLayout()

        title = QLabel("Main Menu")
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
        back_btn = QPushButton("Back to the Main Menu")

        layout.addWidget(title)
        layout.addWidget(back_btn)

        self.setLayout(layout)

        back_btn.clicked.connect(self.go_back)

    def go_back(self):
        self.main_window.stack.setCurrentWidget(self.main_window.main_menu)

class PhrasePage(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        
        layout = QVBoxLayout()

        title = QLabel("Passphrase Generator")
        back_btn = QPushButton("Back to the Main Menu")

        layout.addWidget(title)
        layout.addWidget(back_btn)

        self.setLayout(layout)

        back_btn.clicked.connect(self.go_back)

    def go_back(self):
        self.main_window.stack.setCurrentWidget(self.main_window.main_menu)

class PinPage(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        
        layout = QVBoxLayout()

        title = QLabel("Pin Generator")
        back_btn = QPushButton("Back to the Main Menu")

        layout.addWidget(title)
        layout.addWidget(back_btn)

        self.setLayout(layout)

        back_btn.clicked.connect(self.go_back)

    def go_back(self):
        self.main_window.stack.setCurrentWidget(self.main_window.main_menu)

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
        """)
    window = MainWindow()
    window.show()

    sys.exit(app.exec())