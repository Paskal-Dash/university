import sys, os
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5.QtWidgets import QAbstractButton, QLineEdit, QPushButton


class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'Калькулятор'
        self.status = 0         #0 - The button was still not called, 1 - The button was still called
        uic.loadUi(os.path.join(os.path.abspath(__file__)[:-4], 'B.ui'), self)
        self.btn_0.clicked.connect(self.press_numb)
        self.btn_1.clicked.connect(self.press_numb)
        self.btn_2.clicked.connect(self.press_numb)
        self.btn_3.clicked.connect(self.press_numb)
        self.btn_4.clicked.connect(self.press_numb)
        self.btn_5.clicked.connect(self.press_numb)
        self.btn_6.clicked.connect(self.press_numb)
        self.btn_7.clicked.connect(self.press_numb)
        self.btn_8.clicked.connect(self.press_numb)
        self.btn_9.clicked.connect(self.press_numb)
        self.btn_dot.clicked.connect(self.press_numb)
        self.btn_add.clicked.connect(self.press_oper)
        self.btn_sub.clicked.connect(self.press_oper)
        self.btn_div.clicked.connect(self.press_oper)
        self.btn_mult.clicked.connect(self.press_oper)
        self.btn_equal.clicked.connect(self.Decision)
        self.btn_clear.clicked.connect(self.press_oper)
        self.btn_back.clicked.connect(self.press_oper)
        self.btn_right_bracket.clicked.connect(self.press_bracket)
        self.btn_left_bracket.clicked.connect(self.press_bracket)

    def press_numb(self):
        numb = self.sender().text()
        textbox = self.expression_line.text()
        if not self.status:
            if textbox == '0' and numb != '.':
                if numb != '0':
                    self.expression_line.setText(numb)
            elif (numb == '.' and not textbox[-1] in '().*/+-') or (textbox != '0' and numb != '.'):
                self.expression_line.setText(textbox + numb)
        else:
            if numb == '.':
                self.expression_line.setText('0.')
            else:
                self.expression_line.setText(numb)
            self.status = 0
        return  

    def press_oper(self):
        operator = self.sender().text()
        textbox = self.expression_line.text()
        if self.status:
            if operator == 'C' or operator == 'Back':
                self.status = 0
                self.expression_line.setText('0')
        elif operator == 'C':
            self.expression_line.setText('0')
        elif operator == 'Back':
            if textbox != '0' and len(textbox) != 1:
                self.expression_line.setText(textbox[:-1])
            elif  len(textbox) == 1:
                self.expression_line.setText('0')
        elif operator in '+-*/':
            self.expression_line.setText(textbox + operator)
        return

    def press_bracket(self):
        bracket = self.sender().text()
        textbox = self.expression_line.text()
        if not self.status:
            self.status = 0
            self.expression_line.setText(textbox + bracket)
        else:
            self.expression_line.setText(bracket)
        return

    def Decision(self):
        textbox = self.expression_line.text()
        self.status = 1
        try:
            ans = str(eval(textbox))
        except Exception:
            ans = 'Некорректное выражение'

        self.expression_line.setText(ans)




app = QApplication(sys.argv)
ex = Calculator()
ex.show()
sys.exit(app.exec_())