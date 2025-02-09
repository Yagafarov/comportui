import sys
import pyqtgraph as pg
import pyqtgraph.opengl as gl
import numpy as np
import math
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QSlider, QLabel
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QMatrix4x4

class RobotArm(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        main_layout = QHBoxLayout()
        control_layout = QVBoxLayout()
        
        self.view = gl.GLViewWidget()
        main_layout.addWidget(self.view, 1)
        
        # Bo‘g‘in 1 slider
        self.angle1_label = QLabel("Angle 1: 0°")
        control_layout.addWidget(self.angle1_label)
        self.angle1_slider = QSlider(Qt.Vertical)
        self.angle1_slider.setMinimum(-45)
        self.angle1_slider.setMaximum(30)
        self.angle1_slider.valueChanged.connect(self.updateAngles)
        control_layout.addWidget(self.angle1_slider)
        
        # Bo‘g‘in 2 slider
        self.angle2_label = QLabel("Angle 2: 0°")
        control_layout.addWidget(self.angle2_label)
        self.angle2_slider = QSlider(Qt.Vertical)
        self.angle2_slider.setMinimum(-60)
        self.angle2_slider.setMaximum(70)
        self.angle2_slider.valueChanged.connect(self.updateAngles)
        control_layout.addWidget(self.angle2_slider)

        # Bo‘g‘in 3 slider
        self.angle3_label = QLabel("Angle 3: 0°")
        control_layout.addWidget(self.angle3_label)
        self.angle3_slider = QSlider(Qt.Vertical)
        self.angle3_slider.setMinimum(-90)
        self.angle3_slider.setMaximum(90)
        self.angle3_slider.valueChanged.connect(self.updateAngles)
        control_layout.addWidget(self.angle3_slider)
        
        main_layout.addLayout(control_layout)
        self.setLayout(main_layout)
        self.init3D()
    
    def init3D(self):
        self.view.setWindowTitle("3-Joint Robot Arm Control")
        
        grid = gl.GLGridItem()
        grid.scale(1, 1, 1)
        self.view.addItem(grid)
        
        self.l1 = 2.0
        self.l2 = 2.0
        self.l3 = 1.5  # 3-bo‘g‘in uzunligi
        
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
        angle1 = self.angle1_slider.value()
        angle2 = self.angle2_slider.value()
        angle3 = self.angle3_slider.value()
        
        self.angle1_label.setText(f"Angle 1: {angle1}°")
        self.angle2_label.setText(f"Angle 2: {angle2}°")
        self.angle3_label.setText(f"Angle 3: {angle3}°")
        
        # 1-bo‘g‘in transformatsiyasi
        transform1 = QMatrix4x4()
        transform1.rotate(angle1, 0, 0, 1)
        self.cylinder1.setTransform(transform1)
        
        motor1_transform = QMatrix4x4(transform1)
        motor1_transform.translate(0, 0, self.l1)
        self.motor1.setTransform(motor1_transform)
        
        # 2-bo‘g‘in transformatsiyasi
        transform2 = QMatrix4x4(motor1_transform)
        transform2.rotate(angle2, 1, 0, 0)
        self.cylinder2.setTransform(transform2)
        
        motor2_transform = QMatrix4x4(transform2)
        motor2_transform.translate(0, 0, self.l2)
        self.motor2.setTransform(motor2_transform)
        
        # 3-bo‘g‘in transformatsiyasi
        transform3 = QMatrix4x4(motor2_transform)
        transform3.rotate(angle3, 1, 0, 0)
        self.cylinder3.setTransform(transform3)
        
        motor3_transform = QMatrix4x4(transform3)
        motor3_transform.translate(0, 0, self.l3)
        self.motor3.setTransform(motor3_transform)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = RobotArm()
    window.show()
    sys.exit(app.exec_())
