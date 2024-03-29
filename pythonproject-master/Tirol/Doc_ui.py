# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\pythonproject\Doc.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import psycopg2


class Ui_Doctors(object):
    
    def __init__(self):
        # Create a connection to the database
        self.connection = psycopg2.connect(
            host='localhost',
            port='5432',
            database='mydb',
            user='postgres',
            password='cheesecake'
        )
        self.cursor = self.connection.cursor()  
         
    def searchDoctor(self):
        id = self.lineEdit_5.text()
        self.cursor.execute("SELECT doc_fname, doc_lname, doc_type FROM DOCTOR WHERE doc_id = %s", (id,))
        doctor = self.cursor.fetchone()

        if doctor:
            # Doctor found, display the information
            firstname, lastname, specialization = doctor

            self.lineEdit_7.setText(firstname)
            self.lineEdit_6.setText(lastname)
            self.lineEdit_8.setText(specialization)
            
        else:
            # Doctor not found, show an error message
            error_msg = QMessageBox()
            error_msg.setIcon(QMessageBox.Critical)
            error_msg.setWindowTitle("Error")
            error_msg.setText("Doctor not found.")
            self.clearFields() 
            error_msg.setStandardButtons(QMessageBox.Ok)
            error_msg.exec_()
            
    def clearFields(self):
        # Clear the input fields      
        self.lineEdit_6.clear()
        self.lineEdit_7.clear()
        self.lineEdit_8.clear()
               
    def addDoctor(self):
        from AddDoc_ui import Ui_AddDoctor
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_AddDoctor()
        self.ui.setupUi(self.window)
        self.window.show()
        
    def setAppointment(self):
        firstname = self.lineEdit_6.text()
        lastname = self.lineEdit_7.text()
        specialization = self.lineEdit_8.text()

        if firstname and lastname and specialization:
            # All fields are filled, proceed to the next window
            from App_ui import Ui_Appointment
            confirmation = QMessageBox.question(
                None, 'Confirmation', 'Are you sure you want to set an appointment?',
                QMessageBox.Yes | QMessageBox.No
            )

            if confirmation == QMessageBox.Yes:
                self.window = QtWidgets.QMainWindow()
                self.ui = Ui_Appointment()
                self.ui.setupUi(self.window)             
                self.window.show()
                
        else:
            # Fields are missing, show an error message
            error_msg = QMessageBox()
            error_msg.setIcon(QMessageBox.Critical)
            error_msg.setWindowTitle("Error")
            error_msg.setText("Please fill in all fields.")
            error_msg.setStandardButtons(QMessageBox.Ok)
            error_msg.exec_()
            
    def setupUi(self, Doctors):
        Doctors.setObjectName("Doctors")
        Doctors.resize(815, 577)
        Doctors.setStyleSheet("background-color: white;")
        self.centralwidget = QtWidgets.QWidget(Doctors)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(310, 430, 201, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.setAppointment) 
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(310, 480, 201, 41))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.addDoctor)
        self.pushButton_4.clicked.connect(Doctors.close)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(280, 40, 261, 51))
        self.label_5.setStyleSheet("font: 8pt \"MS Reference Sans Serif\"; font-size: 25px;")
        self.label_5.setObjectName("label_5")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(300, 100, 211, 31))
        self.lineEdit_5.setStyleSheet("font-size: 12pt;")
        self.lineEdit_5.setText("")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(340, 140, 141, 41))
        self.label_6.setStyleSheet("font: 8pt \"MS Reference Sans Serif\"; font-size: 25px;")
        self.label_6.setObjectName("label_6")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_6.setGeometry(QtCore.QRect(300, 290, 211, 31))
        self.lineEdit_6.setStyleSheet("font-size: 12pt;")
        self.lineEdit_6.setText("")
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(340, 240, 141, 41))
        self.label_7.setStyleSheet("font: 8pt \"MS Reference Sans Serif\"; font-size: 25px;")
        self.label_7.setObjectName("label_7")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_7.setGeometry(QtCore.QRect(300, 190, 211, 31))
        self.lineEdit_7.setStyleSheet("font-size: 12pt;")
        self.lineEdit_7.setText("")
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(320, 330, 191, 41))
        self.label_8.setStyleSheet("font: 8pt \"MS Reference Sans Serif\"; font-size: 25px;")
        self.label_8.setObjectName("label_8")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_8.setGeometry(QtCore.QRect(300, 380, 211, 31))
        self.lineEdit_8.setStyleSheet("font-size: 12pt;")
        self.lineEdit_8.setText("")
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(520, 100, 111, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.searchDoctor) 
        Doctors.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Doctors)
        self.statusbar.setObjectName("statusbar")
        Doctors.setStatusBar(self.statusbar)

        self.retranslateUi(Doctors)
        QtCore.QMetaObject.connectSlotsByName(Doctors)

    def retranslateUi(self, Doctors):
        _translate = QtCore.QCoreApplication.translate
        Doctors.setWindowTitle(_translate("Doctors", "Doctors"))
        self.pushButton.setText(_translate("Doctors", "SET APPOINTMENT"))
        self.pushButton_4.setText(_translate("Doctors", "ADD DOCTOR"))
        self.label_5.setText(_translate("Doctors", "Search Doctor\'s ID:"))
        self.label_6.setText(_translate("Doctors", "Firstname:"))
        self.label_7.setText(_translate("Doctors", "Lastname:"))
        self.label_8.setText(_translate("Doctors", "Specialization:"))
        self.pushButton_2.setText(_translate("Doctors", "Search"))

if __name__ == '__main__':
        import sys
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        ui = Ui_Doctors()
        ui.setupUi(MainWindow)
        MainWindow.show()
        sys.exit(app.exec_())