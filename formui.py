# Form implementation generated from reading ui file 'addEditCoffeeForm.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class FormUI(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(689, 600)
        MainWindow.setStyleSheet("QLabel{\n"
"font-size:18px;}")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.sortname_edit = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.sortname_edit.setGeometry(QtCore.QRect(30, 140, 141, 31))
        self.sortname_edit.setObjectName("sortname_edit")
        self.roast_level_edit = QtWidgets.QSpinBox(parent=self.centralwidget)
        self.roast_level_edit.setGeometry(QtCore.QRect(30, 180, 61, 31))
        self.roast_level_edit.setMaximum(999999999)
        self.roast_level_edit.setObjectName("roast_level_edit")
        self.coffee_grind_edit = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.coffee_grind_edit.setGeometry(QtCore.QRect(30, 230, 141, 31))
        self.coffee_grind_edit.setObjectName("coffee_grind_edit")
        self.description_edit = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.description_edit.setGeometry(QtCore.QRect(30, 280, 141, 31))
        self.description_edit.setObjectName("description_edit")
        self.price_edit = QtWidgets.QSpinBox(parent=self.centralwidget)
        self.price_edit.setGeometry(QtCore.QRect(30, 330, 61, 31))
        self.price_edit.setMaximum(999999999)
        self.price_edit.setObjectName("price_edit")
        self.mass_edit = QtWidgets.QSpinBox(parent=self.centralwidget)
        self.mass_edit.setGeometry(QtCore.QRect(30, 370, 61, 31))
        self.mass_edit.setMaximum(999999999)
        self.mass_edit.setObjectName("mass_edit")
        self.id_edit = QtWidgets.QSpinBox(parent=self.centralwidget)
        self.id_edit.setGeometry(QtCore.QRect(30, 90, 61, 31))
        self.id_edit.setMaximum(999999999)
        self.id_edit.setObjectName("id_edit")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(120, 90, 47, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(200, 150, 91, 21))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(120, 190, 91, 21))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(190, 230, 101, 31))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(190, 270, 101, 31))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(120, 330, 101, 31))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(120, 370, 101, 31))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(20, 20, 221, 41))
        self.label_8.setStyleSheet("font-size:25px;")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(440, 20, 231, 41))
        self.label_9.setStyleSheet("font-size:25px;")
        self.label_9.setObjectName("label_9")
        self.sortname_create = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.sortname_create.setGeometry(QtCore.QRect(500, 80, 141, 31))
        self.sortname_create.setObjectName("sortname_create")
        self.description_create = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.description_create.setGeometry(QtCore.QRect(500, 220, 141, 31))
        self.description_create.setObjectName("description_create")
        self.price_create = QtWidgets.QSpinBox(parent=self.centralwidget)
        self.price_create.setGeometry(QtCore.QRect(580, 270, 61, 31))
        self.price_create.setMaximum(999999999)
        self.price_create.setObjectName("price_create")
        self.coffee_grind_create = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.coffee_grind_create.setGeometry(QtCore.QRect(500, 170, 141, 31))
        self.coffee_grind_create.setObjectName("coffee_grind_create")
        self.mass_create = QtWidgets.QSpinBox(parent=self.centralwidget)
        self.mass_create.setGeometry(QtCore.QRect(580, 310, 61, 31))
        self.mass_create.setMaximum(999999999)
        self.mass_create.setObjectName("mass_create")
        self.roast_level_create = QtWidgets.QSpinBox(parent=self.centralwidget)
        self.roast_level_create.setGeometry(QtCore.QRect(580, 120, 61, 31))
        self.roast_level_create.setMaximum(999999999)
        self.roast_level_create.setObjectName("roast_level_create")
        self.update_btn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.update_btn.setGeometry(QtCore.QRect(30, 480, 141, 51))
        self.update_btn.setStyleSheet("font-size:17px;")
        self.update_btn.setObjectName("update_btn")
        self.create_btn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.create_btn.setGeometry(QtCore.QRect(500, 360, 141, 51))
        self.create_btn.setStyleSheet("font-size:17px;")
        self.create_btn.setObjectName("create_btn")
        self.error_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.error_label.setGeometry(QtCore.QRect(260, 400, 181, 51))
        self.error_label.setStyleSheet("color:orange;\n"
"font-size:19px;\n"
"text-align: justify;\n"
"justify-content: center;")
        self.error_label.setText("")
        self.error_label.setObjectName("error_label")
        self.label_10 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(480, 120, 91, 21))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(390, 170, 101, 31))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(520, 310, 51, 31))
        self.label_12.setObjectName("label_12")
        self.label_14 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(400, 90, 91, 21))
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(520, 270, 41, 31))
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(390, 210, 101, 31))
        self.label_16.setObjectName("label_16")
        self.success_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.success_label.setGeometry(QtCore.QRect(250, 460, 231, 71))
        self.success_label.setStyleSheet("color:rgb(145, 255, 143);\n"
"font-size:19px;\n"
"text-align: justify;\n"
"justify-content: center;")
        self.success_label.setText("")
        self.success_label.setObjectName("success_label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 689, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "id"))
        self.label_2.setText(_translate("MainWindow", "sort_name"))
        self.label_3.setText(_translate("MainWindow", "roast_level"))
        self.label_4.setText(_translate("MainWindow", "coffee_grind"))
        self.label_5.setText(_translate("MainWindow", "description"))
        self.label_6.setText(_translate("MainWindow", "price"))
        self.label_7.setText(_translate("MainWindow", "mass"))
        self.label_8.setText(_translate("MainWindow", "Изменение данных"))
        self.label_9.setText(_translate("MainWindow", "Добавление данных"))
        self.update_btn.setText(_translate("MainWindow", "Обновить!"))
        self.create_btn.setText(_translate("MainWindow", "Создать!"))
        self.label_10.setText(_translate("MainWindow", "roast_level"))
        self.label_11.setText(_translate("MainWindow", "coffee_grind"))
        self.label_12.setText(_translate("MainWindow", "mass"))
        self.label_14.setText(_translate("MainWindow", "sort_name"))
        self.label_15.setText(_translate("MainWindow", "price"))
        self.label_16.setText(_translate("MainWindow", "description"))
