import sys, os
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5.QtWidgets import QAbstractButton, QCheckBox, QPushButton
from PyQt5.QtWidgets import QSpinBox

class Breaking_with_Cage(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(os.path.join(os.path.abspath(__file__)[:-4], 'C-main.ui'), self)

        self.spins = {'checkBox_1': self.spinBox_1, 'checkBox_2': self.spinBox_2,
                      'checkBox_3': self.spinBox_3, 'checkBox_4': self.spinBox_4,
                      'checkBox_5': self.spinBox_5, 'checkBox_6': self.spinBox_6,
                      'checkBox_7': self.spinBox_7, 'checkBox_8': self.spinBox_8,
                      'checkBox_9': self.spinBox_9}

        self.checkbox = [self.checkBox_1, self.checkBox_2, self.checkBox_3,
                          self.checkBox_4, self.checkBox_5, self.checkBox_6,
                          self.checkBox_7, self.checkBox_8, self.checkBox_9]

        self.cost = [100, 120, 45, 175, 130, 210, 300, 240, 120]

        self.pos_names = ['Позиция 1', 'Позиция 2', 'Позиция 3', 'Позиция 4', 'Позиция 5',
                          'Позиция 6', 'Позиция 7', 'Позиция 8', 'Позиция 9',]

        self.checkBox_1.stateChanged.connect(self.checked)
        self.checkBox_2.stateChanged.connect(self.checked)
        self.checkBox_3.stateChanged.connect(self.checked)
        self.checkBox_4.stateChanged.connect(self.checked)
        self.checkBox_5.stateChanged.connect(self.checked)
        self.checkBox_6.stateChanged.connect(self.checked)
        self.checkBox_7.stateChanged.connect(self.checked)
        self.checkBox_8.stateChanged.connect(self.checked)
        self.checkBox_9.stateChanged.connect(self.checked)
        self.btn_end.clicked.connect(self.create_receipt)
        self.btn_clear.clicked.connect(self.clear_receipt)

    def checked(self):
        check = self.sender().isChecked()
        name = self.sender().objectName()
        spin = self.spins[name]

        if check and spin.value() == 0:
            spin.setValue(1)
        
        return
    
    def create_receipt(self):
        self.btn_end.setEnabled(False)
        grand_total = 0
        k = len(self.spins)
        rec = ''

        for i in range(k):
            checkbox = 'checkBox_' + str(i+1)
            if self.checkbox[i].isChecked():
                value = str(self.spins[checkbox].value())
                rec += '{}    ({} руб. за 1 шт.)    x{}    ==>>    {} руб.\n'.format(self.pos_names[i], str(self.cost[i]), value, str(self.cost[i] * int(value)))
                grand_total += int(value) * self.cost[i]

        rec += '\n\n\n Общая цена покупки составляет ' + str(grand_total) + ' руб.'
        self.receipt.setPlainText(rec)
        return

    def clear_receipt(self):
        self.receipt.setPlainText('')
        self.btn_end.setEnabled(True)

        k = len(self.spins)
        for i in range(k):
            checkbox = 'checkBox_' + str(i+1)
            self.spins[checkbox].setValue(0)
            self.checkbox[i].setChecked(False)

        return


app = QApplication(sys.argv)
ex = Breaking_with_Cage()
ex.show()
sys.exit(app.exec_())