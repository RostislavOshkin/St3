import sqlite3
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem
from PyQt5 import uic


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        con = sqlite3.connect('coffee.sqlite')
        cur = con.cursor()
        res = cur.execute(f"""Select * from main""").fetchall()

        self.tableWidget.setColumnCount(7)
        self.tableWidget.setHorizontalHeaderLabels([
            "ID",
            "название сорта",
            "степень обжарки",
            "молотый/в зернах",
            "описание вкуса",
            "цена",
            "объем упаковки"])
        for i, row in enumerate(res):
            self.tableWidget.setRowCount(i + 1)
            for j in range(7):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(res[i][j])))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Window()
    w.show()
    sys.exit(app.exec())
