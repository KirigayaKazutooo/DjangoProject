# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\pythonproject\App.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from Doc_ui import Ui_Doctors
from Table_ui import Ui_View
import psycopg2

class Ui_Appointment(object):
        
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
          
    def addAppointment(self):
        id = self.lineEdit_6.text()
        firstname = self.lineEdit.text()
        lastname = self.lineEdit_5.text()
        age = self.lineEdit_2.text()
        gender = self.comboBox.currentText()
        contacts = self.lineEdit_3.text()
        date = self.dateEdit.date().toString('yyyy-MM-dd')
        time = self.timeEdit.time().toString('HH:mm')

        # Check if any of the required fields are empty
        if not id or not firstname or not lastname or not age or not contacts:
                QMessageBox.warning(None, "Error", "Please fill in all the required fields!")
                return

        # Check if the appointment already exists in the database
        self.cursor.execute("SELECT COUNT(*) FROM PATIENT WHERE pat_id = %s", (id,))
        count = self.cursor.fetchone()[0]

        if count > 0:
                QMessageBox.warning(None, "Error", "Appointment with the specified ID already exists!")
                return

        self.cursor.execute("INSERT INTO PATIENT (pat_id, pat_fname, pat_lname, pat_age, pat_gender, pat_contacts, pat_date, pat_time) "
                        "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
                        (id, firstname, lastname, age, gender, contacts, date, time))
        self.connection.commit()

        # Clear the fields after inserting the data
        self.clearFields()
        QMessageBox.information(None, "Success", "Appointment added successfully!")
        
    def clearFields(self):
        # Clear the input fields
        self.lineEdit.clear()
        self.lineEdit_2.clear()
        self.lineEdit_3.clear()
        self.lineEdit_5.clear()
        self.lineEdit_6.clear()
        self.dateEdit.clear()
        self.timeEdit.clear()
        self.comboBox.setCurrentIndex(0)
     
        self.lineEdit_4.clear()
        #self.dateEdit_2.clear()
        #self.timeEdit_2.clear()    
             
    def backButton(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Doctors()
        self.ui.setupUi(self.window)
        self.window.show()    
        
    def updateAppointment(self):
        id = self.lineEdit_6.text()
        firstname = self.lineEdit.text()
        lastname = self.lineEdit_5.text()
        age = self.lineEdit_2.text()
        gender = self.comboBox.currentText()
        contacts = self.lineEdit_3.text()
        date = self.dateEdit.date().toString('yyyy-MM-dd')
        time = self.timeEdit.time().toString('HH:mm')

        self.cursor.execute("UPDATE PATIENT SET pat_fname = %s, pat_lname = %s, pat_age = %s, pat_gender = %s, "
                            "pat_contacts = %s, pat_date = %s, pat_time = %s WHERE pat_id = %s",
                            (firstname, lastname, age, gender, contacts, date, time, id))
        self.connection.commit()
        

        # Show a success message
        QMessageBox.information(None, "Success", "Appointment updated successfully!")    
        
        self.clearFields()
        
    def updateDateEdit(self, date):
        self.dateEdit.setDate(date)

    def updateTimeEdit(self, time):
        self.timeEdit.setTime(time)    
        
    def searchAppointment(self):
        id = self.lineEdit_4.text()
        self.cursor.execute("SELECT pat_id, pat_fname, pat_lname, pat_age, pat_gender, pat_contacts, pat_date, pat_time FROM PATIENT WHERE pat_id = %s", (id,))
        appointment = self.cursor.fetchone()

        if appointment:
            # Doctor found, display the information
            id, firstname, lastname, age, gender, contacts, date, time = appointment
            
            self.lineEdit_6.setText(str(id))
            self.lineEdit.setText(firstname)
            self.lineEdit_5.setText(lastname)
            self.lineEdit_2.setText(age)
            self.comboBox.setCurrentText(gender)
            self.lineEdit_3.setText(contacts)
            self.dateEdit.setDate(date)
            self.timeEdit.setTime(time)
            
        else:
            # Doctor not found, show an error message
            error_msg = QMessageBox()
            error_msg.setIcon(QMessageBox.Critical)
            error_msg.setWindowTitle("Error")
            error_msg.setText("No appointment found.")
            error_msg.setStandardButtons(QMessageBox.Ok)
            error_msg.exec_()    
            
    def deleteAppointment(self):
         id = self.lineEdit_6.text()
         self.cursor.execute("DELETE FROM PATIENT WHERE pat_id = %s", (id,))
         self.connection.commit()
         
         # Clear the fields after deleting the appointment
         self.clearFields()
         QMessageBox.information(None, "Success", "Appointment deleted successfully!")     
           
    def viewAppointments(self):
        self.tableWindow = QtWidgets.QMainWindow()
        self.ui = Ui_View()
        self.ui.setupUi(self.tableWindow)
        self.tableWindow.show()

              
    def setupUi(self, Appointment):
            
        Appointment.setObjectName("Appointment")
        Appointment.resize(1047, 619)
        Appointment.setMouseTracking(False)
        Appointment.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.centralwidget = QtWidgets.QWidget(Appointment)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 170, 221, 29))
        self.label.setStyleSheet("font-size: 18pt;\n"
"")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(50, 270, 48, 29))
        self.label_2.setStyleSheet("font-size: 18pt;\n"
"")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(50, 320, 85, 29))
        self.label_3.setStyleSheet("font-size: 18pt;\n"
"")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(50, 370, 99, 29))
        self.label_4.setStyleSheet("font-size: 18pt;\n"
"")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(50, 420, 58, 29))
        self.label_5.setStyleSheet("font-size: 18pt;\n"
"")
        self.label_5.setObjectName("label_5")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(270, 170, 201, 31))
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(110, 270, 81, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(160, 370, 171, 31))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.timeEdit = QtWidgets.QTimeEdit(self.centralwidget)
        self.timeEdit.setGeometry(QtCore.QRect(270, 470, 131, 31))
        self.timeEdit.setObjectName("timeEdit")
        self.dateEdit = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit.setGeometry(QtCore.QRect(130, 420, 141, 31))
        self.dateEdit.setObjectName("dateEdit")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(150, 320, 111, 31))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(110, 520, 101, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.addAppointment)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(230, 520, 101, 41))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.clearFields)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(550, 110, 471, 51))
        self.label_7.setStyleSheet("color:rgb(85, 85, 255);\n"
"font: 8pt \"MS Reference Sans Serif\"; font-size: 38px;")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(580, 170, 391, 41))
        self.label_8.setStyleSheet("color:rgb(85, 85, 255);\n"
"font: 8pt \"MS Reference Sans Serif\"; font-size: 33px;")
        self.label_8.setObjectName("label_8")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(800, 250, 201, 31))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(560, 250, 231, 29))
        self.label_9.setStyleSheet("font-size: 18pt;\n"
"")
        self.label_9.setObjectName("label_9")
        self.dateEdit_2 = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit_2.setGeometry(QtCore.QRect(850, 380, 141, 31))
        self.dateEdit_2.setObjectName("dateEdit_2")
        self.dateEdit_2.dateChanged.connect(self.updateDateEdit)
        self.timeEdit_2 = QtWidgets.QTimeEdit(self.centralwidget)
        self.timeEdit_2.setGeometry(QtCore.QRect(850, 320, 141, 31))
        self.timeEdit_2.setObjectName("timeEdit_2")
        self.timeEdit_2.timeChanged.connect(self.updateTimeEdit)
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(550, 350, 281, 29))
        self.label_10.setStyleSheet("font-size: 18pt;\n"
"")
        self.label_10.setObjectName("label_10")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(610, 480, 111, 41))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.updateAppointment)
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(610, 530, 111, 41))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.clicked.connect(self.deleteAppointment)
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(740, 480, 111, 41))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_6.clicked.connect(self.searchAppointment)
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(890, 500, 81, 41))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_7.clicked.connect(self.backButton)
        self.pushButton_7.clicked.connect(Appointment.close)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(50, 470, 201, 29))
        self.label_6.setStyleSheet("font-size: 18pt;\n"
"")
        self.label_6.setObjectName("label_6")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(50, 220, 221, 29))
        self.label_11.setStyleSheet("font-size: 18pt;\n"
"")
        self.label_11.setObjectName("label_11")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(270, 220, 201, 31))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(110, 40, 271, 51))
        self.label_12.setStyleSheet("color:rgb(85, 85, 255);\n"
"font: 8pt \"MS Reference Sans Serif\"; font-size: 35px;")
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(50, 120, 221, 29))
        self.label_13.setStyleSheet("font-size: 18pt;\n"
"")
        self.label_13.setObjectName("label_13")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_6.setGeometry(QtCore.QRect(190, 120, 201, 31))
        self.lineEdit_6.setText("")
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(740, 530, 111, 41))
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_8.clicked.connect(self.viewAppointments)
        self.pushButton_8.clicked.connect(Appointment.close)
        Appointment.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Appointment)
        self.statusbar.setObjectName("statusbar")
        Appointment.setStatusBar(self.statusbar)
        

        self.retranslateUi(Appointment)
        QtCore.QMetaObject.connectSlotsByName(Appointment)

    def retranslateUi(self, Appointment):
        _translate = QtCore.QCoreApplication.translate
        Appointment.setWindowTitle(_translate("Appointment", "Doctors"))
        self.label.setText(_translate("Appointment", "Patient\'s Firstname:"))
        self.label_2.setText(_translate("Appointment", "Age:"))
        self.label_3.setText(_translate("Appointment", "Gender:"))
        self.label_4.setText(_translate("Appointment", "Contacts:"))
        self.label_5.setText(_translate("Appointment", "Date:"))
        self.comboBox.setItemText(0, _translate("Appointment", "Gender"))
        self.comboBox.setItemText(1, _translate("Appointment", "Male"))
        self.comboBox.setItemText(2, _translate("Appointment", "Female"))
        self.pushButton_2.setText(_translate("Appointment", "Add appointment"))
        self.pushButton_3.setText(_translate("Appointment", "Clear"))
        self.label_7.setText(_translate("Appointment", "ENTER PATIENT\'S ID TO"))
        self.label_8.setText(_translate("Appointment", "SEARCH APPOINTMENT"))
        self.label_9.setText(_translate("Appointment", "Search appointment:"))
        self.label_10.setText(_translate("Appointment", "Reschedule appointment:"))
        self.pushButton_4.setText(_translate("Appointment", "Update appointment"))
        self.pushButton_5.setText(_translate("Appointment", "Cancel appointment"))
        self.pushButton_6.setText(_translate("Appointment", "Search appointment"))
        self.pushButton_7.setText(_translate("Appointment", "Back"))
        self.label_6.setText(_translate("Appointment", "Appointment Time:"))
        self.label_11.setText(_translate("Appointment", "Patient\'s Lastname:"))
        self.label_12.setText(_translate("Appointment", "APPOINTMENT"))
        self.label_13.setText(_translate("Appointment", "Patient\'s ID:"))
        self.pushButton_8.setText(_translate("Appointment", "View appointments"))
        


if __name__ == '__main__':
        import sys
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        ui = Ui_Appointment()
        ui.setupUi(MainWindow)
        MainWindow.show()
        sys.exit(app.exec_())


