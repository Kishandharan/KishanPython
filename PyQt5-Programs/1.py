import sys
# from PyQt5-Programs import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QFont

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("This is the freaking thing I was looking for!")
        label1 = QLabel("This is freaking cool!", self)
        label1.setFont(QFont("Consolas", 100))
        label1.setGeometry(0, 0, 2000, 200)
        label1.setStyleSheet("color: #ff7003;"
                            "background-color: black;"
                            "font-style: italic;")
        # Problems in this line - label1.setAlignment(Qt.AlignCenter)
        # Will try to fix later

def main():
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__  == "__main__":
    main()