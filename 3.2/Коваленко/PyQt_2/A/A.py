import sys, csv, os
from PyQt5 import uic
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem, QTextEdit, QMainWindow, QApplication
from PyQt5.QtGui import QColor


class Rating_Table(QMainWindow):

    def __init__(self):
        super().__init__()
        uic.loadUi(os.path.join(os.path.abspath(__file__)[:-4], 'A.ui'), self)
        self.loadTable(os.path.join(os.path.abspath(__file__)[:-4], 'rating.csv'))
        self.colorTable()

    def loadTable(self, table_name):
        with open(table_name, encoding='utf8') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            self.title = next(reader)
            self.title.append('Итоги')
            self.rate_table.setColumnCount(len(self.title))
            self.rate_table.setHorizontalHeaderLabels(self.title)
            self.rate_table.setRowCount(0)
            for i, row in enumerate(reader):
                self.rate_table.setRowCount(self.rate_table.rowCount() + 1)
                count = 0
                for j, elem in enumerate(row):
                    if j > 1 and elem != '':
                        count += int(elem)
                    self.rate_table.setItem(i, j, QTableWidgetItem(elem))
                self.rate_table.setItem(i, len(self.title)-1, QTableWidgetItem(str(count//4)))
            self.rate_table.resizeColumnsToContents()

    def colorTable(self):
        for i in range(self.rate_table.rowCount()):
            item = self.rate_table.item(i, len(self.title)-1).text()
            if int(item) >= 95:
                color = 'green'
            elif int(item) < 95 and int(item) >= 80:
                color = 'gold'
            elif int(item) < 90 and int(item) >= 60:
                color = 'tomato'
            else:
                color = 'white'
            for j in range(self.rate_table.columnCount()):
                self.rate_table.item(i, j).setBackground(QColor(color))

    


app = QApplication(sys.argv)
ex = Rating_Table()
ex.show()
sys.exit(app.exec_())