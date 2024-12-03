import sqlite3
import sys
from mainui import MainUI
from formui import FormUI
from PyQt6.QtWidgets import QApplication
from PyQt6.QtWidgets import QMainWindow, QTableWidgetItem


class DBSample(QMainWindow, MainUI):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.create_or_edit.clicked.connect(self.add_or_edit)
        self.update_info.clicked.connect(self.select_data)
        # По умолчанию будем выводить все данные из таблицы films
        self.select_data()

    def select_data(self):
        self.connection = sqlite3.connect("data/coffee.sqlite")
        # Получим результат запроса,
        # который ввели в текстовое поле
        res = self.connection.cursor().execute("SELECT * FROM coffee").fetchall()
        # Заполним размеры таблицы
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setHorizontalHeaderLabels(
            ['ID', 'название сорта', 'степень обжарки', 'молотый/в зернах', 'описание вкуса', 'цена', 'объем упаковки'])
        # Заполняем таблицу элементами
        for i, row in enumerate(res):
            self.tableWidget.setRowCount(
                self.tableWidget.rowCount() + 1)
            for j, elem in enumerate(row):
                self.tableWidget.setItem(
                    i, j, QTableWidgetItem(str(elem)))
        self.connection.close()

    def add_or_edit(self):
        self.second_form = AddUpdateBtn()
        self.second_form.show()


class AddUpdateBtn(QMainWindow, FormUI):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.update_btn.clicked.connect(self.update_bd)
        self.create_btn.clicked.connect(self.create_bd)

    def update_bd(self):
        self.error_label.setText('')
        self.success_label.setText('')
        if not (self.id_edit.value() and self.sortname_edit.text() and self.roast_level_edit.value() and
                self.coffee_grind_edit.text() and self.description_edit.text() and self.price_edit.value() and self.mass_edit.value()):
            self.error_label.setText('Заполните все поля')
            return
        con = sqlite3.connect('data/coffee.sqlite')
        # Выполнение запроса и изменение никнейма и любимого предмета
        con.cursor().execute(f"""UPDATE coffee
                                 SET sort_name = '{self.sortname_edit.text()}',
                                 roast_level = {self.roast_level_edit.value()},
                                 coffee_grind = '{self.coffee_grind_edit.text()}',
                                 description = '{self.description_edit.text()}',
                                 price = {self.price_edit.value()},
                                 mass = {self.mass_edit.value()}
                                 WHERE id = {self.id_edit.value()}""")
        con.commit()
        con.close()
        self.success_label.setText('Успешно!')

    def create_bd(self):
        self.error_label.setText('')
        self.success_label.setText('')
        if not (self.sortname_create.text() and self.roast_level_create.value() and
                self.coffee_grind_create.text() and self.description_create.text() and self.price_create.value()
                and self.mass_create.value()):
            self.error_label.setText('Заполните все поля')
            return
        con = sqlite3.connect('data/coffee.sqlite')
        con.cursor().execute(f"""Insert into coffee(sort_name, roast_level, coffee_grind, description, price, mass)
                                Values('{self.sortname_create.text()}',
                                        {self.roast_level_create.value()},
                                        '{self.coffee_grind_create.text()}',
                                        '{self.description_create.text()}',
                                        {self.price_create.value()},
                                        {self.mass_create.value()})""")
        con.commit()
        con.close()
        self.success_label.setText('Успешно!')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = DBSample()
    ex.show()
    sys.exit(app.exec())
