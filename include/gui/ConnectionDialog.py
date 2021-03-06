"""---------------------------------------------------------------------------------------
--      SOURCE FILE:        ConnectionDialog.py - Simple dialog input box with host and ip
--
--      PROGRAM:            file_transport
--
--      DATE:               October 2, 2016
--
--      REVISION:           (Date and Description)
--
--      DESIGNERS:          Anthony Smith
--
--      PROGRAMMERS:        Anthony Smith
--
--      NOTES:
--      This file extends the PYQT dialog class to build a dialog box with two input
--      boxes and a connection button. One input box is to specify the host address, and
--      the other is to specify the port to connect to. Once the dialog is submitted, it
--      sets the values of both text boxes to be later retrieved
---------------------------------------------------------------------------------------"""
from PyQt4 import QtGui
from PyQt4.QtGui import *

class ConnectionDialog(QDialog):
    DIALOG_HEIGHT = 100
    DIALOG_WIDTH = 450

    def __init__(self, remoteHost, remotePort, parent=None):
        QtGui.QDialog.__init__(self,parent)
        self.remoteHost = remoteHost
        self.remotePort = remotePort
        self.setupUi()
        self.centerPosition()

    def centerPosition(self):
        frameGm = self.frameGeometry()
        screen = QtGui.QApplication.desktop().screenNumber(QtGui.QApplication.desktop().cursor().pos())
        centerPoint = QtGui.QApplication.desktop().screenGeometry(screen).center()
        frameGm.moveCenter(centerPoint)
        self.move(frameGm.topLeft())
        self.show()

    def setupUi(self):
        self.setWindowTitle("File Transfer App - Server Connection")
        self.setGeometry(100, 100, ConnectionDialog.DIALOG_WIDTH, ConnectionDialog.DIALOG_HEIGHT)

        hostLabel = QLabel(self)
        hostLabel.setText("Enter Host Address / Port")

        self.hostText = QLineEdit(self)
        self.hostText.setText(self.remoteHost)

        self.portText = QLineEdit(self)
        self.portText.setText(str(self.remotePort))

        connectBTN = QPushButton(self)
        connectBTN.setText("Connect")
        connectBTN.clicked.connect(self.acceptConnect)

        hbox = QtGui.QHBoxLayout()
        hbox.addWidget(self.hostText, 2)
        hbox.addWidget(self.portText, 1)

        hbox2 = QtGui.QHBoxLayout()
        hbox2.addStretch(1)
        hbox2.addStretch(1)
        hbox2.addWidget(connectBTN)

        vbox = QVBoxLayout()
        vbox.addWidget(hostLabel)
        vbox.addLayout(hbox)
        vbox.addLayout(hbox2)

        self.setLayout(vbox)

    def acceptConnect(self):
        self.remoteHost = self.hostText.text()
        self.remotePort = self.portText.text()
        self.accept()

