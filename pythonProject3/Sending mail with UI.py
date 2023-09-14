
"""
İt is a Udemy' course homework. Firstly I prepared Ui with QtDesigner and after that I connect button with functions.

Lastly I wanted to implement Add File button but I couldn't. Because Mail structure is defined in the send button.
If I was identified mail structure when creating class first of all, I could arrive and set mail' content.

Secondly, I wanted to show a message which display mail is sended succesfully or failed.I displayed them but after that
ı wanted to display screen shut down after 1 second but I couldn't handle it.

For sending mail, You have to use app password of mail. NOT MAIL PASSWORD!
You can create app password on 'https://myaccount.google.com/security'.

What I learned these codes :

    If any state can usable, I have to identify it on the right place.


"""


# Sending mail codes.
from sending_mail_root import Mail_sending

# Essential Module and properties
from PyQt5 import QtCore, QtGui, QtWidgets





# Successfull message window when mail is sended successfully
class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 143)
        self.horizontalLayoutWidget = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 381, 121))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)


    def retranslateUi(self, Form):
            _translate = QtCore.QCoreApplication.translate
            Form.setWindowTitle(_translate("Form", "Form"))
            self.label.setText(_translate("Form",
                                          "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Mail is sended successfully ! </span></p></body></html>"))


# Fail message window when an error occured while sending mail.
class Ui_Form2(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 143)
        self.horizontalLayoutWidget = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 381, 121))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">There occured an error.</span></p></body></html>"))

#The main window which used by us.
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(924, 652)
        #Adding Icon, Icon' path and iplementing icon to main window.
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../Downloads/logo.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)

        #Designing Interface
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(40, 80, 331, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.mail_address_label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.mail_address_label.setObjectName("mail_address_label")
        self.horizontalLayout.addWidget(self.mail_address_label)
        self.mail_address_text = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.mail_address_text.setObjectName("mail_address_text")
        self.horizontalLayout.addWidget(self.mail_address_text)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(40, 190, 331, 80))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.password_label = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.password_label.setObjectName("password_label")
        self.horizontalLayout_2.addWidget(self.password_label)
        self.password_text = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.password_text.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_text.setObjectName("password_text")
        self.horizontalLayout_2.addWidget(self.password_text)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(40, 380, 331, 80))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.receiver_label = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.receiver_label.setObjectName("receiver_label")
        self.horizontalLayout_3.addWidget(self.receiver_label)
        self.receiver_text = QtWidgets.QLineEdit(self.horizontalLayoutWidget_3)
        self.receiver_text.setObjectName("receiver_text")
        self.horizontalLayout_3.addWidget(self.receiver_text)
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(40, 490, 331, 80))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.mail_subject_label = QtWidgets.QLabel(self.horizontalLayoutWidget_4)
        self.mail_subject_label.setObjectName("mail_subject_label")
        self.horizontalLayout_4.addWidget(self.mail_subject_label)
        self.mai_subject_text = QtWidgets.QLineEdit(self.horizontalLayoutWidget_4)
        self.mai_subject_text.setObjectName("mai_subject_text")
        self.horizontalLayout_4.addWidget(self.mai_subject_text)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(40, 310, 321, 31))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(40, 20, 331, 31))
        self.label_6.setObjectName("label_6")
        self.horizontalLayoutWidget_5 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_5.setGeometry(QtCore.QRect(419, 580, 491, 31))
        self.horizontalLayoutWidget_5.setObjectName("horizontalLayoutWidget_5")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_5)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.clear_button = QtWidgets.QPushButton(self.horizontalLayoutWidget_5)
        self.clear_button.setObjectName("clear_button")
        self.horizontalLayout_5.addWidget(self.clear_button)
        self.send_button = QtWidgets.QPushButton(self.horizontalLayoutWidget_5)
        self.send_button.setObjectName("send_button")
        self.horizontalLayout_5.addWidget(self.send_button)
        self.horizontalLayoutWidget_6 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_6.setGeometry(QtCore.QRect(420, 10, 491, 41))
        self.horizontalLayoutWidget_6.setObjectName("horizontalLayoutWidget_6")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_6)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_7 = QtWidgets.QLabel(self.horizontalLayoutWidget_6)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_6.addWidget(self.label_7)
        self.horizontalLayoutWidget_7 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_7.setGeometry(QtCore.QRect(420, 60, 491, 511))
        self.horizontalLayoutWidget_7.setObjectName("horizontalLayoutWidget_7")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_7)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.content_text = QtWidgets.QTextEdit(self.horizontalLayoutWidget_7)
        self.content_text.setObjectName("content_text")
        self.horizontalLayout_7.addWidget(self.content_text)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen_txt_File = QtWidgets.QAction(MainWindow)
        self.actionOpen_txt_File.setObjectName("actionOpen_txt_File")
        self.actionSave_Mail_Message = QtWidgets.QAction(MainWindow)
        self.actionSave_Mail_Message.setObjectName("actionSave_Mail_Message")
        self.actionNew_Mail_Message = QtWidgets.QAction(MainWindow)
        self.actionNew_Mail_Message.setObjectName("actionNew_Mail_Message")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Quick Mail Sender"))
        self.mail_address_label.setText(_translate("MainWindow", " Mail Adress : "))
        self.password_label.setText(_translate("MainWindow", "  Password :  "))
        self.receiver_label.setText(_translate("MainWindow", "    Receiver :  "))
        self.mail_subject_label.setText(_translate("MainWindow", " Mail Subject :"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt;\">Mail settings</span></p></body></html>"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt;\">Login Part</span></p></body></html>"))
        self.clear_button.setText(_translate("MainWindow", "Clear"))
        self.send_button.setText(_translate("MainWindow", "Send"))
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Content</span></p></body></html>"))
        self.actionOpen_txt_File.setText(_translate("MainWindow", "Open .txt File"))
        self.actionSave_Mail_Message.setText(_translate("MainWindow", "Save Mail Message"))
        self.actionNew_Mail_Message.setText(_translate("MainWindow", "New Mail Message"))


        #These functions will called when clicked.
        self.send_button.clicked.connect(self.send_button_clicked)
        self.clear_button.clicked.connect(self.clear_button_clicked)

    def send_button_clicked(self):
        #Creating sub class and send mail at the same time.
        self.mail_send_class = Mail_sending(self.mail_address_text.text(),self.password_text.text(),self.receiver_text.text(),self.mai_subject_text.text(),self.content_text.toPlainText())

        #Control situation of whether sending is successfull or not. If it is successfull, successfull message will displayed.
        if self.mail_send_class.checking == "True":
            self.Form = QtWidgets.QWidget()
            self.ui = Ui_Form()
            self.ui.setupUi(self.Form)
            self.Form.show()

        # Control situation of whether sending is successfull or not. If it is not successfull, fail message will displayed.
        elif self.mail_send_class.checking == "False":
            self.Form = QtWidgets.QWidget()
            ui = Ui_Form2()
            ui.setupUi(self.Form)
            self.Form.show()

    #Clear function deletes all inputs
    def clear_button_clicked(self):
        self.content_text.clear()
        self.mai_subject_text.clear()
        self.receiver_text.clear()
        self.password_text.clear()
        self.mail_address_text.clear()


#Calling window
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
