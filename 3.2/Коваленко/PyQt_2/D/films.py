# -*- coding: utf-8 -*-
import sys, sqlite3
from PyQt5 import uic
import os
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem, QTextEdit, QMainWindow, QApplication
from random import randint


class Films_Table(QMainWindow):

    def __init__(self):
        super().__init__()
        uic.loadUi(os.path.join(os.path.abspath(__file__)[:-8], 'films.ui'), self)
        self.btn.clicked.connect(self.finded)
        self.db_address = os.path.join(os.path.abspath(__file__)[:-8], 'films.db')

        #self.con = sqlite3.connect(r'C:\Users\denis\Desktop\Программирование\Коваленко\PyQt-2\B\films.db')
        #self.cur = con.cursor()
        #self.con.close()
  
    
    def finded(self):
        con = sqlite3.connect(self.db_address)
        cur = con.cursor()
        result = []
        if self.line.toPlainText() != '':
            result.append(cur.execute("""
                            SELECT Films.title AS ft, year, genres.title AS gt, duration FROM Films, genres
                            WHERE ft LIKE :line AND genre = genres.id
                            """, {'line': '%'+self.line.toPlainText()+'%'}).fetchall())
        if self.year.toPlainText() != '':
            if self.yearBox.currentText() == 'В':
                result.append(cur.execute("""
                            SELECT Films.title AS ft, year, genres.title AS gt, duration FROM Films, genres
                            WHERE year = :year AND genre = genres.id
                            """, {'year': self.year.toPlainText()}).fetchall())
            elif self.yearBox.currentText() == 'ДО':
                result.append(cur.execute("""
                            SELECT Films.title AS ft, year, genres.title AS gt, duration FROM Films, genres
                            WHERE year <= :year AND genre = genres.id
                            """, {'year': self.year.toPlainText()}).fetchall())
            else:
                result.append(cur.execute("""
                                SELECT Films.title AS ft, year, genres.title AS gt, duration FROM Films, genres
                                WHERE year >= :year AND genre = genres.id
                                """, {'year': self.year.toPlainText()}).fetchall())
        if self.comboBox.currentText() != '':
            result.append(cur.execute("""
                            SELECT Films.title AS ft, year, genres.title AS gt, duration FROM Films, genres
                            WHERE Films.genre = (SELECT id FROM genres WHERE genres.title = ?)
                            AND genres.title = ?
                            """, (self.comboBox.currentText().lower(), self.comboBox.currentText().lower())).fetchall())
        result.append(cur.execute("""
                            SELECT Films.title AS ft, year, genres.title AS gt, duration FROM Films, genres
                            WHERE duration BETWEEN ? AND ? AND genre = genres.id
                            """, (self.spin_begin.value(), self.spin_end.value())).fetchall())
        con.close()
        rez = frozenset(result[0])
        for i in range(1, len(result)):
            rez = rez & frozenset(result[i])
        rez = list(rez)
        result = []
        if len(rez) <= 20:
            result = rez
        else:
            for i in range(20):
                elem = rez.pop(randint(0, len(rez)-1))
                result.append(elem) 
        title = ['title', 'year', 'genre', 'duration']
        self.films_table.setColumnCount(len(title))
        self.films_table.setHorizontalHeaderLabels(title)
        self.films_table.setRowCount(0)
        self.films_table.setColumnCount(len(title))
        self.films_table.setHorizontalHeaderLabels(title)
        self.films_table.setRowCount(0)
        for i in range(len(result)):
            self.films_table.setRowCount(self.films_table.rowCount() + 1)
            for j in range(len(result[i])):
                self.films_table.setItem(i, j, QTableWidgetItem(str(result[i][j])))
        self.films_table.resizeColumnsToContents()

        



app = QApplication(sys.argv)
ex = Films_Table()
ex.show()
sys.exit(app.exec_())