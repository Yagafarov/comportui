from PyQt5 import QtCore, QtGui, QtWidgets
import pyqtgraph.opengl as gl
from newsFunction import actionSendWithApi,actionSendDefault,actionGoGome
import re

class Ui_MainWindow(object):
        
    def setupUi(self, MainWindow):
        # ANCHOR - Main Window Setup
        MainWindow.setWindowTitle("AGRORob")
        MainWindow.setMinimumSize(QtCore.QSize(1024, 800))
        MainWindow.setStyleSheet("background-color: #f0f0f0;")
        esp_ip = "192.168.187.183"
        self.centralwidget = QtWidgets.QWidget(MainWindow)

        # ANCHOR - Main Layout
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)

        # SECTION - Splitter for Equal Widths
        self.splitter = QtWidgets.QSplitter(QtCore.Qt.Horizontal)

        # SECTION - Control Section
        self.groupControl = QtWidgets.QGroupBox("Control", self.splitter)
        self.groupControl.setAlignment(QtCore.Qt.AlignCenter)
        self.verticalLayoutControl = QtWidgets.QVBoxLayout(self.groupControl)

        # API Send Group
        self.groupBoxAPISend = QtWidgets.QGroupBox("Send with API", self.groupControl)
        self.verticalLayoutAPISend = QtWidgets.QVBoxLayout(self.groupBoxAPISend)

        self.comboBox = QtWidgets.QComboBox(self.groupBoxAPISend)
        self.comboBox.addItems(["Motor 1", "Motor 2", "Motor 3", "Motor 4"])
        self.comboBox.setStyleSheet("""
            QComboBox {
                background-color: #f0f0f0; /* Background color */
                border: 1px solid #888; /* Border color */
                border-radius: 5px; /* Rounded corners */
                padding: 5px; /* Padding */
                margin-bottom:10px;
                font-size:16px;
            }
            QComboBox::drop-down {
                border: none; /* No border for dropdown */
            }
            QComboBox::item {
                background-color: #ffffff;
            }
            QComboBox::item:selected {
                background-color: #0078d7; /* Selected item color */
                color: white; /* Selected item text color */
            }
        """)
        self.verticalLayoutAPISend.addWidget(self.comboBox)

        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(self.groupBoxAPISend)
        self.doubleSpinBox.setStyleSheet("""
            QDoubleSpinBox {
                background-color: #f0f0f0; /* Background color */
                border: 2px solid #0078d7; /* Border color */
                border-radius: 5px; /* Rounded corners */
                padding: 5px; /* Padding */
                font-size: 16px; /* Font size */ 
            }
        """)
        self.verticalLayoutAPISend.addWidget(self.doubleSpinBox)

        self.horizontalSlider = QtWidgets.QSlider(self.groupBoxAPISend)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setStyleSheet("""
    QSlider:horizontal {
        background: #f7f7f7; /* Yengil fon rangi */
        height: 30px; /* Slayder balandligi */
        border-radius: 15px; /* Burchaklarni yumshatish */
        margin-bottom:10px;
    }
    QSlider::groove:horizontal {
        background: #d0d0d0; /* Groove rangi */
        height: 10px; /* Groove balandligi */
        border-radius: 5px; /* Groove burchaklarini yumshatish */
    }
    QSlider::handle:horizontal {
        background: #4a90e2; /* Qo'lga olish rangi */
        width: 25px; /* Qo'lga olish kengligi */
        margin: -7px 0; /* Qo'lga olishni markazga joylash */
        border-radius: 12px; /* Yumshoq qo'lga olish */
        border: 2px solid #ffffff; /* Oq chegara */
    }
    QSlider::handle:horizontal:hover {
        background: #357ab8; /* Qo'lga olish hover rangi */
        border: 2px solid #ffffff; /* Hoverda oq chegara */
    }
""")

        self.verticalLayoutAPISend.addWidget(self.horizontalSlider)

        self.doubleSpinBoxSpeed = QtWidgets.QDoubleSpinBox(self.groupBoxAPISend)
        self.doubleSpinBoxSpeed.setStyleSheet("""
            QDoubleSpinBox {
                background-color: #f0f0f0; /* Background color */
                border: 2px solid #0078d7; /* Border color */
                border-radius: 5px; /* Rounded corners */
                padding: 5px; /* Padding */
                font-size: 16px; /* Font size */
            }
        """)
        self.verticalLayoutAPISend.addWidget(self.doubleSpinBoxSpeed)
        self.horizontalSliderSpeed = QtWidgets.QSlider(self.groupBoxAPISend)
        self.horizontalSliderSpeed.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSliderSpeed.setStyleSheet("""
    QSlider:horizontal {
        background: #f7f7f7; /* Yengil fon rangi */
        height: 30px; /* Slayder balandligi */
        border-radius: 15px; /* Burchaklarni yumshatish */
        margin-bottom:10px;
    }
    QSlider::groove:horizontal {
        background: #d0d0d0; /* Groove rangi */
        height: 10px; /* Groove balandligi */
        border-radius: 5px; /* Groove burchaklarini yumshatish */
    }
    QSlider::handle:horizontal {
        background: #4a90e2; /* Qo'lga olish rangi */
        width: 25px; /* Qo'lga olish kengligi */
        margin: -7px 0; /* Qo'lga olishni markazga joylash */
        border-radius: 12px; /* Yumshoq qo'lga olish */
        border: 2px solid #ffffff; /* Oq chegara */
    }
    QSlider::handle:horizontal:hover {
        background: #357ab8; /* Qo'lga olish hover rangi */
        border: 2px solid #ffffff; /* Hoverda oq chegara */
    }
""")

        self.verticalLayoutAPISend.addWidget(self.horizontalSliderSpeed)

        self.checkBox = QtWidgets.QCheckBox("HEX", self.groupBoxAPISend)
                
        self.checkBox.setChecked(True)
        self.checkBox.setStyleSheet("""
            QCheckBox {
                spacing: 5px; /* Checkbox va matn orasidagi masofa */
                font-size: 14px; /* Shrift o'lchami */
                color: #333; /* Matn rangi */
            }
            QCheckBox::indicator {
                width: 20px; /* Indikator kengligi */
                height: 20px; /* Indikator balandligi */
                border: 2px solid #0078d7; /* Indikator chegarasi */
                border-radius: 4px; /* Indikator burchaklarini yumshatish */
                background: #f0f0f0; /* Indikatorning fon rangi */
            }
            QCheckBox::indicator:checked {
                background: #0078d7; /* Belgilangan indikator rangi */
                border: 2px solid #0056a1; /* Belgilangan indikator chegarasi */
            }
            QCheckBox::indicator:unchecked {
                background: #f0f0f0; /* Belgilanmagan indikator rangi */
            }
            QCheckBox::indicator:checked:hover {
                background: #0056a1; /* Belgilangan indikator hover rangi */
            }
        """)
        self.verticalLayoutAPISend.addWidget(self.checkBox)


        self.pushButton = QtWidgets.QPushButton("Send", self.groupBoxAPISend)
        self.pushButton.clicked.connect(lambda: actionSendWithApi(esp_ip))
        self.pushButton.setStyleSheet("""
            QPushButton {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:1, 
                                            stop:0 #0078d7, stop:1 #0056a1); /* Gradient fon */
                color: white; /* Matn rangi */
                border: none; /* Chegara yo'q */
                border-radius: 5px; /* Burchaklarni yumshatish */
                padding: 10px 20px; /* Tugma ichidagi bo'sh joy */
                font-size: 16px; /* Shrift o'lchami */
            }
            QPushButton:hover {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:1, 
                                            stop:0 #0056a1, stop:1 #003f6b); /* Hover holatidagi gradient */
            }
            QPushButton:pressed {
                background-color: #004080; /* Tugma bosilganda fon rangi */
            }
        """)


        self.verticalLayoutAPISend.addWidget(self.pushButton)

        self.verticalLayoutControl.addWidget(self.groupBoxAPISend)

        # Default Text Group
        self.groupBox_5 = QtWidgets.QGroupBox("Send Default Text", self.groupControl)
        self.verticalLayoutDefaultText = QtWidgets.QVBoxLayout(self.groupBox_5)

        self.lineEdit = QtWidgets.QLineEdit(self.groupBox_5)
        self.lineEdit.setStyleSheet("""
    QLineEdit {
        background-color: #f9f9f9; /* Fon rangi */
        color: #333; /* Matn rangi */
        border: 2px solid #0078d7; /* Chegara rangi */
        border-radius: 5px; /* Burchaklarni yumshatish */
        padding: 10px; /* Ichki bo'sh joy */
        font-size: 16px; /* Shrift o'lchami */
    }
    QLineEdit:focus {
        border: 2px solid #0056a1; /* Fokustagi chegaraning rangi */
        background-color: #ffffff; /* Fokustagi fon rangi */
    }
""")
        self.lineEdit.setPlaceholderText("Default Text")
        self.verticalLayoutDefaultText.addWidget(self.lineEdit)

        self.checkBox_2 = QtWidgets.QCheckBox("HEX", self.groupBox_5)
        self.checkBox_2.setChecked(True)
        self.checkBox_2.setStyleSheet("""
            QCheckBox {
                spacing: 5px; /* Checkbox va matn orasidagi masofa */
                font-size: 14px; /* Shrift o'lchami */
                color: #333; /* Matn rangi */
            }
            QCheckBox::indicator {
                width: 20px; /* Indikator kengligi */
                height: 20px; /* Indikator balandligi */
                border: 2px solid #0078d7; /* Indikator chegarasi */
                border-radius: 4px; /* Indikator burchaklarini yumshatish */
                background: #f0f0f0; /* Indikatorning fon rangi */
            }
            QCheckBox::indicator:checked {
                background: #0078d7; /* Belgilangan indikator rangi */
                border: 2px solid #0056a1; /* Belgilangan indikator chegarasi */
            }
            QCheckBox::indicator:unchecked {
                background: #f0f0f0; /* Belgilanmagan indikator rangi */
            }
            QCheckBox::indicator:checked:hover {
                background: #0056a1; /* Belgilangan indikator hover rangi */
            }
        """)
        self.verticalLayoutDefaultText.addWidget(self.checkBox_2)

        self.pushButton_2 = QtWidgets.QPushButton("Send", self.groupBox_5)
        self.pushButton_2.clicked.connect(lambda: actionSendDefault(esp_ip))
        self.pushButton_2.setStyleSheet("""
            QPushButton {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:1, 
                                            stop:0 #0078d7, stop:1 #0056a1); /* Gradient fon */
                color: white; /* Matn rangi */
                border: none; /* Chegara yo'q */
                border-radius: 5px; /* Burchaklarni yumshatish */
                padding: 10px 20px; /* Tugma ichidagi bo'sh joy */
                font-size: 16px; /* Shrift o'lchami */
            }
            QPushButton:hover {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:1, 
                                            stop:0 #0056a1, stop:1 #003f6b); /* Hover holatidagi gradient */
            }
            QPushButton:pressed {
                background-color: #004080; /* Tugma bosilganda fon rangi */
            }
        """)
        self.verticalLayoutDefaultText.addWidget(self.pushButton_2)

        self.verticalLayoutControl.addWidget(self.groupBox_5)

        # Additional Group Box
        self.groupBox_3 = QtWidgets.QGroupBox("Log", self.groupControl)
        self.verticalLayoutLog = QtWidgets.QVBoxLayout(self.groupBox_3)

        self.textBrowser = QtWidgets.QTextBrowser(self.groupBox_3)
        self.textBrowser.setStyleSheet("""
            QTextBrowser {
                background-color: #f9f9f9; /* Fon rangi */
                color: #333; /* Matn rangi */
                border: 2px solid #0078d7; /* Chegara rangi */
                border-radius: 5px; /* Burchaklarni yumshatish */
                padding: 10px; /* Ichki bo'sh joy */
                font-size: 14px; /* Shrift o'lchami */
                selection-background-color: #0078d7; /* Tanlangan matn fon rangi */
                selection-color: white; /* Tanlangan matn rangi */
            }
            QTextBrowser:focus {
                border: 2px solid #0056a1; /* Fokustagi chegaraning rangi */
            }
        """)
        self.verticalLayoutLog.addWidget(self.textBrowser)


        self.pushButton_3 = QtWidgets.QPushButton("Open Port", self.groupBox_3)
        self.pushButton_3.setStyleSheet("""
            QPushButton {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:1, 
                                            stop:0 #0078d7, stop:1 #0056a1); /* Gradient fon */
                color: white; /* Matn rangi */
                border: none; /* Chegara yo'q */
                border-radius: 5px; /* Burchaklarni yumshatish */
                padding: 10px 20px; /* Tugma ichidagi bo'sh joy */
                font-size: 16px; /* Shrift o'lchami */
            }
            QPushButton:hover {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:1, 
                                            stop:0 #0056a1, stop:1 #003f6b); /* Hover holatidagi gradient */
            }
            QPushButton:pressed {
                background-color: #004080; /* Tugma bosilganda fon rangi */
            }
        """)
        self.verticalLayoutLog.addWidget(self.pushButton_3)

        self.pushButton_4 = QtWidgets.QPushButton("Clear", self.groupBox_3)
        self.pushButton_4.setStyleSheet("""
            QPushButton {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:1, 
                                            stop:0 #0078d7, stop:1 #0056a1); /* Gradient fon */
                color: white; /* Matn rangi */
                border: none; /* Chegara yo'q */
                border-radius: 5px; /* Burchaklarni yumshatish */
                padding: 10px 20px; /* Tugma ichidagi bo'sh joy */
                font-size: 16px; /* Shrift o'lchami */
            }
            QPushButton:hover {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:1, 
                                            stop:0 #0056a1, stop:1 #003f6b); /* Hover holatidagi gradient */
            }
            QPushButton:pressed {
                background-color: #004080; /* Tugma bosilganda fon rangi */
            }
        """)
        self.verticalLayoutLog.addWidget(self.pushButton_4)

        self.verticalLayoutControl.addWidget(self.groupBox_3)

        # SECTION - Visualization Group
        self.groupBox_2 = QtWidgets.QGroupBox("Visualization", self.splitter)
        self.groupBox_2.setAlignment(QtCore.Qt.AlignCenter)

        # Set up GLViewWidget for 3D visualization
        self.view = gl.GLViewWidget()
        self.view.setMinimumWidth(600)
        self.view.setMinimumHeight(600)  # Set minimum height for the view
        self.view.setBackgroundColor('#252525')  # Set background color to white

        # Add grid to the GLViewWidget
        grid = gl.GLGridItem()
        grid.scale(1, 1, 1)
        self.view.addItem(grid)

        # Create a vertical layout for the visualization group box
        self.verticalLayoutVisualization = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayoutVisualization.addWidget(self.view)

        # Add the splitter to the main layout
        self.horizontalLayout.addWidget(self.splitter)

        MainWindow.setCentralWidget(self.centralwidget)

        # MENU BAR
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        MainWindow.setMenuBar(self.menubar)
        self.menubar.setStyleSheet("""
            QMenuBar {
                margin: 20px 0;                
            }
            QMenuBar::item {
                padding: 10px;
                color: #333; /* Dark text color */
            }
            QMenuBar::item:selected {
                background-color: #3498db; /* Selected background */
                color: white;
            }
            QMenuBar::item:hover {
                background-color: #2980b9; /* Hover background */
                color: white;
            }
            QMenu {
                background-color: #ffffff; /* White background for menus */
                color: black;
            }
            QMenu::item {
                padding: 10px;
            }
            QMenu::item:selected {
                background-color: #3498db; /* Selected item background */
                color: white;
            }
            QMenu::item:hover {
                background-color: #2980b9; /* Hover item background */
                color: white;
            }
        """)

        self.menuAction = QtWidgets.QMenu("Action", self.menubar)
        self.menuPorts = QtWidgets.QMenu("Ports", self.menubar)
        self.menuHelp = QtWidgets.QMenu("Help", self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        MainWindow.setStatusBar(self.statusbar)

        # ACTIONS
        self.actionCreator = QtWidgets.QAction("Creator", MainWindow)
        self.actionInfo = QtWidgets.QAction("Info", MainWindow)
        self.actionGoHome = QtWidgets.QAction("Go Home", MainWindow)
        self.menuAction.addAction(self.actionGoHome)
        self.actionGoHome.triggered.connect(lambda: actionGoGome(esp_ip))

        self.menuHelp.addAction(self.actionCreator)
        self.menuHelp.addAction(self.actionInfo)
        self.menubar.addAction(self.menuAction.menuAction())
        self.menubar.addAction(self.menuPorts.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Menu Widget for IP display
        self.menuWidget = QtWidgets.QWidget(self.menubar)
        self.menuLayout = QtWidgets.QHBoxLayout(self.menuWidget)
        self.menuLayout.setContentsMargins(0, 0, 0, 0)  # Remove internal margins
        self.lineEditIP = QtWidgets.QLineEdit(self.menuWidget)
        self.lineEditIP.setPlaceholderText("Enter IP")  # Placeholder text for guidance
        self.lineEditIP.setText(f"{esp_ip}")
        self.lineEditIP.setStyleSheet("""
            font-size: 16px; 
            padding: 5px; 
            background-color: #e6f7ff; /* Light blue background */
            color: #333; /* Dark text color */
            border: 1px solid #a0c4ff; /* Light border */
            border-radius: 5px; /* Rounded corners */
            margin-right: 5px;
            margin-top:10px; 
            min-width: 200px; 
        """)
        self.lineEditIP.setSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        self.menuLayout.addWidget(self.lineEditIP)

        # Create the OK button
        self.okButton = QtWidgets.QPushButton("OK", self.menuWidget)
        self.okButton.setStyleSheet("""
            font-size: 16px; 
            background-color:qlineargradient(x1:0, y1:0, x2:1, y2:1, 
                                            stop:0 #0056a1, stop:1 #003f6b); /* Green background */
            padding: 5px; 
            color: white; /* White text color */
            border: none; /* No border */
            border-radius: 5px; /* Rounded corners */
            margin-top:10px;
            margin-right: 20px; /* Space from the line edit */
        """)
        self.okButton.setSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        self.menuLayout.addWidget(self.okButton)

        # Connect the button's clicked signal to the validation method
        self.okButton.clicked.connect(self.validate_ip_format)

        self.menuLayout.addStretch()  # Add stretchable space at the end
        self.menubar.setCornerWidget(self.menuWidget, QtCore.Qt.TopRightCorner)
    def validate_ip_format(self):
        ip_address = self.lineEditIP.text()
        ip_pattern = re.compile(r"^(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\."
                                r"(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\."
                                r"(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\."
                                r"(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$")

        if ip_pattern.match(ip_address):
            # Change text color to green if valid
            self.lineEditIP.setStyleSheet("""
                font-size: 16px; 
                padding: 5px; 
                background-color: #e6f7ff; /* Light blue background */
                color: qlineargradient(x1:0, y1:0, x2:1, y2:1, 
                                            stop:0 #0056a1, stop:1 #003f6b); /* Dark text color */
                border: 1px solid #a0c4ff; /* Light border */
                border-radius: 5px; /* Rounded corners */
                margin-right: 5px;
                margin-top:10px; 
                min-width: 200px; 
            """)
            print("Success")
            esp_ip = self.lineEditIP.text()
        else:
            # Change text color to red if invalid
            self.lineEditIP.setStyleSheet("""
                font-size: 16px; 
                padding: 5px; 
                background-color: #e6f7ff; /* Light blue background */
                color: red; /* Dark text color */
                border: 1px solid #a0c4ff; /* Light border */
                border-radius: 5px; /* Rounded corners */
                margin-right: 5px;
                margin-top:10px; 
                min-width: 200px; 
            """)
            print('Have a problem')

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
