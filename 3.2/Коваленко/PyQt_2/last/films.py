# -*- coding: utf-8 -*-
import sys, sqlite3
import os
from pathlib import Path
from PyQt5 import uic
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem, QTextEdit, QMainWindow, QApplication, QWidget
from random import randint


class Films_Table(QMainWindow):

    def __init__(self):
        super().__init__()
        uic.loadUi(os.path.join(os.path.abspath(__file__)[:-8], 'films.ui'), self)
        self.btn.clicked.connect(self.finded)
        self.btn_save.clicked.connect(self.saved)
        self.db_address = os.path.join(os.path.abspath(__file__)[:-8], 'films.db')
        self.btn_create.clicked.connect(self.created)
    
    def finded(self):
        con = sqlite3.connect(self.db_address)
        cur = con.cursor()
        result = []
        if self.line.toPlainText() != '':
            result.append(cur.execute("""
                            SELECT Films.id AS fi, Films.title AS ft, year, genres.title AS gt, duration FROM Films, genres
                            WHERE ft LIKE :line AND genre = genres.id
                            """, {'line': '%'+self.line.toPlainText()+'%'}).fetchall())
        if self.year.toPlainText() != '':
            if self.yearBox.currentText() == 'В':
                result.append(cur.execute("""
                            SELECT Films.id AS fi, Films.title AS ft, year, genres.title AS gt, duration FROM Films, genres
                            WHERE year = :year AND genre = genres.id
                            """, {'year': self.year.toPlainText()}).fetchall())
            elif self.yearBox.currentText() == 'ДО':
                result.append(cur.execute("""
                            SELECT Films.id AS fi, Films.title AS ft, year, genres.title AS gt, duration FROM Films, genres
                            WHERE year <= :year AND genre = genres.id
                            """, {'year': self.year.toPlainText()}).fetchall())
            else:
                result.append(cur.execute("""
                                SELECT Films.id AS fi, Films.title AS ft, year, genres.title AS gt, duration FROM Films, genres
                                WHERE year >= :year AND genre = genres.id
                                """, {'year': self.year.toPlainText()}).fetchall())
        if self.comboBox.currentText() != '':
            result.append(cur.execute("""
                            SELECT Films.id AS fi, Films.title AS ft, year, genres.title AS gt, duration FROM Films, genres
                            WHERE Films.genre = (SELECT id FROM genres WHERE genres.title = ?)
                            AND genres.title = ?
                            """, (self.comboBox.currentText().lower(), self.comboBox.currentText().lower())).fetchall())
        result.append(cur.execute("""
                            SELECT Films.id AS fi, Films.title AS ft, year, genres.title AS gt, duration FROM Films, genres
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
        self.result = result
        title = ['title', 'year', 'genre', 'duration']
        self.films_table.setColumnCount(len(title))
        self.films_table.setHorizontalHeaderLabels(title)
        self.films_table.setRowCount(0)
        self.films_table.setColumnCount(len(title))
        self.films_table.setHorizontalHeaderLabels(title)
        self.films_table.setRowCount(0)
        for i in range(len(result)):
            self.films_table.setRowCount(self.films_table.rowCount() + 1)
            for j in range(1, len(result[i])):
                self.films_table.setItem(i, j-1, QTableWidgetItem(str(result[i][j])))
        self.films_table.resizeColumnsToContents()

        if len(result) != 0 and not self.btn_save.isEnabled():
            self.btn_save.setEnabled(True)
        elif len(result) == 0:
            self.btn_save.setEnabled(False)           


    def saved(self):
        con = sqlite3.connect(self.db_address)
        cur = con.cursor()

        for i in range(self.films_table.rowCount()):
            arguments = []
            for j in range(self.films_table.columnCount()):
                arguments.append(self.films_table.item(i, j).text())
            genre = list(cur.execute("""
                                SELECT id FROM genres
                                WHERE title = :title
                                """, {'title':arguments[2].lower()}).fetchone())
            if arguments[-1] == '' or not all(symb in '0123456789' or symb == '' for symb in arguments[1]) or arguments[0] == '' or not all(symb in '0123456789' for symb in arguments[-1]) or arguments[0] == '':
                self.error_form = Errors(self, 'Возникла ошибка. Измененные данные некорректны.')
                self.error_form.show()
                return
            elif int(arguments[1]) < 0 or int(arguments[-1]) < 0:
                self.error_form = Errors(self, 'Возникла ошибка. Измененные данные некорректны.')
                self.error_form.show()
                con.close()
                return
            else:
                cur.execute("""
                            UPDATE Films
                            SET title = ?, genre = ?, year = ?, duration = ?
                            WHERE id = ?
                            """, (arguments[0], str(genre[-1]), str(arguments[1]), str(arguments[-1]), str(self.result[i][0])))
                con.commit()
        con.close()


    def created(self):
        self.create_film = CreateFilm(self, self.db_address)
        self.create_film.show()




class CreateFilm(QWidget):

    def __init__(self, *args):
        super().__init__()
        uic.loadUi(os.path.join(os.path.abspath(__file__)[:-8], 'created.ui'), self)
        self.args = args
        self.buttons = self.btnBox.buttons()
        self.buttons[1].clicked.connect(self.closed)
        self.buttons[0].clicked.connect(self.checked)

    def closed(self):
        self.close()

    def checked(self):
        new_record = []
        if self.name.toPlainText() != '':
            new_record.append(self.name.toPlainText())
            if all(symb in '0123456789' for symb in self.year.toPlainText()) or self.year.toPlainText() == '':
                new_record.append(self.year.toPlainText())
                if all(symb in '0123456789' for symb in self.duration.toPlainText()) and self.duration.toPlainText() != '':
                    if not any(symb in '0123456789' for symb in self.genre.toPlainText()) or self.genre.toPlainText() == '':
                        new_record.append(self.genre.toPlainText())
                        new_record.append(self.duration.toPlainText())
                        self.check = check(self, new_record)
                        self.check.show()
                        return
        self.error_form = Errors(self, 'Возникла ошибка. Введенные данные не корректны')
        self.error_form.show()


        
class Errors(QWidget):

    def __init__(self, *args):
        super().__init__()
        uic.loadUi(os.path.join(os.path.abspath(__file__)[:-8], 'errors.ui'), self)
        self.lbl.setText(args[-1])
        self.btn_close.clicked.connect(self.closed)

    def closed(self):
        self.close()       
    


class check(QWidget):

    def __init__(self, *args):
        super().__init__()
        uic.loadUi(os.path.join(os.path.abspath(__file__)[:-8], 'check.ui'), self)
        self.args = args
        
        self.name.setText(self.name.text() + args[1][0])
        self.year.setText(self.year.text() + args[1][1])
        self.genre.setText(self.genre.text() + args[1][2])
        self.duration.setText(self.duration.text() + args[1][3])

        self.buttons = self.btnBox.buttons()
        self.db_address = os.path.join(os.path.abspath(__file__)[:-8], 'films.db')
        self.buttons[0].clicked.connect(self.created)
        self.buttons[1].clicked.connect(self.closed)

    def closed(self):
        self.close()

    def created(self):
        name, year, genre, duration = self.args[1]
        con = sqlite3.connect(self.db_address)
        cur = con.cursor()
        genre = list(cur.execute("""
                            SELECT id FROM genres
                            WHERE title = :genre
                            """, {'genre': genre.lower()}).fetchone())
        if genre == '':
            genre = cur.execute("""
                                SELECT COUNT(*) FROM genres
                                """)
            cur.execute("""
                        INSERT INTO genres(id, title) VALUES(?, ?)
                        """, (str(int(genre[0])+1), str(name)))
            con.commit()
        cur.execute("""
                    INSERT INTO Films(title, year, genre, duration) VALUES(?, ?, ?, ?)
                    """, (name, year, str(genre[0]), str(duration)))
        con.commit()
        self.close()
        self.args[0].close()




app = QApplication(sys.argv)
ex = Films_Table()
ex.show()
sys.exit(app.exec_())