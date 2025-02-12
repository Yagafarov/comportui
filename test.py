from PyQt5 import QtCore, QtGui, QtWidgets
import pyqtgraph.opengl as gl
import sys
import serial.tools.list_ports as portlist
import serial
import threading
from datetime import datetime
from PyQt5.QtWebEngineWidgets import QWebEngineView
import os

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.resize(1567, 863)
        MainWindow.setMinimumSize(QtCore.QSize(1000, 700))
        # Asosiy layout va markaziy widget
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.main_layout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.main_layout.setContentsMargins(20, 20, 20, 20)
        self.main_layout.setSpacing(15)
        self.angle1 = 45
        self.angle2 = -45
        self.angle3 = 90  # Default qiymatlarni belgilash

        # Yuqori qism (gorizontal layout)
        top_layout = QtWidgets.QHBoxLayout()
        top_layout.setSpacing(20)

        # Chap ustun (vertical layout)
        left_column = QtWidgets.QVBoxLayout()
        left_column.setSpacing(15)

        # GroupBox 1: Для отправки
        self.groupBox = QtWidgets.QGroupBox()
        self._create_group1()
        left_column.addWidget(self.groupBox)

        # Pastki chap qism (2ta groupbox)
        bottom_left = QtWidgets.QHBoxLayout()
        bottom_left.setSpacing(20)

        # GroupBox 2: Для получить
        self.groupBox_2 = QtWidgets.QGroupBox()
        self._create_group2()
        bottom_left.addWidget(self.groupBox_2, 2)

        # GroupBox 4: Отправить
        self.groupBox_4 = QtWidgets.QGroupBox()
        self._create_group4()
        bottom_left.addWidget(self.groupBox_4, 2)

        left_column.addLayout(bottom_left)

        # Ong ustun (vertical layout)
        right_column = QtWidgets.QVBoxLayout()

        # GroupBox 3: Таблица ПОРТОВ
        self.groupBox_3 = QtWidgets.QGroupBox()
        self._create_group3()
        right_column.addWidget(self.groupBox_3)

        top_layout.addLayout(left_column, 3)  # 60% ширины
        top_layout.addLayout(right_column, 2) # 40% ширины
        self.main_layout.addLayout(top_layout, 1)

        # TextBrowser va tugma
        split_widget = QtWidgets.QWidget()
        split_layout = QtWidgets.QHBoxLayout(split_widget)
        split_layout.setContentsMargins(0, 0, 0, 0)
        split_layout.setSpacing(10)
        
        self.main_layout.addWidget(split_widget)

        #LINK - 3D visualizatsiya
        self.view = gl.GLViewWidget()
        self.view.setMinimumHeight(600)
        split_layout.addWidget(self.view,2)

        #ANCHOR - fazoda yerni ifodalash 
        grid = gl.GLGridItem()
        grid.scale(1, 1, 1)
        self.view.addItem(grid)

        #ANCHOR - bo'g'in uzunliklari
        self.l1 = 140/100
        self.l2 = 200/100
        self.l3 = 200/100

        # 1-bo‘g‘in
        self.cylinder1 = self.createCylinder(self.l1, (0, 0, 1, 1))
        self.motor1 = self.createSphere((1, 1, 0, 1))

        # 2-bo‘g‘in
        self.cylinder2 = self.createCylinder(self.l2, (0, 1, 0, 1))
        self.motor2 = self.createSphere((1, 0, 1, 1))

        # 3-bo‘g‘in
        self.cylinder3 = self.createCylinder(self.l3, (1, 0, 0, 1))
        self.motor3 = self.createSphere((0, 1, 1, 1))

        self.updateAngles()


        MainWindow.setCentralWidget(self.centralwidget)
        
        # Menubar va statusbar
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        # Dastur parametrlari
        self.serial_port = None
        self.thread = None
        self.reading = False

        # Portlarni yangilash timer
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update_ports)
        self.timer.start(1000)
    def createCylinder(self, length, color):
        cylinder = gl.GLMeshItem(meshdata=gl.MeshData.cylinder(rows=20, cols=20, radius=[0.1, 0.1], length=length),
                                 smooth=True, shader='shaded', color=color)
        self.view.addItem(cylinder)
        return cylinder

    def createSphere(self, color):
        sphere = gl.GLMeshItem(meshdata=gl.MeshData.sphere(rows=20, cols=20, radius=0.2),
                               smooth=True, shader='shaded', color=color)
        self.view.addItem(sphere)
        return sphere
    def updateAngles(self):
        # Burchaklarni aniqlash
        
        
        text = self.comboBox_selectMotor.currentText()
        try:
            motor_index = int(text.split(" ")[1])
        except (IndexError, ValueError):
            motor_index = 1  # Default motor index

        
        try:
            if motor_index == 1:
                self.angle1 = float(self.doubleSpinBox.value())
            elif motor_index == 2:
                self.angle2 = float(self.doubleSpinBox.value())
            elif motor_index == 3:
                self.angle3 = float(self.doubleSpinBox.value())
        except ValueError:
            # Agar qiymatni o'qishda xato bo'lsa, default qiymatlar ishlatiladi
            pass

        # 1-bo‘g‘in transformatsiyasi
        transform1 = QtGui.QMatrix4x4()
        transform1.rotate(self.angle1, 0, 0, 1)
        self.cylinder1.setTransform(transform1)

        motor1_transform = QtGui.QMatrix4x4(transform1)
        motor1_transform.translate(0, 0, self.l1)
        self.motor1.setTransform(motor1_transform)

        # 2-bo‘g‘in transformatsiyasi
        transform2 = QtGui.QMatrix4x4(motor1_transform)
        transform2.rotate(self.angle2, 1, 0, 0)
        self.cylinder2.setTransform(transform2)

        motor2_transform = QtGui.QMatrix4x4(transform2)
        motor2_transform.translate(0, 0, self.l2)
        self.motor2.setTransform(motor2_transform)

        # 3-bo‘g‘in transformatsiyasi
        transform3 = QtGui.QMatrix4x4(motor2_transform)
        transform3.rotate(self.angle3, 1, 0, 0)
        self.cylinder3.setTransform(transform3)

        motor3_transform = QtGui.QMatrix4x4(transform3)
        motor3_transform.translate(0, 0, self.l3)
        self.motor3.setTransform(motor3_transform)

    #LINK - API orqali ma'lumotlarni yuborish
    def _create_group1(self):
        self.groupBox.setTitle("Для отправки")
        self.groupBox.setFont(QtGui.QFont("Segoe UI", 12))
        layout = QtWidgets.QHBoxLayout()
        layout.setContentsMargins(10, 15, 10, 15)

        # Motor selector
        self.comboBox_selectMotor = QtWidgets.QComboBox()
        self.comboBox_selectMotor.setFont(QtGui.QFont("Segoe UI", 12))
        icon = QtGui.QIcon("icons/motor.png")
        for i in range(1,5):
            self.comboBox_selectMotor.addItem(icon, f"Мoтор {i}")
        
        # Qolagi elementlar
        self.checkBox = QtWidgets.QCheckBox("Обратный")
        self.checkBox.setFont(QtGui.QFont("Segoe UI", 12))
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox()
        self.doubleSpinBox.setFont(QtGui.QFont("Segoe UI", 12))
        self.doubleSpinBox.setRange(0, 999)
        self.doubleSpinBox_2 = QtWidgets.QDoubleSpinBox()
        self.doubleSpinBox_2.setFont(QtGui.QFont("Segoe UI", 12))
        self.doubleSpinBox_2.setRange(0, 999)
        self.btn_send = QtWidgets.QPushButton("Отправлять")
        self.btn_send.setIcon(QtGui.QIcon("icons/send.png"))
        self.btn_send.setFont(QtGui.QFont("Segoe UI", 12))
        self.btn_send.setStyleSheet("""
            QPushButton {
                background-color: #2196F3;
                color: white;
                border-radius: 6px;
                padding: 6px 12px;
            }
            QPushButton:hover {
                background-color: #1976D2;
            }
        """)

        # Size policies
        for widget in [self.comboBox_selectMotor, self.doubleSpinBox, self.doubleSpinBox_2]:
            widget.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)

        # Layout tartibi
        layout.addWidget(self.comboBox_selectMotor)
        layout.addSpacing(15)
        layout.addWidget(self.checkBox)
        layout.addWidget(self.doubleSpinBox)
        layout.addWidget(self.doubleSpinBox_2)
        layout.addSpacing(15)
        layout.addWidget(self.btn_send)
        self.groupBox.setLayout(layout)

    #LINK - Qabul qilish va PORTni ochish
    def _create_group2(self):
        self.groupBox_2.setTitle("Для получить")
        self.groupBox_2.setFont(QtGui.QFont("Segoe UI", 12))
        layout = QtWidgets.QVBoxLayout()
        layout.setContentsMargins(10, 15, 10, 15)

        port_layout = QtWidgets.QHBoxLayout()
        self.comboBox_ports = QtWidgets.QComboBox()
        self.comboBox_ports.setFont(QtGui.QFont("Segoe UI", 12))
        
        self.btn_input = QtWidgets.QPushButton("Получение данных")
        self.btn_input.setIcon(QtGui.QIcon("icons/input.png"))
        self.btn_input.setFont(QtGui.QFont("Segoe UI", 12))

        port_layout.addWidget(self.comboBox_ports)
        port_layout.addWidget(self.btn_input)
        layout.addLayout(port_layout)
        self.groupBox_2.setLayout(layout)

    #LINK - LOGlar va PORT jadvallarini ko'rish uchun
    def _create_group3(self):
        self.groupBox_3.setTitle("Информация")
        self.groupBox_3.setFont(QtGui.QFont("Segoe UI", 12))
        layout = QtWidgets.QVBoxLayout()
        layout.setContentsMargins(10, 15, 10, 15)

        # Создаем горизонтальный контейнер для кнопок
        button_layout = QtWidgets.QHBoxLayout()

        # Кнопка "Очистить"
        self.clearButton = QtWidgets.QPushButton("Очистить")
        self.clearButton.setIcon(QtGui.QIcon("icons/clear.png"))
        self.clearButton.setFont(QtGui.QFont("Segoe UI", 12))
        button_layout.addWidget(self.clearButton)

        # Кнопка "Таблица ПОРТОВ"
        self.modal_button = QtWidgets.QPushButton("Таблица ПОРТОВ")
        self.modal_button.setIcon(QtGui.QIcon("icons/table.png"))
        self.modal_button.setFont(QtGui.QFont("Segoe UI", 12))
        button_layout.addWidget(self.modal_button)

        # Добавляем горизонтальный контейнер с кнопками в основной layout
        layout.addLayout(button_layout)

        # Таблица и текстовое поле (остаются вертикально)
        self.table_model = QtGui.QStandardItemModel(0, 2)
        self.table_model.setHorizontalHeaderLabels(['Устройство', 'Примечание'])
        
        self.tableView = QtWidgets.QTableView()
        self.tableView.setModel(self.table_model)
        self.tableView.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.tableView.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.tableView.setFont(QtGui.QFont("Segoe UI", 12))

        # Текстовый блок
        self.textBrowser1 = QtWidgets.QTextBrowser()
        self.textBrowser1.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.textBrowser1.setFont(QtGui.QFont("Segoe UI", 12))
        self.textBrowser1.clear()
        layout.addWidget(self.textBrowser1, stretch=2)

        self.groupBox_3.setLayout(layout)
    
    #LINK - Oddiy matn yuborish uchun
    def _create_group4(self):
        self.groupBox_4.setTitle("Отправить")
        self.groupBox_4.setFont(QtGui.QFont("Segoe UI", 12))
        layout = QtWidgets.QHBoxLayout()
        layout.setContentsMargins(10, 15, 10, 15)

        self.lineEdit = QtWidgets.QLineEdit()
        self.lineEdit.setFont(QtGui.QFont("Segoe UI", 12))
        
        self.btn_send_2 = QtWidgets.QPushButton("Отправлять")
        self.btn_send_2.setIcon(QtGui.QIcon("icons/send.png"))
        self.btn_send_2.setFont(QtGui.QFont("Segoe UI", 12))
        self.btn_send_2.setStyleSheet("""
            QPushButton {
                background-color: #2196F3;
                color: white;
                border-radius: 6px;
                padding: 6px 12px;
            }
            QPushButton:hover {
                background-color: #1976D2;
            }
        """)

        layout.addWidget(self.lineEdit, 3)
        layout.addWidget(self.btn_send_2, 1)
        self.groupBox_4.setLayout(layout)

    #LINK -  LOGlarni tozalash funksiyasi
    def clearText(self):
        if hasattr(self,'serial_port') and self.serial_port and self.serial_port.is_open:
            self.textBrowser1.clear()
            selected_port = f"<span style='color:green;'>{'='*30}<br>Получение данных от: {self.comboBox_ports.currentText()}<br>{'='*30}</span>"
            current_log = self.textBrowser1.toHtml()
            new_text = current_log + "<br>" + selected_port
            self.textBrowser1.setHtml(new_text)
        else:
            self.textBrowser1.clear()
            self.textBrowser1.append("<span style='color:red;'>Записи очищены</span>")

    #LINK - API orqali ma'lumot yuborish funksiyasi
    def btn_send_motor(self):
        if hasattr(self, 'serial_port') and self.serial_port and self.serial_port.is_open:
            motor = self.comboBox_selectMotor.currentText().split(" ")[1]
            
            isInverse = "8" if self.checkBox.isChecked() else "0"
            
            hex_degree = str(hex(int(float(self.doubleSpinBox.text().replace(',', '')))))
            print(hex_degree)
            if len(hex_degree)==6:
                degree1=hex_degree[2:4]
                degree2=hex_degree[4:6]
            else:
                degree1="0"+hex_degree[2]
                degree2=hex_degree[3:5]                

            hex_speed = str(hex(int(float(self.doubleSpinBox_2.text().replace(',','')))))
            if len(hex_speed)==6:    
                speed1 = hex_speed[2:4]
                speed2 = hex_speed[4:6]
            else:
                speed1 = "0"+hex_speed[2]
                speed2 = hex_speed[3:5]

            self.updateAngles()
            message = "11 " + isInverse + motor + " " + degree1+ " " + degree2 + " " + speed1 + " " + speed2
            hex_message = bytes.fromhex(message.replace(" ", ""))
            self.serial_port.write(hex_message)
            self.textBrowser1.append(message)
        else:
            self.textBrowser1.append("<span style='color:red;'>Ошибка: последовательный порт не открыт.</span>")

    #LINK - Oddiy matn yuborish uchun funksiya
    def btn_send_clicked(self):
        if hasattr(self,'serial_port') and self.serial_port and self.serial_port.is_open:
            message = self.lineEdit.text()
            
            if message:
                try:
                    hex_message = bytes.fromhex(message.replace(" ", ""))    
                    self.serial_port.write(hex_message)
                    self.serial_port.writable(hex(19))
                    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                        # Ma'lumotni vaqt bilan birga logga qo'shish
                    formatted_data = f"<span style='color:green;'>[{current_time}] Отправлено сообщение:</span><span style='color:green;'> {message}</span>"
                    self.textBrowser1.append(formatted_data)
                    self.lineEdit.clear()
                except Exception as e:
                    self.textBrowser1.append(f"<span style='color:red;'>Ошибка: {str(e)}</span>")
            else:
                self.textBrowser1.append("<span style='color:orange;'>Внимание: Требуется сообщение.</span>")
        else:
            self.textBrowser1.append("<span style='color:red;'>Ошибка: последовательный порт не открыт.</span>")

    #LINK - PORT listni yangilash uchun funksiya
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

    #LINK - PORT jadvalini yangilash uchun funksiya
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
                self.textBrowser1.append("<span style='color:red;'>Последовательный порт закрыт.</span>")

            
            self.btn_input.setText("Получение данных")
            return

        # Yangi sessiyani boshlash
        selected_port = f"<span style='color:green;'>{'=' * 30}<br>Получение данных от: {self.comboBox_ports.currentText()}<br>{'=' * 30}</span>"
        current_log = self.textBrowser1.toHtml()
        new_text = current_log + "<br>" + selected_port
        self.textBrowser1.setHtml(new_text)

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
                self.textBrowser1.append("<span style='color:red;'>Ошибка: Не удалось открыть последовательный порт.</span>")

        except Exception as e:
            # Xato xabarini qizil rangda ko'rsatish
            self.textBrowser1.append(f"<span style='color:red;'>Ошибка: {str(e)}</span>")

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
        

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowIcon(QtGui.QIcon("icons/portMain.png"))  # Ikonka fayli
        
        # Oynani ekran markaziga joylashtirish
        # Signal-slot ulanishlari
        self.btn_send.clicked.connect(self.btn_send_motor)
        self.btn_send_2.clicked.connect(self.btn_send_clicked)
        self.btn_input.clicked.connect(self.btn_input_cliked)
        self.clearButton.clicked.connect(self.clearText)
        self.modal_button.clicked.connect(self.show_modal_table)
    def show_modal_table(self):
        """Show ports table in a modal dialog"""
        dialog = QtWidgets.QDialog(self)
        dialog.setWindowTitle("Таблица портов")
        dialog.setModal(True)
        dialog.resize(600, 400)

        # Create table view
        layout = QtWidgets.QVBoxLayout(dialog)
        table_view = QtWidgets.QTableView()
        table_view.setModel(self.table_model)  # Share the same model
        table_view.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        
        layout.addWidget(table_view)
        dialog.setLayout(layout)
        dialog.exec_()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())