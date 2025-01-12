from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import serial.tools.list_ports as portlist
import serial
import threading
from datetime import datetime

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.resize(1567, 863)
        MainWindow.setAutoFillBackground(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(40, 20, 841, 91))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.groupBox)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 821, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.comboBox_selectMotor = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        self.comboBox_selectMotor.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.comboBox_selectMotor.setFont(font)
        self.comboBox_selectMotor.setEditable(False)
        self.comboBox_selectMotor.setObjectName("comboBox_selectMotor")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/motor.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.comboBox_selectMotor.addItem(icon, "")
        self.comboBox_selectMotor.addItem(icon, "")
        self.comboBox_selectMotor.addItem(icon, "")
        self.comboBox_selectMotor.addItem(icon, "")
        self.comboBox_selectMotor.addItem(icon, "")
        self.comboBox_selectMotor.addItem(icon, "")
        self.comboBox_selectMotor.addItem(icon, "")
        self.comboBox_selectMotor.addItem(icon, "")
        self.horizontalLayout.addWidget(self.comboBox_selectMotor)
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.checkBox = QtWidgets.QCheckBox(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.checkBox.setFont(font)
        self.checkBox.setAutoFillBackground(False)
        self.checkBox.setObjectName("checkBox")
        self.horizontalLayout.addWidget(self.checkBox)
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.doubleSpinBox.setFont(font)
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.horizontalLayout.addWidget(self.doubleSpinBox)
        self.doubleSpinBox_2 = QtWidgets.QDoubleSpinBox(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.doubleSpinBox_2.setFont(font)
        self.doubleSpinBox_2.setObjectName("doubleSpinBox_2")
        self.horizontalLayout.addWidget(self.doubleSpinBox_2)
        self.doubleSpinBox_3 = QtWidgets.QDoubleSpinBox(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.doubleSpinBox_3.setFont(font)
        self.doubleSpinBox_3.setObjectName("doubleSpinBox_3")
        self.horizontalLayout.addWidget(self.doubleSpinBox_3)
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.btn_send = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.btn_send.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/send.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_send.setIcon(icon1)
        self.btn_send.setObjectName("btn_send")
        self.horizontalLayout.addWidget(self.btn_send)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(40, 140, 411, 91))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")

        self.comboBox_ports = QtWidgets.QComboBox(self.groupBox_2)
        self.comboBox_ports.setGeometry(QtCore.QRect(20, 30, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.comboBox_ports.setFont(font)
        self.comboBox_ports.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.comboBox_ports.setObjectName("comboBox_ports")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons/port.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        # self.comboBox_ports.setItemIcon(icon2)
        self.comboBox_ports.addItem(icon2, "")
        ports = portlist.comports()
        port_names = [port.device for port in ports]
        self.comboBox_ports.addItems(port_names)

        self.btn_input = QtWidgets.QPushButton(self.groupBox_2)
        self.btn_input.setGeometry(QtCore.QRect(180, 30, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.btn_input.setFont(font)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("icons/input.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_input.setIcon(icon3)
        self.btn_input.setObjectName("btn_input")
        self.btn_input.clicked.connect(self.btn_input_cliked)

        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(890, 20, 641, 211))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setObjectName("groupBox_3")

        # layout for table
        self.verticalLayoutWidget = QtWidgets.QWidget(self.groupBox_3)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 30, 621, 171))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        self.table_model = QtGui.QStandardItemModel(0,2)
        self.table_model.setHorizontalHeaderLabels(['Устройство', 'Примечание'])

        self.tableView = QtWidgets.QTableView(self.verticalLayoutWidget)
        self.tableView.setObjectName("tableView")
        self.tableView.setModel(self.table_model)
        self.verticalLayout.addWidget(self.tableView)

        self.groupBox_4 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_4.setGeometry(QtCore.QRect(460, 139, 421, 91))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox_4.setFont(font)
        self.groupBox_4.setObjectName("groupBox_4")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEdit.setGeometry(QtCore.QRect(10, 31, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.btn_send_2 = QtWidgets.QPushButton(self.groupBox_4)
        self.btn_send_2.setGeometry(QtCore.QRect(280, 30, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.btn_send_2.setFont(font)
        self.btn_send_2.setIcon(icon1)
        self.btn_send_2.setObjectName("btn_send_2")
        self.btn_send_2.clicked.connect(self.btn_send_clicked)

        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(40, 260, 1491, 541))
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser.setFont(font)

        self.clearButton = QtWidgets.QPushButton("Очистить", self.centralwidget)
        self.clearButton.setGeometry(QtCore.QRect(1400, 270, 120, 40)) 
        self.clearButton.setFont(font)
        iconClear = QtGui.QIcon()
        iconClear.addPixmap(QtGui.QPixmap("icons/clear.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.clearButton.setIcon(iconClear)
        self.clearButton.clicked.connect(self.clearText)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1567, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.serial_port = None
        self.thread = None


        # timer for update com ports
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update_ports)
        self.timer.start(1000)
    def clearText(self):
        if hasattr(self,'serial_port') and self.serial_port and self.serial_port.is_open:
            self.textBrowser.clear()
            selected_port = f"<span style='color:green;'>{'=' * 30}<br>Получение данных от: {self.comboBox_ports.currentText()}<br>{'=' * 30}</span>"
            current_log = self.textBrowser.toHtml()
            new_text = current_log + "<br>" + selected_port
            self.textBrowser.setHtml(new_text)

            
        else:
            self.textBrowser.clear()
            self.textBrowser.append("<span style='color:red;'>Записи очищены</span>")
            
    def btn_send_clicked(self):
        if hasattr(self,'serial_port') and self.serial_port and self.serial_port.is_open:
            message = self.lineEdit.text()
            
            if message:
                try:    
                    self.serial_port.write(message.encode('utf-8'))
                    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                        # Ma'lumotni vaqt bilan birga logga qo'shish
                    formatted_data = f"<span style='color:green;'>[{current_time}] Отправлено сообщение:</span><span style='color:green;'> {message}</span>"
                    self.textBrowser.append(formatted_data)
                    self.lineEdit.clear()
                except Exception as e:
                    self.textBrowser.append(f"<span style='color:red;'>Ошибка: {str(e)}</span>")
            else:
                self.textBrowser.append("<span style='color:orange;'>Внимание: Требуется сообщение.</span>")
        else:
            self.textBrowser.append("<span style='color:red;'>Ошибка: последовательный порт не открыт.</span>")

    def update_ports(self):
        self.table_model.removeRows(0, self.table_model.rowCount())  # Jadvalni tozalash
        current_port = self.comboBox_ports.currentText()
        self.comboBox_ports.clear()  # COM portlar ro'yxatini tozalash
        ports = list(portlist.comports())  # Portlar ro'yxatini olish

        # ComboBox'ga yangi portlar ro'yxatini qo'shish
        port_names = [port.device for port in ports]
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons/port.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        # self.comboBox_ports.setItemIcon(icon2)
        # self.comboBox_ports.addItem(icon2, "")
        # self.comboBox_ports.addItems(icon2, port_names)  # Yangi portlarni ComboBox'ga qo'shish
        # Port nomlarini va ikonalarni qo'shish
        for port_name in port_names:
            self.comboBox_ports.addItem(icon2, port_name)

        # Jadvalga yangi portlarni qo'shish
        for port in ports:
            self.add_table_row(port.device, port.description)

        if current_port in port_names:
            self.comboBox_ports.setCurrentText(current_port)
        else:
            self.comboBox_ports.setCurrentIndex(0) 

    def add_table_row(self, name, comment):
        row_count = self.table_model.rowCount()
        self.table_model.insertRow(row_count)
        self.table_model.setData(self.table_model.index(row_count, 0), name)                # Ном
        self.table_model.setData(self.table_model.index(row_count, 1), comment)             # Изоҳ

    def btn_input_cliked(self):
        # Agar o'qish allaqachon davom etayotgan bo'lsa, uni to'xtatish
        if hasattr(self, 'reading') and self.reading:
            # Flagni to'xtatish va portni yopish
            self.reading = False
            if self.serial_port and self.serial_port.is_open:
                self.serial_port.close()
                self.textBrowser.append("<span style='color:red;'>Последовательный порт закрыт.</span>")

            
            self.btn_input.setText("Получение данных")
            return

        # Yangi sessiyani boshlash
        selected_port = f"<span style='color:green;'>{'=' * 30}<br>Получение данных от: {self.comboBox_ports.currentText()}<br>{'=' * 30}</span>"
        current_log = self.textBrowser.toHtml()
        new_text = current_log + "<br>" + selected_port
        self.textBrowser.setHtml(new_text)

        try:
            # Serial portni sozlash
            self.serial_port = serial.Serial(
                port=self.comboBox_ports.currentText(),
                baudrate=9600,
                timeout=1
            )

            if self.serial_port.is_open:
                # O'qishni boshqarish uchun flagni sozlash
                self.reading = True
                # Ma'lumotlarni o'qish uchun yangi mavzu yaratish
                self.thread = threading.Thread(target=self.read_from_serial)
                self.thread.daemon = True
                self.thread.start()

                self.btn_input.setText("Стоп")
            else:
                self.textBrowser.append("<span style='color:red;'>Ошибка: Не удалось открыть последовательный порт.</span>")

        except Exception as e:
            # Xato xabarini qizil rangda ko'rsatish
            self.textBrowser.append(f"<span style='color:red;'>Ошибка: {str(e)}</span>")

    def read_from_serial(self):
        """
        Serial portdan ma'lumotlarni o'qiydigan funksiya.
        """
        while self.reading:
            try:
                if self.serial_port and self.serial_port.is_open:
                    # Serial portdan ma'lumotni o'qish
                    data = self.serial_port.readline().decode('utf-8').strip()
                    if data:
                        # Hozirgi vaqtni formatlash
                        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                        # Ma'lumotni vaqt bilan birga logga qo'shish
                        formatted_data = f"<span style='color:#252525;'>[{current_time}] Полученная информация:</span><span style='color:green;'> {data}</span>"
                        self.textBrowser.append(formatted_data)
                else:
                    break
            except Exception as e:
                self.textBrowser.append(f"<span style='color:red;'>Ошибка: {str(e)}</span>")
                break


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "COM PORT UI"))
        self.groupBox.setTitle(_translate("MainWindow", "Для отправки"))
        self.comboBox_selectMotor.setCurrentText(_translate("MainWindow", "Мoтор 1"))
        self.comboBox_selectMotor.setItemText(0, _translate("MainWindow", "Мoтор 1"))
        self.comboBox_selectMotor.setItemText(1, _translate("MainWindow", "Мoтор 2"))
        self.comboBox_selectMotor.setItemText(2, _translate("MainWindow", "Мoтор 3"))
        self.comboBox_selectMotor.setItemText(3, _translate("MainWindow", "Мoтор 4"))
        self.comboBox_selectMotor.setItemText(4, _translate("MainWindow", "Мoтор 5"))
        self.comboBox_selectMotor.setItemText(5, _translate("MainWindow", "Мoтор 6"))
        self.comboBox_selectMotor.setItemText(6, _translate("MainWindow", "Мoтор 7"))
        self.comboBox_selectMotor.setItemText(7, _translate("MainWindow", "Мoтор 8"))
        self.checkBox.setText(_translate("MainWindow", "Обратный"))
        self.btn_send.setText(_translate("MainWindow", "Отправлять"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Чтобы получить"))
        self.btn_input.setText(_translate("MainWindow", "Получение данных"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Таблица ПОРТОВ"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Отправить"))
        self.btn_send_2.setText(_translate("MainWindow", "Отправлять"))


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())