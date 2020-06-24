import sys, os
from PyQt5 import uic
from PyQt5.QtWidgets import QTextBrowser, QTextEdit, QMainWindow, QApplication


class TextBrowser(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(os.path.join(os.path.abspath(__file__)[:-4], 'A.ui'), self)
        self.textEdit.textChanged.connect(self.translated_text)

    def translated_text(self):
        text = self.sender().toPlainText()
        self.textBrowser.setHtml(text)
        return

app = QApplication(sys.argv)
ex = TextBrowser()
ex.show()
sys.exit(app.exec_())