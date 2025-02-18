import sys
from PyQt6 import uic
import sqlite3
from PyQt6.QtWidgets import QApplication, QMainWindow
from interface_main_2 import Ui_Form
import os


#os.chdir('..')
#os.chdir('Data')


class Edit(QMainWindow, Ui_Form):
    def __init__(self, last):
        self.last = last
        super().__init__()
        self.connection = last.connection
        self.cursor = last.connection.cursor()
        #os.chdir('..')
        #os.chdir('release')
        self.setupUi(self)
        self.pushButton.clicked.connect(self.run)
        self.pushButton_2.clicked.connect(self.edit)
        self.pushButton_3.clicked.connect(self.end_edit)
        self.lineEdit_2.setEnabled(False)
        self.lineEdit_3.setEnabled(True)
        self.lineEdit_4.setEnabled(True)
        self.lineEdit_5.setEnabled(True)
        self.lineEdit_6.setEnabled(True)
        self.lineEdit_7.setEnabled(True)
        self.lineEdit_8.setEnabled(True)

    def run(self):
        self.label_8.setText('')
        name_coffee = self.lineEdit.text()
        result = self.cursor.execute(f"""SELECT id FROM Data WHERE Sort = '{name_coffee}'""").fetchone()
        if result is not None:
            self.lineEdit_2.setText(f'{result[0]}')
            self.lineEdit_3.setText(self.cursor.execute(f"""SELECT Sort FROM
             Data WHERE id = '{result[0]}'""").fetchone()[0])
            self.lineEdit_4.setText(self.cursor.execute(f"""SELECT Degree_roasting FROM
             Data WHERE id = '{result[0]}'""").fetchone()[0])
            self.lineEdit_5.setText(self.cursor.execute(f"""SELECT Viev FROM
             Data WHERE id = '{result[0]}'""").fetchone()[0])
            self.lineEdit_6.setText(self.cursor.execute(f"""SELECT Taste_description FROM
             Data WHERE id = '{result[0]}'""").fetchone()[0])
            self.lineEdit_7.setText(self.cursor.execute(f"""SELECT Price FROM
             Data WHERE id = '{result[0]}'""").fetchone()[0])
            self.lineEdit_8.setText(self.cursor.execute(f"""SELECT Volume FROM
             Data WHERE id = '{result[0]}'""").fetchone()[0])
        else:
            self.lineEdit_2.setText('')
            self.lineEdit_3.setText('' + name_coffee)
            self.lineEdit_4.setText('')
            self.lineEdit_5.setText('')
            self.lineEdit_6.setText('')
            self.lineEdit_7.setText('')
            self.lineEdit_8.setText('')

    def edit(self):
        if self.lineEdit_2.text() != '' and self.lineEdit_3.text() != '':
            self.cursor.execute(f"""UPDATE Data
                                SET Sort = '{self.lineEdit_3.text()}',
                                Degree_roasting = '{self.lineEdit_4.text()}',
                                Viev = '{self.lineEdit_5.text()}',
                                Taste_description = '{self.lineEdit_6.text()}',
                                Price = '{self.lineEdit_7.text()}',
                                Volume = '{self.lineEdit_8.text()}' WHERE ID = '{self.lineEdit_2.text()}'""")
            self.connection.commit()
            self.label_8.setText('Запись успешно обновлена')
        else:
            if self.lineEdit_3.text() != '':
                self.cursor.execute(f"""INSERT INTO Data (Sort, Degree_roasting, Viev, Taste_description, Price, Volume)
                                    Values ('{self.lineEdit_3.text()}', '{self.lineEdit_4.text()}',
                                            '{self.lineEdit_5.text()}', '{self.lineEdit_6.text()}',
                                            '{self.lineEdit_7.text()}', '{self.lineEdit_8.text()}')""")
                self.connection.commit()
                self.label_8.setText('Запись успешно добавлена')
            else:
                self.label_8.setText('Нельзя добавить/обновить запись, не указав сорт')

    def end_edit(self):
        self.last.show()
        self.hide()