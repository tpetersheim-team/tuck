#!/usr/bin/env python

from PyQt5.QtWidgets import (QApplication, QBoxLayout, QGridLayout, QHBoxLayout, QLabel, QMessageBox, QPushButton, QWidget)


app = QApplication([])
window = QWidget()

topLayout = QHBoxLayout()
mainLayout = QGridLayout()
mainLayout.addLayout(topLayout, 0, 0, 1, 2)

label = QLabel("Hello Tuck!")
topLayout.addWidget(label)
label.show()

button = QPushButton("Show me the tuck")
topLayout.addWidget(button)
def on_button_clicked():
        alert = QMessageBox()
        alert.setText("Dumb tucker!")
        alert.exec_()

button.clicked.connect(on_button_clicked)
button.setDefault(True)

window.setLayout(mainLayout)
window.show()

app.exec_()
