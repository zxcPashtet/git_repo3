import sys
from PyQt6 import uic
import os
import sqlite3
from PyQt6.QtWidgets import QApplication, QMainWindow
from main_2 import Edit
from interface_main import Ui_Form


os.chdir('..')
os.chdir('Data')


class MyWidget(QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        self.connection = sqlite3.connect('coffee.sqlite')
        self.cursor = self.connection.cursor()
        os.chdir('..')
        os.chdir('release')
        self.setupUi(self)
        self.pushButton.clicked.connect(self.render)
        self.pushButton_2.clicked.connect(self.end)

    def render(self):
        name_coffee = self.lineEdit.text()
        result = self.cursor.execute(f"""SELECT id FROM Data WHERE Sort = '{name_coffee}'""").fetchone()
        if result is not None:
            self.label.setText(f'ID: {result[0]}')
            self.label_2.setText('Сорт: ' + self.cursor.execute(f"""SELECT Sort FROM
             Data WHERE id = '{result[0]}'""").fetchone()[0])
            self.label_3.setText('Степень обжарки: ' + self.cursor.execute(f"""SELECT Degree_roasting FROM
             Data WHERE id = '{result[0]}'""").fetchone()[0])
            self.label_4.setText('Вид: ' + self.cursor.execute(f"""SELECT Viev FROM
             Data WHERE id = '{result[0]}'""").fetchone()[0])
            self.label_5.setText('Описание вкуса: ' + self.cursor.execute(f"""SELECT Taste_description FROM
             Data WHERE id = '{result[0]}'""").fetchone()[0])
            self.label_6.setText('Цена: ' + self.cursor.execute(f"""SELECT Price FROM
             Data WHERE id = '{result[0]}'""").fetchone()[0])
            self.label_7.setText('Объём упаковки: ' + self.cursor.execute(f"""SELECT Volume FROM
             Data WHERE id = '{result[0]}'""").fetchone()[0])
        else:
            self.label.setText('ID: Данный сорт кофе не найден в базе данных')
            self.label_2.setText('')
            self.label_3.setText('')
            self.label_4.setText('')
            self.label_5.setText('')
            self.label_6.setText('')
            self.label_7.setText('')

    def end(self):
        print(self)
        self.win = Edit(self)
        self.hide()
        self.win.show()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())