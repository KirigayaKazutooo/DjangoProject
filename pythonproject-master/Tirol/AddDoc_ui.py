# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\pythonproject\AddDoc.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from Doc_ui import Ui_Doctors
from PyQt5.QtWidgets import QMessageBox
import psycopg2

class Ui_AddDoctor(object):
        
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
    
    def addDoctor(self):
        id = self.lineEdit_4.text()
        firstname = self.lineEdit.text()
        lastname = self.lineEdit_2.text()
        specialization = self.lineEdit_3.text()

        # Check if any of the required fields are empty
        if not firstname or not lastname or not specialization:
                # Inputs are invalid, show an error message
                error_msg = QtWidgets.QMessageBox()
                error_msg.setIcon(QtWidgets.QMessageBox.Critical)
                error_msg.setWindowTitle("Error")
                error_msg.setText("Please fill in all the fields.")
                error_msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
                error_msg.exec_()
                return

        # Check if the doctor with the same doc_id already exists
        self.cursor.execute("SELECT COUNT(*) FROM DOCTOR WHERE doc_id = %s", (id,))
        count = self.cursor.fetchone()[0]

        if count > 0:
                # A doctor with the same doc_id already exists, show an error message
                error_msg = QtWidgets.QMessageBox()
                error_msg.setIcon(QtWidgets.QMessageBox.Critical)
                error_msg.setWindowTitle("Error")
                error_msg.setText(f"A doctor with the ID {id} already exists.")
                error_msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
                error_msg.exec_()
        else:
                # The doctor doesn't exist, proceed with adding the doctor
                self.cursor.execute("INSERT INTO DOCTOR (doc_id, doc_fname, doc_lname, doc_type) "
                            "VALUES (%s, %s, %s, %s)",
                            (id, firstname, lastname, specialization))
                self.connection.commit()

                # Inputs are valid, show a success message
                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Information)
                msg.setWindowTitle("Doctor Added")
                msg.setText(f"Doctor {firstname} {lastname} with specialization in {specialization} has been added.")
                msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
                msg.exec_()

                self.lineEdit.clear()
                self.lineEdit_2.clear()
                self.lineEdit_3.clear()
                self.lineEdit_4.clear()
        
    def deleteDoctor(self):
        id = self.lineEdit_4.text()
        
        try:
          self.cursor.execute("DELETE FROM DOCTOR WHERE doc_id = %s", (id,))
          self.connection.commit()

          # Clear the fields after deleting the doctor
          self.lineEdit_4.clear()

          QMessageBox.information(None, "Success", "Doctor deleted successfully!")

        except Exception as e:
          # Display an error message if an exception occurs
          error_msg = QtWidgets.QMessageBox()
          error_msg.setIcon(QtWidgets.QMessageBox.Critical)
          error_msg.setWindowTitle("Error")
          error_msg.setText(f"Failed to delete the doctor. Error: {str(e)}")
          error_msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
          error_msg.exec_()  
          
    def backButton(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Doctors()
        self.ui.setupUi(self.window)
        self.window.show()    
            
    def setupUi(self, AddDoctor):
        AddDoctor.setObjectName("AddDoctor")
        AddDoctor.resize(498, 500)
        AddDoctor.setStyleSheet("background-color:rgb(255, 255, 255);\n"
"font: 8pt \"MS Reference Sans Serif\"; font-size: 35px;")
        self.label = QtWidgets.QLabel(AddDoctor)
        self.label.setGeometry(QtCore.QRect(190, 110, 141, 51))
        self.label.setStyleSheet("font: 8pt \"MS Reference Sans Serif\"; font-size: 25px;")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(AddDoctor)
        self.label_2.setGeometry(QtCore.QRect(190, 200, 151, 51))
        self.label_2.setStyleSheet("font: 8pt \"MS Reference Sans Serif\"; font-size: 25px;")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(AddDoctor)
        self.label_3.setGeometry(QtCore.QRect(130, 290, 291, 51))
        self.label_3.setStyleSheet("font: 8pt \"MS Reference Sans Serif\"; font-size: 25px;")
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(AddDoctor)
        self.lineEdit.setGeometry(QtCore.QRect(150, 170, 211, 31))
        self.lineEdit.setStyleSheet("font-size: 12pt;")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(AddDoctor)
        self.lineEdit_2.setGeometry(QtCore.QRect(150, 260, 211, 31))
        self.lineEdit_2.setStyleSheet("font-size: 12pt;")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(AddDoctor)
        self.lineEdit_3.setGeometry(QtCore.QRect(150, 350, 211, 31))
        self.lineEdit_3.setStyleSheet("font-size: 12pt;")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.pushButton = QtWidgets.QPushButton(AddDoctor)
        self.pushButton.setGeometry(QtCore.QRect(150, 390, 91, 31))
        self.pushButton.setStyleSheet("font-size: 8pt;\n"
"")
        self.pushButton.setFlat(False)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.addDoctor)
        self.pushButton_2 = QtWidgets.QPushButton(AddDoctor)
        self.pushButton_2.setGeometry(QtCore.QRect(210, 430, 91, 31))
        self.pushButton_2.setStyleSheet("font-size: 10pt;\n"
"")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.backButton)
        self.pushButton_2.clicked.connect(AddDoctor.close)
        self.label_4 = QtWidgets.QLabel(AddDoctor)
        self.label_4.setGeometry(QtCore.QRect(230, 20, 71, 51))
        self.label_4.setStyleSheet("font: 8pt \"MS Reference Sans Serif\"; font-size: 25px;")
        self.label_4.setObjectName("label_4")
        self.lineEdit_4 = QtWidgets.QLineEdit(AddDoctor)
        self.lineEdit_4.setGeometry(QtCore.QRect(150, 80, 211, 31))
        self.lineEdit_4.setStyleSheet("font-size: 12pt;")
        self.lineEdit_4.setText("")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.pushButton_3 = QtWidgets.QPushButton(AddDoctor)
        self.pushButton_3.setGeometry(QtCore.QRect(270, 390, 91, 31))
        self.pushButton_3.setStyleSheet("font-size: 8pt;\n"
"")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.deleteDoctor)
        self.retranslateUi(AddDoctor)
        QtCore.QMetaObject.connectSlotsByName(AddDoctor)

    def retranslateUi(self, AddDoctor):
        _translate = QtCore.QCoreApplication.translate
        AddDoctor.setWindowTitle(_translate("AddDoctor", "Adding doctor"))
        self.label.setText(_translate("AddDoctor", "Firstname:"))
        self.label_2.setText(_translate("AddDoctor", "Lastname:"))
        self.label_3.setText(_translate("AddDoctor", "Field of specialization:"))
        self.pushButton.setText(_translate("AddDoctor", "ADD"))
        self.pushButton_2.setText(_translate("AddDoctor", "BACK"))
        self.label_4.setText(_translate("AddDoctor", "ID:"))
        self.pushButton_3.setText(_translate("AddDoctor", "DELETE"))

if __name__ == '__main__':
        import sys
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        ui = Ui_AddDoctor()
        ui.setupUi(MainWindow)
        MainWindow.show()
        sys.exit(app.exec_())
